
a = [1, 2, 3]
b = [1, 2, 3]
c = a


print("id of a:", id(a))
print("id of b:", id(b))
print("id of c:", id(c))


print("a == b:", a == b)
print("a is b:", a is b)

print("a == c:", a == c)
print("a is c:", a is c)

num_a = 1
num_b = 1

print("num_a == num_b", num_a == num_b)
print("num_a is num_b", num_a is num_b)

print()

print(a, b, c)
a.append(4)
b.append(9)
c.append(5)
print(a, b, c)

print('a is list type?', isinstance(a, list))
print('a is list-like type?', isinstance(a, (list, tuple)), type(a))

t = ()
print('t is list-like type?', isinstance(t, (list, tuple)), type(t))

exists = True

print('type of exists', type(exists))

print("'exists' is type of int?", isinstance(exists, int))

print('exists to int', int(exists))
print('exists is 1?', exists is 1)
print('exists == 1?', exists == 1)


print("id of exists:", id(exists))
print("id of int 1:", id(int(1)))


print("type(a)", type(a))
print("type(a) is type(b)", type(a) is type(b))
print("type(a) is type(c)", type(a) is type(c))


cache = {}

def get_user(user_id):
    if user_id not in cache:
        u = ...
        cache[user_id] = u
        return u
    return cache[user_id]


u1 = get_user(7)
u2 = get_user(7)
"""
u1 == u2  # is True

u1.id == u2.id  # is True

u1 is not u2  # is True
"""

