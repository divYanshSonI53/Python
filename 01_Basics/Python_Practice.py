# Tuesday, 9th April

# python ની અંદર list [] brackets use કરી ને બને dictionary {} curly braces use કરી ને બને અને tuples () parenthesis use કરી ને બને  

# Booleans is treated as numbers in python for true(1) and for false(0) 

x = 2
y = 3
z = 4

print(x+y)

print(x+y*z) # આ સારી practice ના કેવાઈ કેમ કે આમાં પેલા સુ થસે એ અપડને નથી ખબર જેમ કે multiplication થસે કે addition થસે પેલા એટલે તો સવાલ એ ઉઠે ક કરવું શું  

# print((x + y) * z)  જે કામ પેલા કરાવું હોય એને parenthesis ની અંદર લઈ લેવાના 

print(40 + 2.23) # આ સારી practice ના કેવાય  કેમ કે બંને data type એક સરખા હોવા જોઈએ તો સારું રહીએ વધારે તો સવાલ એ ઉઠે કે કરવું શું 


print(40 + int(2.23))

# અથવા તો
 
print(float(40) + int(2.23)) # આમ પણ થાય 

# 👆 આને operator overloading કેવાય 👆

print('chai' + 'aur' + 'code')

print(x, y, z)

print(x + 1, y * 2) # એક જ લાઇન માં બધુંય કરાવું હોય તો (,) આપીએ એટલે થઈ જાય

print(y % 2) # remainder કાઢવા માટે 

print(z ** 2) # power ગોતવા માટે, આમાં થાય છે શું કે z માં શું value છે ? 4 તો 4 multiply  થઈ જશે 2 વાર 

print(z ** 5)

print(100 ** 2)

print(2 ** 100)

print(2 ** 1000)

result = 1/3.0

print(result)

repr('chai')

str('chai')

print('chai')

# comparison

print(1 < 2) # python ની અંદર boolean value true નું T પણ capital છે અને false નું F પણ અને Python ની અંદર True ને 1 પણ કેવાય અને False ને 0 પણ કેવાય

print(5.0 == 5.0)

print(4.0 != 5.0)

print(x, y, z)

print(x < y < z) # હવે આમાં થાય છે શું કે comparison કરવા માટે આ રીત સાચી જ છે પણ આ રીત નો વપ્રાસ બંને ત્યાં સુધી ના કરાય જેમ ક આ example માં પૂછવા સુ માંગે છે કે શું 'x' 'y' થી નાનું છે તો કે હા નાનું છે ને પરત પૂછે છે કે શું 'y' 'z' થી નાનું છે તો કે હા નાનું છે તો આમાં કરાય શું એ નીચે દર્શાવેલ છે ⬇️

print(x < y and y < z) # આમાં and operator નો ઉપયોગ કરેલ છે અને બંને ત્યાં સુધી આનો જ ઉપયોગ કરાય 

print(x < y or y > z) # આમાં or operator નો ઉપયોગ કરેલ છે અને બંને ત્યાં સુધી આનો જ ઉપયોગ કરાય

# હવે ઘણી વાર આમાં સવાલ સુ ઉઠે કે ⬇️

print(1 == 2 < 3) # આમ બંને ત્યાં સુધી ના લખાય એના બદલે નીચે દર્શાવેલ છે એમ લખો ⬇️

print(1 == 2 and 2 < 3)

#  હવે python ની અંદર ઘણી વાર એવું જોઈએ છે અપડે કે ઘણા લોકો third party libraries નો પણ ઉપયોગ કરે છે એન કરવો પણ જોઈએ એના થી અપડો code powerful થઈ જાય 
# જેમ કે ⬇️ 

import math
print(math.floor(3.5)) 
print(math.floor(-3.5)) # હવે આમાં floor કરે છે શું કે નંબર નીચે સૌથી નજીકનું મૂલ્ય round off કરીને આપડને result આપે છે જેમ કે ⬇️ 

print(math.floor(3.6))
print(math.floor(3.9))

# Wednesday, 10th April

print(math.trunc(2.8)) # હવે આમાં તરુંક કરે છે શું કે number line માં 0 બાજુ લઈ જાય છે એટલે કે આ ઉદાહરણ માં 2.8 લખ્યું છે તો 2 round off થઈ ને આવી જસે

print(math.trunc(-3.1 )) # હવે આમાં તરુંક કરે છે શું કે number line માં 0 બાજુ લઈ જાય છે એટલે કે આ ઉદાહરણ માં -3.1 લખ્યું છે તો 3 round off થઈ ને આવી જસે

# Python માં number precision almost infinite હોય છે જેમ કે ⬇️ 

