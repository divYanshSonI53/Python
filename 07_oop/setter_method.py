# Wednesday, 17th April

# આની પેલા ના example માં આપડે getter method નો ઉપયોગ જોયો તો આ example માં આપડે setter method નો ઉપયોગ જોશી ⬇️ 

# setter method નો ઉપયોગ parameters through જે values આવે એને modify કરવા માટે થાય છે 


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def set_brand(self):
#         self.brand = "Pagani"
#         return f"{self.brand} {self.model}"
    
# cars = Car("Tata", "safari")
# print(cars.set_brand())

class Person:
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("The name must be a string.")
        self._name = name

    def get_name(self):
        return self._name

person = Person("Alice")
person.set_name("Bob")
print(person.get_name())