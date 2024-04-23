# Friday, 12th April

# km = input("Provide distance: ")
# # km_int = int(km)

# if km < 3:
#     print("You can walk")
# elif km <= 4 & km >= 15:
#     print("You can ride a bike")
# elif km > 15:
#     print("You can ride a car")

distance = int(input("Provide distance: "))# આ એક્જામ્પલ માં સમજાવેલ છે કે આપડે કેવી રીતે directly input ની અંદર integer value લઈ સકીએ નકર તો થાય છું કે input ની અંદર આપડે ગમે એ values લઈએ તો એ string બની ને save thaay variable ની અંદર 

if distance <= 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"

else:
    transport = "Car"

print("Ai recommend you the transport of:",transport)