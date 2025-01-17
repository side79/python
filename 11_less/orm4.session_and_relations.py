from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, Relationship
from datetime import datetime


engine = create_engine("sqlite:///example2.db")
Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    
    posts = Relationship("Post", back_populates="author")
    
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"
    
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False) #or author_id = Column(Integer, ForeignKey("users")) if model(class) not show, where "users" is table name

    author = Relationship(User, back_populates="posts")
    
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author={self.author})"
    
    def __repr__(self):
        return str(self)


def create_user(username:str) -> User:
    u = User(username="sam")
    
    print("id before:", u.id)
    session.add(u)
    session.commit()
    print("id after:", u.id)
    
    return User

def author_posts(title:str,) -> Post:
    user: User = session.query(User).filter_by(username="sam").one()
    print(user)
    
    #post = Post(title = "First post!", author=user)
    #session.add(post)
    #session.commit()
    #print(post)
    #print(user.posts)
    
    post = Post(title = "Second post!", author=user)
    
    session.add(post)
    
    user.posts.append(post)
    session.commit()
    
    print(user.posts)
    
    
    return Post

if __name__ == "__main__":
    #Base.metadata.create_all(engine)
    session = Session()
    #u = create_user("sam")
    
    
    session.close()