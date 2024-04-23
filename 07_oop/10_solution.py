# Thursday, 18th April

# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

# નીચે દર્શાવેલ example માં સમજાવેલ છે કે શું આપડે multiple classes inherit કરી શકીએ તો કે હા એનો જ example નીચે દર્શાવેલ છે 

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model



class Battery:
    
    def battery_info(self):
        return "This is battery"

class Engine:
    
    def engine_info(self):
        return "This is engine"

class ElectricCar(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCar("Tesla", "Model S")

print(my_new_tesla.engine_info())

print(my_new_tesla.battery_info())