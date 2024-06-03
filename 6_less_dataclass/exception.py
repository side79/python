class PositiveValueError(ValueError):
    def __init__(self, value):
        self.value = value
        
    def __str__(self) -> str:
        return f'Error, {self.value} less then real age'    
