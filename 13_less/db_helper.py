URL = "sqllite:///:memoty:"

class User:
    def __init__(self, username):
        self.username = username
    
    def __str__(self):
        return self.username


class Engin:#
    def __init__(self, url):
        self.url = url

class Connection:
    def __init__(self, engine):
        self.engine = engine

    def get_admin(self):
        return User("admin")
    

def get_engine(url=URL):
