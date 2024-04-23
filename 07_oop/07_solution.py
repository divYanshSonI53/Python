# Thursday, 18th April

# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

# static method મને સંમજાણુ નથી બરાબર 

# હવે સવાલ એ ઉઠે કે static method અથવ તો decorators હોય શું static method નો ઉપયોગ એટલે થાય છે કે કોઈ પણ class ની અંદર આપડે કોઈ એવી def બનાવી છે જેનું access આપડે object ને ના આપવું હોય એટલે થાય છે  એટલે કે આપડે direct class માં જે def બનાવેલ છે એનું નામ લખીને જ એને access કરી સકીએ ઓબ્જેક્ટ બનાવીને access કરવા જશી તો નઇ થાય 

# હવે આ example ની અંદર નીચે self નું મહત્વ સમજાવેલ છે parameters ની અંદર કે આપડે શુકામ self નો ઉપયોગ કરીએ parameters ની અંદર તો object જ્યારે class ની અંદર def ને access કરવા માંગતુ હોય તો self લગાડવું જ પડે પણ નીચે દર્શાવેલ example માં આપડે self નો ઉપયોગ નથી કરવો તો એના બદલે શું કરી સકીએ એવું કે જેના થી object બનાયવા વગર access કરી સકીએ આપડે તો એના માટે જ static method નો ઉપયોગ થાય છે 
 
class Car:

    total_cars = 0

    def __init__(self, brand, model):
        self._brand = brand
        self.model = model
        Car.total_cars =+ 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    

class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    

my_car = Car("Tata", "Safari")

Car("Tata", "Safari")

# print(my_car.general_description())

print(Car.general_description())

