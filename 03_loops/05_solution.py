# Saturday, 13th April

# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

input_str = input("Provide String: ") # આ લઈને ની અંદર string input લેવામાં આવી છે 

for character in input_str: # આ લઈને ની અંદર input_str માંથી character ની અંદર એક પછી એક letter લેવા માં આવે છે 

    if input_str.count(character) == 1: # આ line ની અંદર count method નો ઉપયોગ કરવામાં આવેલ છે જેના થી થાય શું કે input_str નામ ની string ઉપર loop farshe એના લીધે એક પછી એક character fetch થશે input_સ્તર mathi તો count method નું કામ શું છે કે આખી string માંથી અગર એકેય character એક જ વાર આવ્યું છે તો જે if statement માં condition આપી છે એ True થઈ જશે 

        print("First non repeated character is:", character)


# ઉપર દર્શાવેલ code ને થોરોક optimised કરવો હોય તો એની રીત નીચે દર્શાવેલ che ⬇️

input_str = input("Provide String: ")

for character in input_str:
    print(character)
    if input_str.count(character) == 1:
        print("First non repeated character is:", character)
        break # આ example ની અંદર break keyword નો ઉપયોગ કરવામાં આવેલ છે જેનાથી એની પેલા જે conditional statement આપેલ છે એ અગર True થઈ જાય તો loop ત્યાં જ break થઈ જશે આગડ નઇ વધે
