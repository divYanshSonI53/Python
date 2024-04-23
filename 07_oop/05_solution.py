# Wednesday, 17th April

# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# હવે polymorphism નો મતલબ હોય શું તો morphism એટલે કે રૂપ ધારણ કરી શકે અને poly એટલે કે અનેક એટલે કે અનેક રૂપ ધારણ એને polymorphism કેવાય ⬇️ 

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self): # આ line માં polymorphism નો મતલબ દર્શાવેલ છે જે છે કે Car નામ ના class ની અંદર fuel_type નામ નું def બનાવેલ છે અને નીચે ElectricCar નામ ના class ની અંદર પણ fuel_type નામ નું def દર્શાવેલ છે પણ બંને values અલગ અલગ return કરે છે એને જ polymorphism કેવાય નામ એક જેવુ જ હોય પણ કામ અલગ અલગ કરે 
        
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(my_tesla.fuel_type())

my_safari = Car("Tata", "Safaari")
print(my_safari.fuel_type())