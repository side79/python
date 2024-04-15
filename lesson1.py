import sys

print('Hello world', end=" ") #end убирает перенос на другую сточку, делает прото пробел перед след выводом.

print(1+1)
print(3-1)
print(5*2)

print('max 32 bit: ', 2**32)
print('max 64 bit: ', 2**64)
print('max 64 bit from2: ', -2 ** 64 // 2, 'to', 2 ** 64//2)

print('python overload: ', 2**64 * 2**64)

print('size of 2^64', sys.getsizeof(2**64), 'bytes')

print('foo', 'bar', 'spam', 'eggs')

print('spam' + 'eggs')
print('spam' + ' end ' + 'eggs')

print(10 / 5)
print(11 / 5)
print(10 // 5)
print(11 // 5)

print(11 % 5)

print('foo' * 3)

CONSTANT_PI = 3.1415 # This is what a constant is usually called
print(CONSTANT_PI)

print(True, False)

print(True + False, False + False, True + True)

print(True is False, True is True, False is False)
l_from_list = list()
print(l_from_list)
l = [] # fast at the code level
print(l)
print(l_from_list == l)
print((l_from_list == l) is True)

a = 1
b = a
b = 2

print('a=', a, 'b=', b)

l1 = [1, 2, 3]
l2 = l1
l3 = l1
l2 = [3, 4, 5]
l4 = [1, 2, 3]
print('l1', l1, 'l2', l2, 'l3', l3, 'l4', l4)
l1[0] = 6
l3[2] = 7
print('l1', l1, 'l2', l2, 'l3', l3, 'l4', l4)
print('l1 is l3', l1 is l3)
print('l1 is l3', l1 is l4)
print('l1 is l2', l1 is l2)
print('len of l1', len(l1))

print('last array l2 elem', l2[-1])

print('pre last array l2 elem', l2[-2])

array = [1, 2, 3, 4, 5, 6, 7]
print('array[1:3]', array[1:3])
print('array[1:3]', array[0:3])
print('array[1:3]', array[:3])
print('array[1:3]', array[1:])
print('array[1:3]', array[:])

array_copy = array[:]
print(array_copy)
array_copy.append(8)
array_copy_list = list(array_copy)
array_copy_list.append(9)

print(array, array_copy, array_copy_list)

print(list('abcdifg'))

######################

num = 4

if(num % 2 ==0):
    print('num is even')
else:
    print('num is odd')
    
res = 1 - 2

if res > 0:
    print('greater than zero')
elif res < 0:
    print('smaller than zero')
else:
    print('is zero')
    
for i in array:
    print(i)
    
line = 'foo bar spam aggs baz'

print('words in line', line.split())
print('separate:')

for word in line.split():
    print(word)
    
array_words = line.split();

while array_words:
    words = array_words.pop()
    print('removed', words)
    print('remains', array_words)

print(array_words)

d= {
    1: 'A',
    2: 'B',
    3: 'C'
}

d2 = d
d[4] = 'D'

d2['foo'] = 'bar'
print(d)
print(d2.pop('foo'))
print(d)
print(d[1])
print(d[2])
print(d[3])

for k in d:
    print(k, '=', d[k])

for k, v in d.items():
    print(k, '=', v)


s = {1, 2, 3, 3, 3, 2, 1} # set has unique values
print(s)

for i in s:
    print(i)
    
#t = tuple()
#t=()
t=(1,2,3)
print(t)

dct = {
    (1,2,3): [4,5,6],
    (4,5,6): [7,8,9]
}

print(dct)
print(dct[4,5,6])

contry_codes = {'RU', 'BU', 'FR'}

print('RU?','RU' in contry_codes)
print('FR?', 'BS'  in contry_codes)

contry_codes_secondery = {'RU', 'BS', 'AU'}

print(contry_codes.difference(contry_codes_secondery))

print(contry_codes - contry_codes_secondery)

print(contry_codes.intersection(contry_codes_secondery))

print(contry_codes & contry_codes_secondery)


for i in [2, 11, 13, 4, 6, 7, 8, 9]:
    if i > 10:
        continue
    print(i)
    if i % 2 != 0:
        break

for i in [2, 4, 6]:
    if i % 2 != 0:
        break
    print(i)
else:
    print('did not break')

for i in [1]:
    print('gonna break')
    break
else:
    print('never shows')