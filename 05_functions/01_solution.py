# Saturday, 13th April

# python ની અંદર function ને def એટલે કે definition keyword use કરી ને બનાવવા માં આવે છે function બનાવવા માટે function અથવા તો fun keyword નો ઉપયોગ થતો નથી 

# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

def square_of_number(number): 
    # print(number ** 2)
    return number ** 2 


# square_of_number(4) # આ line ની અંદર definition call કરેલ છે જેનાથી definition ની અંદર print ની અંદર જે લખેલ છે એ print થઈ જશે  

result = square_of_number(4) # આ line ની અંદર example આપ્યુ છે કે definition ને variable ની અંદર store કરાવવાશે તો એ store નઇ થાય એટલે એના માટે definition ની અંદર values return કરાવવી પડે 

print(result)

print(square_of_number(13)) # values return થયા પછી એને આપડે variable માં store ના કરાવવું હોય અને direct print કરાવવું હોય તો પણ કરાવવી સકીએ 

