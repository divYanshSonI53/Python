# Saturday, 13th April

# 8. Prime Number Checker
# Problem: Check if a number is prime

number = int(input("Provide the number to check if the number is prime or not:"))# number input લેવામાં આવ્યું છે 

for i in range(2, number): # for loop ની અંદર condition આપવા માં આવી છે કે range mathi 2 થી શરૂઆત કરી ને number જે આપેલ છે ત્યાં સુધી ફેરવવાની છે એક પછી એક 

    if number % i == 0: # અગર number i સાથે એટલે કે number ઈનપુટ જે આપેલ છે એની sathe divide થઈ જાય અને remainder માં 0 આવે 

        print("The number is not prime") # તો print થઈ જશે કે number જે તમે આપ્યો છે એ prime number નથી  
        break
else:
    print("The number is prime")