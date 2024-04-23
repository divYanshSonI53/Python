# Thursday, 11th April

# tuples

# હેવ tuples અને list લઘભગ એક જેવા જ હોય છે વધારે કઈ difference છે નઇ કઈ બંને માં બસ major difference એ જ છે કે list mutable હોય છે અને tuples immutable હોય છે અને એના સિવાય ના difference નીચે દર્શાવેલ છે  ⬇️

# tuples

# tuples are immutable

# tuples are faster than list

# tuples use less memory

tea_types = ("Black", "Green", "Oolong")
print(tea_types)

# tuples માં indexing use કરી આપડે જાની સકીએ કઈ position ઉપર કઈ value છે list ની જેમ જ  ⬇️ 

print(tea_types[0])

print(tea_types[-1])

# Slicing ⬇️ 

print(tea_types[1:])

# tuples ની અંદર આપડે values ના બદલી સકીએ એનું example નીચે દર્શાવેલ છે ⬇️

# tea_types[0] = "Masala"

# length ⬇️ 

print(len(tea_types))


# નીચે example માં દર્શાવેલ છે કે આપડે કેવી રીતે 2 tuples ને joint કરી સકીએ અને જે tuple પેલા લખ્યું છે એ આગડ add થઈ જશે અને જે tuple પછી લખ્યું છે એ પાછડ add થઈ જશે ⬇️ 

more_tea = ("Herbal", "Earl Grey")

all_tea = more_tea + tea_types

print(all_tea)

# નીચે example માં દર્શાવેલ છે કે આપડે question પણ પૂછી સકીએ જેમ કે નીચે પૂછ્યું છે કે શું all_tea ની અંદર Green છે તો કે હા એટલે print ની અંદર જે statement છે એ print થઈ જસે
 
if "Green" in all_tea:
    print("Green tea is in the list")


# count method ⬇️ 

more_tea = ("Herbal", "Earl Grey", "Herbal")

print(more_tea)

print(more_tea.count("Herbal"))
print(more_tea.count("Herb"))

# નીચે example માં દર્શાવેલ છે કે આપડે કેવી રીતે tuples નો જ ઉપયોગ કરી tuples માંથી values fetch કરી સકીએ પણ શરત એક જ છે કે જે tuple માંથી values fetch કરીએ છીએ એની length એક સરખી જ હોવી જોઈએ ⬇️ 

print(tea_types)

(black, green, Oolong) = tea_types # આ example માં tuple ની અંદર black, green, oolong as a variable બની ગયા છે અને એની અંદર tea_types ની જે values છે એ આવી ગઈ છે  

print(black)
print(green)
print(Oolong)

# type method ⬇️ 

print(type(tea_types))

# nested tuple ⬇️ 

nested_tuple = (1, 2, 3, (4, 5, 6))

print(nested_tuple)

nested_tuple = ("Hello Kaise",(1, 2, 3), "hain aap sab")

print(nested_tuple)

# nested tuple ની અંદર થી values કેવી રીતે fetch karvi ⬇️ 

print(nested_tuple[0])
print(nested_tuple[1][2])
print(nested_tuple[2])

# ----------------------------*---------------------------------*---------------------------

