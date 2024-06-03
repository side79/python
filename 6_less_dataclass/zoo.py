from dataclasses import dataclass
from typing import List
from animals import Bear

# class Zoo:
#     def __init__(self, animals):
#         self.animals = animals
        
#     def __str__(self) -> str:
#         return f'In zoo are {self.animals}'

@dataclass
class Zoo:
    animals: List[Bear]