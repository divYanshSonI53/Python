# Friday, 12th April

age = input("provide the age: ")
age_int = int(age)
day = "Wednesday"

price = 12 if age_int >= 18 else 8 # આ example ની અંદર conditional statement એક જ line ની અંદર લખેલ છે. જેમાં સમજાવ્યું છે કે price તો 12 જ છે પણ અગર વ્યક્તિ ની age 18 અથવા તો 18 થી ઉપર હોય તો 12 છે નકર તો 18 થી નીચે હોય age તો 8 છે 

if day == "Wednesday":
    
    # price = price - 2
    price -=2

print("Ticket price for you is $", price) 
