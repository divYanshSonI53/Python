# Tuesday, 16th April

# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.

# નીચે દર્શાવેલ example માં even_generator નામ ની definition બનાવવા માં આવેલ છે અને એના parameters ની અંદર limit નામ નું variable બનાવવા માં આવેલ છે જેમાં definition call ટાણે parameters માં values pass કરવામાં આવશે 

# def even_generator(limit):

#     for i in range(2, limit+1, 2): # range માં આપડે parameters માં 3 arguments આપી સકીએ જેમ કે start,stop અને step. start etle કે range ક્યાંથી ચાલુ કરવી છે, stop એટલે કે કયા ઊભી રખાવવી છે અને step એટલે કે range જે આપેલ છે એના છેલા argument માં 2 આપેલ છે એટલે કે 1 છોડીને 1 value આપશે 

#         # print(i) # હવે વાંધો કયા આવે ઘણી વાર આપડે values direct print ના કરાવવી હોય અને એના બદલે આપડે ગમે એ variable ની અંદર store કરાવવી હોય એટલે એના માટે આપડે values return કરાવવી પડે પણ એના પછી પણ વાંધો કયા આવે કે નીચે print કરાવવા ટાણે આપડે parameters ની અંદર value pass કરી દઈએ તો પણ loop એક જ વાર ફરીને બંધ થઈ જશે એટલે એનો જવાબ આવશે ખાલી 2 જ તો એના માટે બીજું શું કરી સકીએ એના examples નીચે દર્શાવેલ છે ⬇️ 
         
#         return i  

# print(even_generator(10))

# આપડે બીજું શું કરી સકીએ એનો example નીચે દર્શાવેલ છે ⬇️

# હવે નીચે દર્શાવેલ example માં list નો ઉપયોગ કરી problem solve કરવામાં આવેલ છે જેનો જવાબ આપડને list માં જ મડસે પણ જવાબ અગર list માં ના જોતું હોય તો શું કરવું જેનો example આ example ની નીચે દર્શાવેલ છે 

# def even_generator(limit):
#     li = [] # આ example માં empty list લેવામાં આવેલ છે જેમાં range જે આપેલ છે એમાંથી i ની અંદર જે values છે એ li નામ ની list માં add થઈ જશે 

#     for i in range(2, limit +1, 2):
#         li.append(i)
#     return li

# print(even_generator(10))

# હવે actual માં શું કરવું એનું example નીચે દર્શાવેલ છે ⬇️ 

def even_generator(limit):
    for i in range(2, limit +1, 2):
        print(i) 
        yield i # આ example માં yield keyword નો ઉપયોગ કરવામાં આવેલ છે જે પણ values return જ કરે function call ટાણે પણ અનુ કામ છે જેમ કે આ example માં definition ની andar for loop નો upyog કરેલ છે જેમાં કીધેલ છે કે definition call ટાણે parameters માં જે limit આવેલ છે એને 2 થી લઈ ને limit + 1 સુધી ચલાવો અને એમ 2 skip કરતાં જાઓ તો yield keyword જે છે એ આ example માં loop ને જય સુધી ફરવાનું કીધેલ છે એ ફરી જાય પછી એને એજ state માં values ને જાડવી રાખે છે ટુંક માં બધુંય કામ થઈ ગયા પછી values return કરે નકર તો એના બદલે return keyword નો ઉપયોગ કરેલ હોત તો loop ફરે એમ પેલી જે વેલ્યુ આવે એ જ return કરી દીએ  


# print(even_generator(10)) # હવે આપડે definiton ના parameter માં direct value ના આપી સકીએ કેમ કે values variable ની અંદર store કરાવવાની છે એક પછી એક  

for num in even_generator(10): # હવે આ line માં for loop નો ઉપયોગ કરી even_generator નામ ના definition માં parameter માં pass કરેલ છે 10 એ 10 ઉપર definition માં જાય છે એની નીચે loop ને જે કામ દર્શાવેલ છે એ કામ પૂરું કરી 1 વાર loop નીચે num નામ ના variable માં store થાય છે એક પછી એક ટુંક માં બંને loop ફરે છે પેલા નીચે વાડી loop ફરે છે પછી ઉપર વાડી તો સવાલ એ ઉઠે કે even_generator ની અંદર parameters માં 10 pass કરેલ છે તો તો જેટલી વાર loop ફરે એટલી vaar 10 જ જાય ને ઉપર તો કે હ 10 જ જાય છે ઉપર જેટલી વાર loop ફરે છે એટલી વાર પણ ઉપર જે loop એક વાર ફરી ગયા પછી yield નો ઉપયોગ કરેલ છે જે loop જે ફરી ગઈ છે એક વાર એને યાદ રાખે છે એટલે બીજી વાર loop ફરવા જાય એની પેલા એને યાદ હોય કે loop already એક વાર ફરી ગઈ છે જેનો જવાબ હતો 2 એ યાદ રાખી લ્યે એના પછી બીજી વાર ફરે એટલે 4 આવે તો એને પણ યાદ રાખી લ્યે પેલા પછી જ ફરે  

    print(num)
