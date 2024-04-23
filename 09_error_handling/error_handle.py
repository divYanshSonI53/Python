# Friday, 19th April

# નીચે example માં file open કરાવવાની 3  રીત દર્શાવેલ છે write mode માં  


file = open('youtube.txt', 'w')

# ------------------------------*-------------------------*---------------------

try:
    file.write('chai aur code')
finally:
    file.close()

#----------------*-----------------------------*--------------------------------


with open('youtube.txt', 'w') as file:
    file.write('chai aur python')