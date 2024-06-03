from exception import PositiveValueError
from dataclasses import dataclass
from food import Food

# class Bear:
#     def __init__(self, name, age, food):
#         self.name = name
#         self.food = food
#         if age < 0:
#             #raise Exception('Error, age less then real')
#             raise PositiveValueError(age)
            
#         self.age = age
        
#     def __str__(self) -> str:
#         return f'{self.name} {self.age}'
@dataclass
class Bear:
    name: str
    age: int
    food: Food
    
    def __post_init__(self):
            if self.age < 0:
                #raise Exception('Error, age less then real')
                raise PositiveValueError(self.age)