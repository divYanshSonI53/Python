# Saturday, 13th April

# Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.


number = int(input("Provide any number:")) # આ line ની અંદર number input લેવામાં આવેલ છે 

factorial = 1 # નવું factorial name નું variable લેવું અને એની અંદર value 1 દેવી ફરજીયાત હતી કેમ કે factorial variable ને number માં જે input આવે એની સાથે multiply કરાવા માટે 

while number > 0: # while loop નો ઉપયોગ કરેલ છે 
        
        factorial = factorial * number # આ line માં conditional statement આપેલ છે કે number ની અંદર જે સંખ્યા આપેલ છે એને factorial સાથે multiply કરતાં જાઓ એક પછી એક તો માની લો કે સંખ્યા 5 આપેલ છે તો પેલી વાર loop ફરશે ત્યારે factorial માં ઉપર પેલે થી જ 1 આપેલ છે એટલે એ 1 multiply થઈ જશે 5 સાથે અને નીચે આપેલ statement માં લખેલ છે કે જે નંબર input માં આવ્યું હોય એને 1 સાથે minus કરી દો

        number = number - 1 # એટલે કે 5 - 1 = 4


print("Factorial value of the given number is:", factorial)