print(9999999999999999999999999999 + 1)

print(9999999999999999999999999999 + 2.1) # પણ અગર decimal value હોય તો આ રીત ના ચાલે કેમ કે સરખો જવાબ ના મડે તો એના માટે કરવું શું ⬇️ 

# from decimal import Decimal

# # This will maintain precision for the integer part

# print(99999999999999999999999 + Decimal('22.1'))

# Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
# Decimal('0.3')

# Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')

print((2 + 1j) * 3) # આ ઉદાહરણ ને imaginary numbers અથવા તો iota numbers પણ કેવાય 

#  Binary, Octal and Hexadecimal Examples ⬇️ 

# octal value કેમ સોધવી એનું ઉદાહરણ ⬇️ 

print(0o20)

# Reverse octal

print(oct(64))

# Hexadecimal value કેમ સોધવી એનું ઉદાહરણ ⬇️

print(0xff)

# Reverse hexadecimal

print(hex(64))

# Binary value કેમ સોધવી એનું ઉદાહરણ ⬇️

print(0b1000)

# Reverse binary

print(bin(64))

# હવે ઉપર 👆 દર્શાવેલ રીત યાદ રીએ ના રીએ એના માટે આપડે બીજુ શું કરી સકીએ

print(int('10000', 2)) # binary 
print(int('64', 8)) # octal
print(int('64', 16)) # hexadecimal

# Random Methods 

import random

print(random.random())
print(random.random())

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

l1 = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(l1))
print(random.choice(l1))
print(random.choice(l1))
print(random.choice(l1))

print(random.shuffle(l1))
print(l1)

print(random.shuffle(l1))
print(l1)

# Fraction

# from fractions import Fraction

# myFra = Fraction(2, 7) # Fraction barckets ની અંદર જે લખ્યું છે (2, 7) એટલે કે 2 upon 7
# print(myFra)

# Next datatype 

# Sets

setone = {1, 2, 3, 4}

print(setone & {1, 3}) # intersection
print(setone | {1, 3}) # union
print(setone | {1, 3, 7}) # union
print(setone - {1, 3}) # difference

print(setone ^ {1, 3}) # symmetric difference

print(setone - {1, 2, 3, 4})# આમાં સુ થાય છે કે result માં set{} લખેલું આવસે કેમ કે {} Parenthesis એક પ્રકાર ની empty dictionary હોય છે   

print(type({})) # જેમ કે આ example માં કોઈ પણ object નો પ્રકાર કેમ ગોતવો એ દર્શાવેલ છે

# Boolean data type 

# print(type(true))
# print(type(false))

# next datatype 

# String

chai = "Masala Chai"
print(chai)
first_char = chai[0]
print(first_char) # Fetching String's First Character

last_char = chai[-1]

print(last_char) # Fetching String's Last Character


# String Slicing

slice_chai = chai[0:6]
print(slice_chai) 

num_list = "0123456789"

print(num_list[:])

print(num_list[3:])

print(num_list[:7])

print(num_list[0:5])

print(num_list[5:10])

print(num_list[0:10:2]) # આ example માં સુ થાય છે કે ત્રીજું digit છે એટલે કે ત્રીજું parameter આપેલું છે 2 તો એમ થાય કેઃ શું કે 1-1 digit કે letter ગમે એ કયો string માં એ મૂકીને રિજલ્ટ આપે છે જેમ કે એના બદલે અગર 3 લખ્યું હોય તો 2-2 digit કે letter મૂકીને રિજલ્ટ અપસે ⬇️ 

print(num_list[0:10:3])

print(num_list[::-1])


print(chai)

print(chai.lower()) #Lowercase 

print(chai.upper()) #Uppercase

print(chai.title()) #Titlecase

chai = "   Masala Chai   "

print(chai) 
print(chai.strip()) # strip નો ઉપયોગ string ની અંદર spaces કાઢવા માટે હોય છે 

chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger")) # replace method નો ઉપયોગ string ની અંદર કઈ પણ replace કરવા માટે થાય છે બીજું ઉદાહરણ ⬇️ 

print(chai.replace("Lemon", "Ginger", 1))

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", ")) # split method ની અંદર parenthesis ની અંદર parameters આપવું એ સારી practice કેવાય છે જેમ કે આમાં parenthesis ની અંદર (, અને space આપ્યું છે) એટલે કે એના થી જે લિસ્ટ બનસે એની અંદર comma અને space ના ગણાય

chai = "Masala Chai"
print(chai.find("Chai"))

print(chai.find("chai")) # આ example માં "chai" નો first letter small છે એટલે find method શોધી ના સક્યુ એટલે એનું result negative index માં આવે 

