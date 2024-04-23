# Friday, 12th April

# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter a number: ")) # આ line ની અંદર range નું input લેવા માં આવ્યું છે કે loop કયા number સુધી ફરશે અને એની અંદર જેટલા પણ even numbers આવતા હશે એ add થઈ ને result  મડી જશે    
sum_even = 0 # આ line ની અંદર નવું variable ફરજીયાત બનાવવું જ પડે કેમ કે એની અંદર loop જેટલી વાર ફરશે એટલી વાર ઈવન numbers add કરાવવા પડે એટલે એની શરૂઆત 0 થી કરી છે 

for even_numbers in range(1, n+1): # આ line માં statement ની અંદર range આપેલ છે જે છે 1 થી લઈ ને n+1 સુધી એટલે કે infinite સુધી એટલે કે range input લીધેલ છે ત્યાં સુધી 

    if even_numbers % 2 == 0: # આ line માં કીધેલ છે કે range જ્યાં સુધી ફરશે એમાં ઈવન numbers કેમ શોધવા તો કે એને 2 sathe divide કરી દ્યો remainder માં અગર 0 આવે તો એ even number કેવાય એટલે કે even number આવશે તો જ નીચે લખેલ code execute થશે 

        sum_even += even_numbers # હવે આ line માં લખેલ છે કે જેટલી વાર even_numbers આવે એટલી વાર એને sum_even સાથે add કરતાં જાઓ એટલે કે પેલી વાર loop ફરશે તો એમાં 1 આવશે એટલે કે આ line execute નઇ થાય પણ બીજી વાર loop ફરશે તો એમાં 2 આવશે એટલે sum_even ની અંદર starting 0 આપેલ છે તો 0+2 થઈ એવી જ રીતે આગડ 2+2, 4+2, 6+2, 8+2, n.....સુધી 

print("Sum of even number is: ", sum_even)