# Wednesday, 17th April

# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

# નીચે દર્શાવેલ example માં inheritance નો ઉપયોગ કરેલ છે તો કે inheritance હોય શું inheritance એટલે કે એક class ને બીજા class માંથી જે કઈ પણ લેવું હોય એને inheritance કેવાય 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_full_name(self): # આ example માં display_full_name નામ નું function એટલે કે def બનાવેલ છે જે parameters through def __init__ constructor માંથી self.brand અને self.model જેની અંદર __init__ ના parameters માં def call ટાણે brand અને model નામ ના variable માંથી જે આવે એ self.brand માં અને self.model માં store થાય છે

        return f"{self.brand} {self.model}"
    
    
class ElectricCar(Car): # આ line માં ElectricCar નામ નું class ઉપર જે Car નામ નું class છે એને inherit કરે છે એટલે inherit કરવા માટે બસ ElectricCar નામ ના class ના parameters માં જે class ને inherit કરવું હોય એનું નામ લખવું પડે 

    def __init__(self, brand, model, battery_size):

        # Call the superclass constructor

        super().__init__(brand, model) # આ line માં super method નો ઉપયોગ કર્યો છે જેના થી ઉપર Car નામ ના class માં જે કામ થઈ ગયું છે પેલે થી ઉપર brand અને model ની અંદર આવી ગયું છે એ નીચે મોકલી દો 

        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.battery_size)

print(my_tesla.display_full_name())