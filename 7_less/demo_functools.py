from functools import partial, lru_cache, wraps

power_of_2 = lambda x: pow(x,2)
print(power_of_2(2))
print(power_of_2(3))

p2 = partial(pow, exp = 3)
print(p2(2))
print(p2(3))
print(p2(4))

p = partial(pow, 3)

print(p(1))
print(p(2))
print(p(3))

def my_lru_cache(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            pass
        res = func(*args)
        cache[args] = res
        return res
    return wrapper

@my_lru_cache
def fib(n):
    if n <0:
        return None
    if n < 2:
        return 1
    return fib(n-1)+fib(n-2)

print([fib(n) for n in range(100)])
    