# Wednesday, 17th April

# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# ઉપર કીધેલ છે કે Car નામ ના class માં જે brand નામ નું attribute છે એને encapsulate કરી દીઓ એટલે કે private કરી દીઓ એનો મતલબ એ થઈ કે class ની અંદર તો access થઈ જશે પણ object બનાવીને access નઇ થાય અને કીધેલ છે કે encapsulate કરી ને એના માટે getter method આપો જેના થી જ access થવું જોઈએ brand 

class Car:
    def __init__(self, brand, model):

        self.__brand = brand # આ line માં brand નામે ના variable પેલા 2 વાર underscore લગાડ્યું છે એના થી આ private થઈ ગયું છે એટલે કે આ class ની અંદર તો access થઈ સકશે પણ object through access નઇ થાય અને ઉપર કીધેલ છે કે brand attribute ને access કરવા માટે એક getter method બનાવો જે નીચે દર્શાવેલ છે ⬇️ 

        self.model = model

    def get_brand(self): # આ line માં brand ને access કરવા માટે getter method બનાવેલ છે એટલે કે જે attribute private કરી દીધું હોય અને એને access કરાવવું હોય તો જે નામ નું attribute હોય એની પેલા get_ લગાડી દેવાનું પણ get_ ની જગ્યા એ આપડે બીજું નામ ભી આપી સકીએ પણ એવું ના કરાય એ સારી practice ના કેવાય
         
        return self.__brand + "!"

    def display_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

# print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)

print(my_tesla.display_name())

print(my_tesla.get_brand())