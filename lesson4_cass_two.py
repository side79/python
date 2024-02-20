class BaseVehicle:
    SOUND = ''
    
class Car(BaseVehicle):
    SOUND = 'beer'
    WHEELS = 4
    MAX_FUEL = 10_000
    
    def __init__(self, fuel=5000, fuel_consumption = 100):
        self.__fuel = fuel
        self._fuel_consumption = fuel_consumption
    
    @property
    def fuel(self):
        return self.__fuel
    
    
    #@fuel.setter
    #def fuel(self, value):
        
            
    
    def go(self, distance):
        fuel_to_spand = distance * self._fuel_consumption
        if fuel_to_spand > self.fuel:
            print(f"Cannot go, not enough fuel {self.fuel}, need {fuel_to_spand}")
            return
        self.__fuel -= fuel_to_spand
        print(f"Going {distance}, spent {fuel_to_spand}, left {self.fuel}")
    
    def add_fuel(self, value):
        print("Adding", value, "of fuel")
        self.__fuel += value
        if self.__fuel > self.MAX_FUEL:
            print("lost", self.__fuel - self.MAX_FUEL ,"of fuel")
            self.__fuel = self.MAX_FUEL
        return self.__fuel
    
class Truck(Car):
    WHEELS = 6
    MAX_FUEL = 20_000
    
    
c = Car()
print("car c consumption", c._fuel_consumption)
c.go(20)
c.go(20)
print(c.fuel)
print("adding fiel. now:", c.add_fuel(2000))
#print("car c fuel", c.__fuel)

t = Truck(fuel_consumption=200)
t.add_fuel(5000)
t.go(30)
t.add_fuel(20_000)