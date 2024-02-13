from time import time
import sys
from functools import wraps, reduce
from operator import mul

sys.set_int_max_str_digits(0)

def secondary():
    print('secondary')

def add(a, b):
    return a + b

    
def div(a, b):
    if b == 0:
        return
    return a / b

def rain_today():
    res = ...
    if res.status == "OK":
        return res.data.will_rain  #true/false
    return None

def greed(name='world'):
    print('Hello', name)

def multiplay_lines(multiplay_lines, times, lines=None):
    if lines is None:
        lines = {}
        print('id of dict:', id(lines))
        
    for i in range(1, times + 1):
        lines[i] = multiplay_lines * i
    return lines


def power(a, paw=2):
    return a ** paw
    
def count_values(counter, *args, as_list=False):
    print(counter)
    print(args)
    if as_list:
        return [counter(v) for v in args]
    return {v: counter(v) for v in args}


def my_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0
    while start < end:
        print('yieldind', start)
        yield start
        start += step
        print("insereted v to", start)
        
        
r = range(10)
print(r)
print(list[r])
print(tuple(r))

for i in r:
    print(i, end=" ")
print()
    
s = {v for v in r}
s.add(7)
print(s)

t = (power(v, 3) for v in r)
print(t)

print('first', next(t))
print('second', next(t))

for i in t:
    print(i)
#print('last', next(t))    
def main():
    print('hello mein')
    #secondary()
    #print('a + b =', add(1, 3))
    
    #div_res = div(10, 2)
    #print('div_res', div_res)
    
    #div_res = div(10, 0)
    #print('div_res', div_res)
    #greed('Jhone')
    #geed()
    #lines = multiplay_lines('foo', 4)
    #print(lines)
    #print('id of returne dict:', id(lines))
    #print(multiplay_lines('spam', 2, lines))
    #print(multiplay_lines('bzz and aggs', 2))
    #res = count_values(power, 1, 2, 2, 4, 5, 6)
    #print(res)
    
    #res = count_values(power, 1, 2, 2, 4, 5, 6, 7, 8, 9, as_list=True)
    #print(res)
    range_g = my_range(10)
    print(range_g)
    print('next range val:', next(range_g))
    print('first next done')
    print('doing next again')
    print('next val:', next(range_g))
    print('doing next again 2')
    print(list(range_g))
    
    
#main()

def time_func(funk, *args):
    start_time = time()
    print('time before:', start_time)
    res = funk(*args)
    end_time = time()
    print('time ater:', end_time)
    print('computed in:', end_time - start_time)
    print('returning resault', res)
    return res


def timing_dec(func):
    @wraps(func)
    def wrapper(*args):
        return time_func(func, *args)
    return wrapper

def demo_decorate():
    time_func(power, 1000, 100)

@timing_dec
def new_power(a, paw=2):
    return a ** paw

#demo_decorate()

print('New pawer', new_power(1000))

@timing_dec
def new_div(a, b):
    if b == 0:
        return
    return a / b

print('new div', new_div(1000, 2))


#####################################################


values = list(range(10))

print('Values range', values)
pawered_gen = map(new_power, values)

print('pawered_gen', pawered_gen)
print(list(pawered_gen))

onli_even = filter(lambda v: v % 2 ==0, values)

print('onli_eve', list(onli_even))

res = 1
for v in values[1:]:
    res *= v
    
print('res', res)

res = reduce(mul, values[1:])

print('Res reduce:', res)


def accept_kwargs(**kwargs):
    print(kwargs)
    
accept_kwargs(foo="bazz", eggs="spam", bag=123)
123