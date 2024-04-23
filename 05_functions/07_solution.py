# Saturday, 13th April

# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# નીચે દર્શાવેલ example ની અંદર sum_of_all નામ ની definition બનાવવામાં આવેલ છે જેની અંદર (*) Asterisk args નો ઉપયોગ થયેલ છે *args નો ઉપયોગ એટલે થાય કે function call કરાવવા ટાણે function માં 1 argument અથવા તો multiple arguments આવશે એ કઈ નક્કી નથી એના માટે થાય છે 

def sum_of_all(*args): # args ની જગ્યા એ આપડે ગમે એ keyword લખી sakiye પણ એ સારી practice ના કેવાય એટલે બંને ત્યાં સુધી args જ  લખવું

    print(*args) 

    print(args) # આ line માં ખાલી args print કરાવેલ છે જેના થી parameters માંથી જે કોઈ પણ values આવશે એને tuples માં convert કરી દેશે એટલે કે tuples ના લીધે એ iterable object બની જશે તો આપડે એની ઉપર loop ફેરવી સકીએ 

    for i in args:
        print(i * 2)

    return sum(args) # આ line માં sum method નો upyog કરવામાં આવેલ છે જેના ઉપયોગ થી parameters ની અંદર જેટલી values આવશે એને add કરીને function call ટાણે return કરી દેશે 

print(sum_of_all(1, 2, 3))
# print(sum_of_all(1, 2, 3, 4, 5))
# print(sum_of_all(1, 2, 3, 4, 5, 6, 7, 8))

