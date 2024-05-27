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
