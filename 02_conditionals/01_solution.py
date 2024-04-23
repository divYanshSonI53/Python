# Friday, 12th April

age = int(input("Provide ma an age: "))


if age < 13:
    print("Child")# બંને example same જ છે બસ નીચે દર્શાવેલ example માં આપડે condition જે લખતા હોય એને આપડે parenthesis ની અંદર પણ લખી સકીએ 

if (age < 13):
    print("Child")# python ની અંદર indentations નું ધ્યાન બ્વ જ રાખવું પડે કેમ કે python ની અંદર conditional statements બીજી languages પ્રમાણે આપડે શું કરાવવું છે એ બધુ curly braces, parenthesis અથવા તો brackets ની અંદર ના લખવાનું હોય એના બદલે indentation નું ધ્યાન રાખવું પડે 

elif age < 20:  
    print("Teenager")

elif age < 60:

    print("Adult")

else:
    print("Senior")