chai = "Masala Chai Chai Chai"
print(chai.count("Chai")) # આ example માં string ની અંદર count method નો ઉપયોગ કરી parameters માં જે શોધવું હોય એ pass કરી અપડે જાની સકીએ કે એ વસ્તુ કેટલી વખત string માં આવી છે જેમ કે count  method નું બીજું example નીચે દર્શાવેલ છે ⬇️ 

chai = "Divyansh soni"
print(chai.count("s"))

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)

# format method ના example માં દર્શાવેલ છે કે curly braces {} એટલે કે placeholder નો ઉપયોગ કરીએ string ના statement માં તો એ print કરાવા format method નો ઉપયોગ કરી એમ parameters pass કરવા પડે એનો example નીચે દર્શાવેલ છે જેમ કે નીચેના example માં variables as a parameters pass કર્યા છે ⬇️ 

print(order.format(quantity, chai_type))

print(order.format(chai_type, quantity))

chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety)

# નીચે ⬇️ example માં દર્શાવેલ છે કે આપડે કેવી રીતે ઉપર જે list દર્શાવેલ છે એનો ઉપયોગ કરી list ની value બધી joint કરાવી સકીએ અને એની આગડ "" નો ઉપયોગ કરી એમ જણાવી સકીએ કે list ની અંદર જે value છે એની અંદર આપડને space જોય hyphen જોય અથવા તો ગમે એ વસ્તુ કરાવી સકીએ 
 
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(", ".join(chai_variety))

chai = "Masala Chai"
print(chai)

# String Length જાણવા માટે નીચે દર્શાવેલ મેથડ નો ઉપયોગ થઈ છે ⬇️ 

print(len(chai))

for letter in chai:
    print(letter)
# નીચે દર્શાવેલ example માં string statement ની અંદર અગર ("") double quotes નો ઉપયોગ કરવો હોય તો (\) backslash અથવા તો આખું statement ('') single quotes ની અંદર લખી શકાય છે 
 
chai = "He said, \"Masala chai is awesome\""
print(chai)

chai = 'He said, "Masala chai is awesome"'
print(chai)

# raw string example જ્યારે આપડને (\) backslash use કરવું string statement કેમ કે (\) એક unicode character escaping કેવાય એટલે એના માટે raw string નો ઉપયોગ કરવો પડે અથવા તો windows માં path દેવા માટે આનો વપ્રાસ થાય છે 

chai = "Masala\nChai"
print(chai) # આ example માં થસે શું કે \n નો ઉપયોગ કરેલ છે એટલે Masala પછી એક line મૂકીને ચા લખેલું આવી જસે result માં 

chai = r"Masala\nChai"
print(chai)

chai = r"C:\Users\Divyansh\Downloads"
print(chai)

# string માં આપડે સવાલ પણ પૂછી સકીએ જેમ કે નીચેના example માં print કરાવ્યું છે ત્યાં દર્શાવેલ છે code માં કે શું તમારી chai નામ ની string માં Masala છે ? તો આનો જવાબ boolean value માં અવસે true અથવા તો false 

chai = "Masala Chai"
print("Masala" in chai)

chai = "Masala Chai"
print("aa" in chai)

# નીચેના example માં દર્શાવેલ છે કે list ની અંદર નો જે data છે એ indexing use કરી fetch કરીએ છીએ 
 
tea_varieties = ["black", "Green", "Oolong", "white"]
print(tea_varieties[-1])
print(tea_varieties[0])
print(tea_varieties[1])
print(tea_varieties[2])
print(tea_varieties[3])

# List ના slicing dicing examples ⬇️ 

print(tea_varieties[1:3])
print(tea_varieties[1:4])
print(tea_varieties[:4])
print(tea_varieties[2:])

tea_varieties[3] = "Herbal"
print(tea_varieties)

# tea_varieties[1:2] = "Lemon"
print(tea_varieties) # આ example માં શું થાય છે કે tea_varieties variable માં જે parameter pass કર્યું છે [1:2] એમ select શું થસે કે 1 થી લઈ ને 2 સુધી જાય ને એમ છેલું index select ના થાય એ તો normal છે તો select સુ થશે કે 1 જ તો green ની જગ્યા એ lemon આવી જસે પણ એ lemon word નું પણ slicing થઈ જશે તો એનું result આવસે ['black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']

tea_varieties[1:2] = ["Lemon"]
print(tea_varieties) # હવે આ example માં દર્શાવેલ છે કે ઉપર જે example છે માં ભૂલ થાય છે એના થી બચવું કેમ તો આ example માં થયું છે શું કે Lemon ને as a list treat કરવામાં આવ્યું છે હવે આમાં આપડને જોવાનું છે શું કે શું અપડે એક કરતાં વધારે data list માં બદલી સકીએ કે નઇ ⬇️ 

