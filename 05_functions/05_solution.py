# Saturday, 13th April

# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "User"): # આ line માં definition ના parameters માં name નામ ના variable માં પેલે થી value આપેલ છે એટલે કે definition call ના time એ અગર કોઈ argument pass કરવામાં ના વી parameters ની અંદર તો default value જે છે "User" એ જ લેવામાં આવી જશે 

    return "Hello " + name + "!"

print(greet()) 
print(greet("chai aur code")) 