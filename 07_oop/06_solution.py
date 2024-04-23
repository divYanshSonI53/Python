# Thursday, 18th April

# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created

# 👆 અપ દર્શાવેલ comment માં કેવા માંગે છે કે તમે Car નામ ના class માં તમે એક variable બનાવી કેટલી cars બાઈની છે એનું ધ્યાન રાખો 


# નીચે દર્શાવેલ example માં થોરુંક સમજવું પડે કે python ની અંદર immideate garbage collect ના થાય એમ વાર લાગે 

class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        # self.total_cars += 1 # આ line માં દર્શાવેલ છે કે આપડે આવી રીતે પણ લખી સકીએ અને નીચે દર્શાવેલ છે એવી રીતે પણ લખી સકીએ 

        Car.total_cars += 1 # આ line માં લખેલ છે કે Car નામ ની ક્લાસ ની અંદર જે total_cars નામ નું variable છે એ આ __init__ નામ નું constructor નો જેટલી વાર વપ્રાસ થાય એટલી વાર 1 add કરી દીઓ 

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.fuel_type())

Car("Tata", "Safari")
Car("Tata", "Nexon")
# print(my_safari.fuel_type())

print(Car.total_cars)

