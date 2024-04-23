# Friday, 12th April

# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_numbers_count = 0 # આ line માં positive_numbers_count નું variable banavvu અને એની અંદર 0 value દેવી જરૂરી હતી કેમ કે loop ની અંદર positive values નું count જાણવા માટે variable પેલે થી ખાલી હોવું જરૂરી હોય  

for number in numbers: # આ લઈને ની અંદર numbers નામ ના variable ની list ની અંદર થી values fetch કરવામાં આવે છે એક એક કરી ને 

    if number > 0: # આ line ની અંદર if statement નો ઉપયોગ કરી condition આપવા માં આવે છે કે values જેટલી પણ આવે છે numbers નામ ના variable list ની અંદર થી એક એક કરી ને એને 0 સાથે compare કરો અગર 0 થી મોટું હોય તો નીચેના સ્ટેટમેંટ માં લખ્યું છે કે 1 add કરી દો અને અગર value 0 થી નાની આવે તો કઈ પણ કરવાનું કીધેલ નથી  

        # નીચે આપેલ બંને statement એક જ કામ કરે છે બંને રીત માન્ય છે ⬇️ 

        # positive_numbers_count = positive_numbers_count + 1

        positive_numbers_count += 1
    
print("Final count of positive number is:", positive_numbers_count)