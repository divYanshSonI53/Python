# Friday, 12th April

# Hietsh choudhary's example  ⬇️

# coffee_size = input("Provide Size: ")
# extra_shot = True

# if extra_shot:
#     coffee = coffee_size + " Coffee with extra shot"
# else:
#     coffee = coffee_size + "Coffe"

# print("Your order is:",coffee)

# નિછે દર્શાવેલ example ખોટું છે એટેલે એની નીચે ના example માં સાચું example દર્શાવેલ છે ⬇️ 

# નીચે દર્શાવેલ example માં input લેવા સાથે strip function અને lower function નો ઉપયોગ કરેલ છે એનાથી થશે શું કે strip function તો string ની અંદર whitespaces એટલે કે ખાલી જગ્યા કાઢીને string save કરાવશે variable ની અંદર અને એની સાથે જ lower function string જે input કરાશે એ અગર uppercase માં હશે અથવા તો lowercase માં જ હશે તો પણ string ને lowercase ની અંદર જ save કરાવવામાં આવશે variable ની અંદર  ⬇️

# coffee_size = input("Provide Size: ").strip().lower()
# extra_shot = input('''Do you want extra shot? "yes" or "no" ''').strip().lower()

# if extra_shot == "yes": #આ line ઉપર થાય છે શું કે extra_shot variable ની andar જે ઈનપુટ લેવામાં આવ્યું છે એસ અથવા તો નો એટલે કે એસ હશે તો boolean value True ગણાશે તો જ nested if ની અંદર જવામાં આવશે નકર તો boolean value no હોય એટલે કે False તો એના માટે શું કરવું એ નીચે આપેલ છે elif statement માં  ⬇️ 
#     extra_shot = True

#     if coffee_size == "small":
#         coffee = "Small Coffee with extra shot of espresso"

#         if coffee_size == "medium":
#             coffee = "Medium Coffee with extra shot of espresso"

#             if coffee_size == "large":
#                 coffee = "Large Coffee with extra shot of espresso"


#     if extra_shot == "no":
#         extra_shot = True

#         if coffee_size == "small":
#             coffee = "Small Coffee"

#             if coffee_size == "medium":
#                 coffee = "Medium Coffee"

#                 if coffee_size == "large":
#                     coffee = "Large Coffee"

# print("Your order is:",coffee)

# -------------------*-----------------------*--------------------------

coffee_size = input("Provide Coffe Size: ").strip().lower()
extra_shot = input('''want extra shot of espresso "yes" or "no" ''').strip().lower()

if coffee_size == "small":
    coffee = "Small Coffee"
elif coffee_size == "medium":
    coffee = "Medium Coffee"
elif coffee_size == "large":
    coffee = "Large Coffee"

if extra_shot == "yes":
    coffee = coffee + " with extra shot of espresso"

print("Your order is:",coffee)

