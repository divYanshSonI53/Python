# Saturday, 13th April

# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True: # આ line માં while loop નો ઉપયોગ કરેલ છે જેમાં statement True આપેલ છે એટલે કે infinite વાર આ loop ફરવી જોય  

    number = int(input("Enter value between 1 and 10: ")) # number input લેવામાં આવ્યું che 

    # if number >= 1 and number <= 10: # આવી રીતે પણ લખી સકીએ 
    if 1 <= number <= 10: # આ line ની માં condition આપી આછે અગર number 1 થી 10 સુધી માં આવે તો જ condition true ગણાશે અને એની નીચેનું statement print કરી break થઈ જશે નકર યો આ loop infinite વાર સુધી ચાલતી જ રહેશે  
        print("Thank you")
        break
    else:
        print("Please enter a number between 1 and 10")