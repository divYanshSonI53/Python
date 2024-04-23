# Sunday, 14th April

# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# નીચે દર્શાવેલ example માં **kwargs નો ઉપયોગ કરવામા આવેલ છે જેનો મતલબ છે key, words arguments 

# def print_kwargs(name, power): # આ line માં print_kwargs નામ ની definition ના parameters માં name અને power નામ ના variables બનાવવા માં આવેલ છે જેમાં નીચે થી parameters ની અંદર 2 arguments pass કરવામાં આવશે તો એ accept કરી લેશે પણ સવાલ એ ઉઠે કે 2 થી વધુ arguments pass કરવી હોય key words format માં તો શું કરવું તો એના માટે જ **kwargs નો ઉપયોગ કરવામા આવે છે જે multiple arguments as a key words format માં લઈ શકે 
   
def print_kwargs(**kwargs):
    for key, value in kwargs.items(): # હવે multiple key અને values જે parameters માંથી આવે એને આપડે direct print ના કરાવી સકીએ એટલે એના માટે for loop નો ઉપયોગ કરવો pade અને item method નો 
        print(f"{key}: {value}") # આ line માં f string નો ઉપયોગ કરી parameters માં આવેલ key અને value print કરાવેલ છે 


print(print_kwargs(name = "Superman", power = "Inviniciblity"))
print(print_kwargs(name = "Superman"))
print(print_kwargs(name = "Superman", power = "Inviniciblity", enemy = "Kryptonite"))

