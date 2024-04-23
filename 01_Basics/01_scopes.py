# Tuesday, 16th April

# scopes અથવા તો namespaces

# username = "chaiaurcode"

# def test(){
    # બધી languages ની અંદર normally definition બનાવ્યા પછી curly braces નો upyog થાય જે scopes જ કેવાય પણ python ની અંદર curly braces ના બદલે colon નો ઉપયોગ થાય છે અને જેની અંદર indentation નો ઉપયોગ થતો હોય એટેલ સમજી લેવાનું scope જ છે 
# }

# if true{

# }

# ----------------------*-----------------------------*----------------------------------

username = "chaiaurcode" # Global variable

def func():
    # username = "chaiaurcode2" # આ local variable કેવાય જે definition બનાવેલ છે એની અંદર બનેલું છે અને નીચે print કારવેલું છે જો અગર આ line ને comment કરી દેવામાં આવે તો python શું કરશે કે global variables માં આવી ને username નામ નું જ variable શોધશે અને એની અંદર જે હોય એ print કરાવી દેશે 
    print(username)

print(username)
func()

# -----------------*-----------------------------*----------------------------------

# બીજું example ⬇️ 

x = 99 # આ line માં x નામ નું global variable લીધેલ છે જેમાં value આપેલ છે 99 હવે આ line માં શું સમજવા માંગે છે કે global variable બનાવેલ હોય એનો ઉપયોગ આપડે બધી જગ્યા એ લઈ સકીએ 

# def func2(y):
#     z = x + y # આ line માં x ની value જે upr દર્શાવેલ છે 99 અને ય ની value જે નીચે function call ટાણે parameters માંથી pass થઈ ને આવશે જે છે 1 એટલે કે 99 + 1 = 100 z નામ ના variable માં store થઈ જશે અને નીચે return કરવામાં આવે છે 
#     return z

# result = func2(1)
# print(result)

# -----------------------*---------------------------------------*-------------------

# ત્રીજું example ⬇️ 

# def func3():
#     global x # આ line માં global keyword નો ઉપયોગ કરેલ છે જેના થી આપડે જે globally x નામ નું જે variable દર્શાવેલ છે ઉપર જેની value છે 99 એ આ function ની અંદર global keyword નો ઉપયોગ કરી બદલવામાં આવે છે જે સારી practice ના કેવાય અને બંને ત્યાં સુધી આનો ઉપયોગ ના કરવો જોઈએ  
#     x = 12

# func3()
# print(x)

# ------------------------*------------------------------*---------------------------


# ચોથું example ⬇️

# નીચે દર્શાવેલ example માં function ની અંદર function એટલે કે definition ની અંદર definition બનાવવામાં આવેલ છે જેમાં પેલા function ની અંદર x નામ ના vairable ની 88 મૂકવા માં આવ્યું છે અને બીજા function માં એટલે કે function ની અંદર બીજું function જે છે એમાં x print કરાવેલ છે અને એ તો અપડને ખ્યાલ જ છે x માં globally 99 મુકેલ છે તો સવાલ એ ઉઠે કે print કયું x થશે તો આમાં function ને as a ઘર માની લો અને એની અંદર નું જે function બનાવેલ છે એને ઘર નું room તો હવે થાય છે શું કે function ની અંદર જે બીજું function બનાવવામાં આવેલ છે જેમાં x print કરાવેલ છે એ function ની baar આવશે જોવા માટે એટલે કે room ની બાર આવશે જોવા ઘર માં પછી ત્યાં અગર નો માંડે તો gloabally શોધવા જશે  

def f1():
    x = 88
    def f2():
        print(x)
    # f2() હવે function ની પાછડ આપડે parenthesis લગાડી દઈએ એનો મતલબ એમ હોય છે કે એ ફંકશન execute કરાવવા માંગીએ છીએ
     
    return f2 # આ line માં ખાલી f2 return કરેલ છે એટલે કે આપડે આખે આખું function જ return કરીએ છીએ આ line માં

myResult = f1() # આ line માં f1 ને call કરાવવામાં આવે છે જેની અંદર પેલા તો x declare કરેલ છે જેની અંદર 88 છે એના પછી function ની અંદર જ function માં x print કરાવામાં આવે છે ane f2 return કરવામાં આવે છે એટલે કે આખે આખું function જ return થાય che એના f2 ની પાછડ અગર parenthesis નો ઉપયોગ કરેલ હોત તો function ત્યાં ને ત્યાં execute કરવામાં આવત પણ એના badle myResult માં f1 call કરવામાં આવ્યું છે એટલે આખે આખું function જ મોકલવામાં આવ્યું છે અને નીચે ની line માં myResult ની પાછડ parenthesis લગાડેલ છે એટલે કે execution કરેલ છે 

myResult()

# -----------------*--------------------------*------------------------------

# પાંચમું example ⬇️

# નીચે દર્શાવેલ example માં chaicoder અને actual નામ ની definition ની અંદર definition બનાવવામાં આવેલ છે હવે chaicoder નામ ની definition માં parameters માં function call ટાણે 2 લેવામાં આવ્યું છે જે store થયું છે definition ની બાર f નામ ના variable માં એવી જ રીતે બીજી વાર functional call ટાણે parameters ની અંદર 3 pass કરવામાં આવ્યું છે જે store થયું છે g ની અંદર હવે function call તો થઈ ગયું છે અને એમાં parameters ની અંદર 2 અને 3 pass થઈ ગયા છે એના પછી આખે આખું actual નામ નું function જ return કરવામાં આવેલ છે જેની andar x ** num છે એટલે કે x ** 2 અને એવી જ રીતે g ની અંદર x ** 3 એના પછી jyare f અને g print કરાવવામાં આવે છે tyare એની અંદર parameters માં જે values pass કરવામાં આવશે એ x ની જગ્યા લેશે એટલે કે 3 ** 2 અને એવી જ રીતે g માં 3 ** 3 
 
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3) 

print(f(3))
print(g(3))