# Thursday 11th, April

# dictionary

# List અને dictionary માં શું ફેર છે કે લિસ્ટ પ આપડે ઇન્ડએક્સિનગ through બધુંય કરીએ પણ dictionary માં આપડે ગમે એ value લખીએ છીએ તો એની એક specific કે આપીએ છીએ જેનો એક્જામ્પલ નીચે દર્શાવેલ છે  ⬇️


chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"} # જે કોઈ પણ વેલ્યુ લખવી હોય એની પેલા એની key આપવી પડે 
print(chai_types)

print(chai_types["Masala"])
print(chai_types["Ginger"])
# print(chai_types["gingery"]) આ statement માં error આવશે કેમ કે આ નામ ની key આપડે નોંધાવી જ નથી dictionary માં 

print(chai_types)

# જેમ આપડે list ની અંદર indexing નો ઉપયોગ કરી list માં values બદલાવીએ છીએ એવી જ રીતે dictionary ની અંદર keys નો ઉપયોગ કરી dictionary ની અંદર values બદલવી સકીએ ⬇️  

chai_types["Green"] = "Fresh" 
print(chai_types)

print(chai_types)

for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai, chai_types[chai]) # આ example માં chai જે variable છે એમ for loop નો ઉપયોગ કરી chai_types ની અંદર જે keys છે પેલા તો એ fetch કરવામા આવે છે એના પછી chai_type[chai] એટલે કે એની value 

# for loop ની અંદર આપડે directly 2-2 variable લઈ અકીએ એનો example નીચે દર્શાવેલ છે ⬇️ 

for key, values in chai_types.items():
    print(key, values)

if "Masala" in chai_types:
    print("I have Masala Chai")

print(len(chai_types)) # આનો જવાબ આવશે 3 કેમ કે dictionary ની અંદર keys ને item બંને આપીએ છે આપડે એનો મતલબ એ નથી કે બંને ગણાશે, ગણાશે તો એની valueજ જે છે 3 

# dictionary ની અંદર add કરાવવા માટે નીચે દર્શાવેલ method નો યપયોગ થાય છે ⬇️ 

chai_types["Earl Grey"] = "Citruos"
print(chai_types) # આ method નો ઉપયોગ કરી છેલે થી add થઈ જશે 

# pop method in dictionary ⬇️ 

chai_types.pop("Ginger")
print(chai_types) # હવે dictionary માં indexing ના હોય એટલે આમાં parameters pass કરવા જ પડે કે ડિક્શનરી માંથી શું હટાવવું છે એટલે કે જે હટાવવું છે એની key 

# popitem method in dictionary ⬇️ 

chai_types.popitem()
print(chai_types) # આ method માં parameters પાસ કરવાની જરૂર ના પડે આ મેથડ છેલે થી item ઉડાડી દીએ એટલે હવે આપડી પાસે dictionary માં 2 જ item રીએ 

# delete method ⬇️ 

# python ની અંદર આ delete method નો લઘભગ બધી જ જગ્યા એ ઉપયોગ કરવામાં આવે છે જેમ કે લિસ્ટ ની અંદર dictionary ની અંદર 

del chai_types["Masala"]
print(chai_types)

# clear method ⬇️ 

chai_types.clear()
print(chai_types)

# copy method  ⬇️

chai_types_copy = chai_types.copy() # આ example માં સમજાવ્યું છે કે copy method use કરવાથી memory માં એક નવું reference બને છે chai_types નું નકર તો copy method નો ઉપયોગ ના કરેલ હોય અને એની જગ્યા એ direct chai_types લખેલું હોત તો direct chai_types dictionary નું જ reference બનતું memory માં 


# update method ⬇️

chai_types_copy.update({"Ginger": "Hot"})
print(chai_types_copy)

# nested dictionary's example ⬇️ 

tea_shop = {

    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "tea": {"Green": "Mild", "Black": "Strong"}

}

print(tea_shop)

print(tea_shop["chai"]) # dictionary ની અંદર dictionary ને કેવી રીતે access કરવું

print(tea_shop["chai"]["Ginger"]) # dictionary ની અંદર dictionary ને કેવી રીતે access કરવું 

# sqaured and cubed number example⬇️ 

squared_num = {x:x**2 for x in range(10)}
print(squared_num) # આ example માં squared_num ની અંદર પેલા તો x: declare કર્યું છે પછી કીધું છે કે x સાથે કરાવવું શું છે તો કે x**2 પછી for loop નો ઉપયોગ કરેલ છે એમાં જે x variable declare કરેલું છે પેલા આપડે અને range declare કરી છે જેમાં આપડે કીધેલું છે 1 થી 10 સુધી 

cube_num = {x:x**3 for x in range(10)}
print(cube_num)

# ફરી પાછું clear method નું example ⬇️ 

squared_num.clear()
print(squared_num)

# નીચે દર્શાવેલ example મા સમજાવ્યું છે કે 2 list આપડને ને આપેલ હોય તો એને dictionary માં કેમ convert કરવી  fromkeys method ની મદદ થી 

# fromkeys method ⬇️ 

keys = ["Masala", "Ginger", "Lemon"]
print(keys) # આ example માં keys નામ નું variable બનાવ્યું છે અને એની અંદર 0 indexing ઉપર Masala છે 1 indexing ઉપર Ginger છે અને 2 indexing ઉપર Lemon છે  

default_value = "Delicious" # આ છે બીજી list જેમાં variable નું નામ છે default_value જેની અંદર value Delicious છે અને એ value dictionary જે બનસે એમ values ની જગ્યા લેશે 

new_dict = dict.fromkeys(keys, default_value) # આ example માં દર્શાવેલ છે કે keys ની અંદર જ કોઈ પણ values હોય એને as a dictionary ની keys ની જેમ use કરવામા આવેલ છે અને default_value ની અંદર જે કોઈ પણ values હોય એ as a dictionary ની value ની જેમ યુઝ કરવામા આવે છે  
print(new_dict)

new_dict = dict.fromkeys(keys, keys)
print(new_dict)

# -----------------------*--------------------------------*-------------------------------