# Wednesday, 17th April

# classes and objects

# Inheritance

# Polymorphism

# Encapsulation

# Abstraction

# હવે classes અને objects હોય શું class નો ઉપયોગ એટલે કરવામાં આવે છે કારણ કે class ની અંદર જે વારે ઘડીએ જે વસ્તુ કામ આવની છે એને આપડે class ની અંદર લખી સકીએ અને class બનાવ્યા પછી આપડે જે variable ની અંદર call કરાવીએ એને કેવાય object 

# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class. 

class Car: # આ line માં Car નામ નું class બનાવવા માં આવેલ છે 

    def __init__(self, brand, model): # આ line માં definition બનાવેલ છે જેનું નામ __init__ રાખેલ છે એટલે કે constructor કેવાય અને એના parameters ની અંદર self keyword નો ઉપયોગ કરવામાં આવેલ છે જેનો ઉપયોગ કરીને જ આપડે આ definition ની અંદર brand અને model નામ નું જે variable બનાવેલ છે એને access કરી સકીએ 

        self.brand = brand # આ line માં self.brand લખેલ છે એટલે કે એ આ definition ની અંદર બનાવેલ brand નામ નું variable છે જેની અંદર parameters માં brand માંથી જે આવશે એ self.brand માં આવી જશે 

        self.model = model

my_car = Car("Lamborghini", "Aventador")

print(my_car.brand)

print(my_car.model)

my_new_car = Car("Porsche", "Spyder 911")

print(my_new_car.brand)

print(my_new_car.model)