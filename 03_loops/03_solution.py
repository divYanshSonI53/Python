# Friday, 12th April

# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter any Number: ")) #આ line માં input લેવામાં આવ્યું છે જે store થશે number variable ની અંદર 

for into in range(1, 11): # આ line માં નવું variable બનાવ્યું છે into નામ નું જેની અંદર range માંથી (1-10) સુધી ની values એક પછી એક આવતી રેશે 

    print(number, 'x', into, '=', number * into) # આ line માં multiplication table print કરાવવાની રીત લખેલ છે 

# નીચે દર્શાવેલ example માં 5th iteration loop ને skip કરીને result આવશે જેના માટે continue keyword નો ઉપયોગ કરવો પડે  

number = int(input("Enter any Number: "))

for into in range(1, 11):
    if into == 5:
        continue
    print(number, 'x', into, '=', number * into)