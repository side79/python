def my_fink():
    """
        My demo fink
    """
    pass

print(my_fink.__name__, my_fink.__doc__)

def _get_con(*args):
    print('creating con', args)
    return ...

def get_connection(*args):
    if get_connection.con is None:
        get_connection.con = _get_con(*args)
    return get_connection.con

get_connection.com = None

conn1 = get_connection
coon2 = get_connection

print('coon1 is conn2', conn1 is coon2)