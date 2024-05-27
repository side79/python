import traceback

class PositiveValueError(ValueError):
    def __init__(self, value):
        self.value = value
        
    def __str__(self) -> str:
        return f'Error, {self.value} less then real age'    

class Bear:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            #raise Exception('Error, age less then real')
            raise PositiveValueError(age)
            
        self.age = age
        
    def __str__(self) -> str:
        return f'{self.name} {self.age}'    
    
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