import redis
from time import sleep

r = redis.Redis()

print(r.get("foo"))
print(r.set("qwe", 123))
print(r.get("qwe"))

print(r.setex("qwerty", 1, "qwer"))

print(r.get("qwerty"))
sleep(1)
print(r.get("qwerty"))


