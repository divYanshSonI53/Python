# Saturday, 13th April

# 4. Reverse a String
# Problem: Reverse a string using a loop

input_str = input("Provide String: ") # આ line ની અંદર string input લેવા માં આવી છે 

reversed_str = "" # આ line ની અંદર નવું variable બનાવવા માં આવેલ છે અને empty string રાખવા માં આવેલ છે 

for character in input_str: # આ line ની અંદર character નામ નું નવું કરિયાબળે બનાવવા માં આવ્યું છે જેની અંદર input_str માં થી loop જેટલી વાર ફરશે એટલે કે input_str string ની અંદર થી એક પછી એક letter આવી જશે 

    # reversed_str = reversed_str + character અગર આવી રીતે લખતા તો સીધે રીતે જ string store થતી reversed_str ની અંદર 

    reversed_str = character + reversed_str # હવે આ line ની અંદર શું થાય છે મૂળ એ સમજવા જેવુ છે તો કે reversed_str નામ ની જે empty string ઉપર બનાવેલ છે એની અંદર એક પછી એક character આવે છે input_str માં થી એ add થતાં જાય છે reversed_str ની અંદર reversed_સ્તર = "p", "yp", "typ", "htyp", "ohtyp", "nohtyp"

print("Original String: ",input_str) 

print(reversed_str)