tea_varieties[1:2] = ["Masala", "Ginger"]
print(tea_varieties)

print(tea_varieties[1:1]) # હવે આ example માં શું થાય છે કે parameters માં starting point આપ્યુ છે 1 અને એન્ડ પણ કરાવ્યું છે 1 ઉપર જ એટલે આનું result આવસે [] list ની અંદર કઈ નઇ એટલે આનો ઉપયોગ લિસ્ટ ની અંદર data delete કરવામા પણ આવે છે હવે આગડ ⬇️

tea_varieties[1:1] = ["test", "test"]
print(tea_varieties)

print(tea_varieties[1:2])

print(tea_varieties[1:3])

tea_varieties[1:3] = []

print(tea_varieties)

for tea in tea_varieties:
    print(tea)

# for tea in tea_varieties:
    # print(tea, end="-") # હવે આ example માં શું થાય છે કે print ની અંદર જે statement માં end નો ઉપયોગ કર્યો છે અને એની અંદર જે - ઉપયોગ કર્યો છે એના થી થાય છે શું કે result new line ની અંદર નઇ આવે એના બદલે એક જ line માં અવસે પણ - સાથે 

print(tea_varieties)

if "Oolong" in tea_varieties:
    print("Oolong is in the list")

# Append Method નું example 

print(tea_varieties)
print(tea_varieties.append("Oolong"))
print(tea_varieties)

if "Oolong" in tea_varieties:
    print("I have Oolong Tea")

# Remove method નું example 

print(tea_varieties.remove("Oolong"))
print(tea_varieties) # remove method ના example માં થાય છે શું કે એની અંદર જે parameter આપો એ list માં થી કાઢી નાખે પણ એક જ વાર 

# pop method નું example

print(tea_varieties.pop())
print(tea_varieties) # pop method નો ઉપયોગ લિસ્ટ ની અંદર last value કાઢવા માટે થાય છે અગર એની અંદર કઈ parameters ના આપ્યા હોય તો પણ અગર એની અંદર indexing નું યુઝ કરી parameters આપ્યા છે તો એ delete થઈ જશે જેનું example નીચે આપેલ છે ⬇️ 

print(tea_varieties.pop(3))
print(tea_varieties)

# List ની અંદર insert method નો upyog નો example ⬇️ 

tea_varieties.insert(1, "Green")
print(tea_varieties) # insert method નો ઉપયોગ indexing નો ઉપયોગ કરી કોઈ પણ specific જગ્યા ઉપર data insert કરવા માટે થાય છે 

tea_varieties.insert(4, "Oolong")
print(tea_varieties)

# copy method નો ઉપયોગ નીચે દર્શાવેલ છે ⬇️ 

tea_varieties_copy = tea_varieties
print(tea_varieties_copy) # આ example માં શું થાય છે કે tea_varieties_copy નામ નું નવું variable બનાવ્યું છે ને એની અંદર tea_varieties list નું reference આપ્યુ છે બસ એની કોપી નથી બની આ example માં તો copy કરવા માટે કરવું શું એનું example નીચે દર્શાવેલ છે ⬇️ 

tea_varieties_copy = tea_varieties.copy()
print(tea_varieties_copy) # આ example માં શું થાય છે કે copy method નો ઉપયોગ કરેલ છે તો એના લીધે memory માં એક નવું reference બને છે tea_varieties_copy નું જેમાં tea_varieties લિસ્ટ ની copy છે ટુંક માં memory માં નવી જગ્યા રોકાય છે અને main list ને કઈ પણ નઇ થાય 

tea_varieties_copy.append("Lemon")
print(tea_varieties_copy)

# range method ના examples નીચે દર્શાવેલ છે ⬇️ 

print(range(10))

x = range(10)

for x in range(10):
    print(x**2) # હવે આ example માં થયું છે શું કે પેલા તો x નામ નું variable declare કર્યું che અને એની અંદર range આપી che 1 થી લઈ ને 10 સુધી ની એના પછી for loop નો ઉપયોગ કરી x ની અંદર જે range આપી છે એને range sathe જ મડાવીને print માં x ** 2 કરાવી દીધું છે હેવ આ example ને શોર્ટ રીતે લખવું હોય તોય રસ્તો છે જે નીચે દર્શાવેલ છે ⬇️ 

squared_num = [x**2 for x in range(10)]
print(squared_num)

cube_num = [y**3 for y in range(10)]
print(cube_num)

# ------------------------*----------------------------------------*---------------


