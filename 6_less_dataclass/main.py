from animals import Bear
from zoo import Zoo
from food import Food


food = Food('Mead', 'sweets')
bear = Bear('Faust', 1, food)

zoo = Zoo([])

zoo.animals.append(bear)

print(zoo.animals)