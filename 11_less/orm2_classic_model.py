from sqlite3.dbapi2 import *
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper

engin = create_engine("sqlite:///example.db")
metadata = MetaData()

users_talbe = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, default=False),
)

#class User:
    #def __init__(self) -> None:
        #pass
        
class User:
    def __init__(self, id:int, username:str, is_staff:bool):
        """_summary_

        Args:
            id (int): _description_
            username (str): _description_
            is_staff (bool): _description_
        """
        self.id = id
        self.username = username
        self.is_staff = is_staff
        
mapper(User, users_talbe)
        

if __name__ == "__main__":
    metadata.create_all(engin)
