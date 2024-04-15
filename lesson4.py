class Point():
    all_instans = []
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.all_instans.append(self)
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    
    def __repr__(self) -> str:
        return str(self)
        

print(Point.all_instans)
p = Point(1,2)
print(Point.all_instans)

#p.x = 1

#p.y = 2

print(p)