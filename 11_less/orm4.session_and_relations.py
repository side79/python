from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, Relationship
from datetime import datetime


engine = create_engine("sqlite:///example2.db")
Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

post_tags_table = Table(
    "posts_table",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    posts = Relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"
    
    def __repr__(self):
        return str(self)


class Tag(Base):  # Исправлено название класса
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)

    posts = Relationship("Post", secondary=post_tags_table, back_populates="tags")  # Указан правильный класс

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)

    author = Relationship(User, back_populates="posts")
    tags = Relationship("Tag", secondary=post_tags_table, back_populates="posts")  # Указан правильный класс

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author={self.author})"

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    u = User(username=username)

    print("id before:", u.id)
    session.add(u)
    session.commit()
    print("id after:", u.id)

    return u

def create_tags():
    user = session.query(User).filter_by(username="sam").one()
    user.is_staff = True

    tags = [Tag(name=name) for name in ("news", "flask", "django", "python")]
    post = Post(title="News Flask vs Django", author=user)
    post.tags.extend(tags)

    session.add(post)
    session.commit()

    print(post, post.tags)

    for tag in tags:
        print(tag, tag.posts)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session()
    
    # users = session.query(User).filter(
    #     User.id > 1,
    #     User.username != "sam2"
    # ).all()
    
    # print(users)
    
    
    #posts = session.query(Post).all()
    
    #print(posts, posts.tags)

    # for post in posts:
    #     print(post, post.tags)
        
    
    flasks_posts = session.query(
        User
    ).join(
        Post,
        User.id == Post.author_id
    ).filter(
        Post.tags.any(Tag.name.ilike("new%"))
    )
    
    print()
    print()
    print(flasks_posts)
    print()
    print()
    print(flasks_posts.all())
    print()
    
    test_qr = session.query(
        Post
    ).filter(
        Post.author_id == 1
    ).all()
    
    print(test_qr)

    session.close()
