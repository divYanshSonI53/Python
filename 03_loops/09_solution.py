# Saturday, 13th April

# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

# મારી રીત ⬇️ 

items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) > 1:
        print(f"Duplicate found: {item}")
        break


# hitesh chaudhary ની રીત ⬇️ 

items = ["apple", "banana", "orange", "apple", "mango", "banana"] # આ line માં items નામ ની list આપેલ છે 

unique_item = set() # આ line માં unique_item નામ નું set() બનાવેલ છે જેમાં items નામ ની list માંથી એક એક કરી ને values add થશે કેમ કે નીચે loop માં દર્શાવેલ છે 

for item in items: # item નામ ના variable માં items list માંથી એક એક કરી ને values આવશે  
    if item in unique_item: # આ line માં લખેલ છે કે અગર unique_item set()ની અંદર એક જેવી જ items આવશે તો નીચે આપેલ statement print થઈ loop break થઈ jashe 

        print(f"Duplicate found: {item}")
        break

    unique_item.add(item) # add method નો ઉપયોગ કરેલ છે એટલે આ line માં થશે શું કે unique_item ની અંદર item માંથી એક એક કરી ને values add થઈ જશે 

