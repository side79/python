import traceback
#All moduls or (import animals as n)
#import animals
from animals import Bear, PositiveValueError

from core.animals import Bear, PositiveValueError #from folder


# bear = Bear('Faust', 5)

# print(bear)

# bear = Bear('Faust', -5)

# print(bear)

name = 'Faust'
age = int(input('Read age: '))

try:
    bear = Bear(name, age)
except PositiveValueError as e:
    #print(f'Error is name:  {e}')
    print('Error is name:', traceback.format_exc()) # it's only dev not for user
except ValueError as e:
    print(f'Error is name: {e}')
except Exception as e:
    print('Here error Exception')
else:
    # No error
    print(f'It is {bear.name}, its {bear.age}', )
finally:
    # always executed
    print('always executed')
    
print('end')