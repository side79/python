from dataclasses import dataclass

@dataclass(frozen=True) # frozen does it not change class
class Food:
    name: str
    type_food: str

# class Food:
#     def __init__(self, name, food_type):
#         self.name = name,
#         self.food_type = food_type


if __name__ == '__main>__':
    food = Food('Med', 'sweets')
    
    food_2 = Food('Med', 'sweets')
    
    print(food)
    print(food == food_2)
    
    food.name = '123' #This method doesn't work because I set rozen=True
    print(food)
    