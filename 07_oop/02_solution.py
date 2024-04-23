# Wednesday, 17th April

# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

# આગળ example માં આપડે એક constructor બનાવાયું તું પણ આ example માં આપડે class ની andar function એટલે કે definition બનાવશી 


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_full_name(self): # આ line માં Car નામ ના class ની અંદર display_full_name નામ ની definition બનાવવામાં આવેલ છે જે parameters through definition __init__ માંથી self.brand અને self.model માંથી એની અંદર જે હોય એ fetch કરે છે અને નીચે f string return કરે છે 

        return f"{self.brand} {self.model}"

my_car = Car("Tata", "Safari")

print(my_car.display_full_name()) # આ line માં દર્શાવેલ છે કે આપડે કેવી રીતે Car નામ ના class માંથી display_full_name નામ ની def માંથી f string જે return કરેલ છે એને access કરી સકીએ . નો ઉપયોગ કરી ને  