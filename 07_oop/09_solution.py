# Thursday, 18th April

# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

# 👆 ઉપર પૂછ્યું છે કે શું my_tesla instance એટલે કે object Car અને ElectricCar નામ ના class નું જ છે તો જવાબ આવશે True અથવા તો False માં જેનું example નીચે દર્શાવેલ છે ⬇️ 

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"


my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

print(isinstance(my_tesla, Car)) # આ line  માં પૂછ્યું છે કે શું my_tesla Car નામ ના class નું object છે તો કે હા એટલે result માં True આવશે

print(isinstance(my_tesla, ElectricCar)) # આ line માં પૂછ્યું છે કે શું my_tesla ElectriCar નામ ના class નું object છે તો કે હા એટલે result માં True આવશે 