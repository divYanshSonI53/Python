# Thursday, 18th April

# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

# હવે ઉપર કીધેલ છે કે તમે જે constructor બનાવીને parameters through model માં જે value આવતી હોય ગમે એ એને read-only બનાવી દો એટલે કે એની value change ના કરી શકાય એવું બનાવી દો @property decorator થી તો આપડે આગળ example માં જોયું છે કે આપડે class ની અંદર def ની અંદર જે variable બનાવેલ છે એનું access ના કરી શકાય એવું બનાવવું હોય તો એની આગડ 2 વાર (__) લગાડી દઈએ તો access ના થઈ શકે નીચે દર્શાવેલ example માં પણ કઈ ક એવી જ રીતે છે


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model # આ લઈને માં model પેલા 2 વાર underscore લગાવ્યું છે એટલે કે private કાર દીધું છે હવે model ને access અથવા તો overwrite નઇ કરી શકાય પણ aapde model ની andar શું છે એ જોવું હોય તો એના માટે નીચે method બનવું પડે એટલે નીચે method બનાવેલ છે  

    @property  # આ line માં @property decorator નો ઉપયોગ કરેલ છે એનો મતલબ એ છે કે આપડે intentionally એક property hide કરવા માંગીએ છીએ અને છતાઈ access કરવું હોય તો method through જ access થાય ⬇️  
    def model(self):
        return self.__model

my_car = Car("Tata", "Safari")
print(my_car.model) # આ line માં model ને access કરવા માટે my_car.model() ના બદલે my_car.model લખીને કરવામાં આવ્યું છે કેમ કે property decorator ની અંદર return self.model લખ્યું છે એટલે કે એ model ને as a property return કરે છે તો એની પાછડ parenthesis નઇ લાગે  