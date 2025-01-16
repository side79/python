from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

engine = create_engine("sqlite:///example2.db")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
