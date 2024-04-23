# Saturday, 13th April

# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

# def add(a, b):
#     return a + b

# result = add(1, 2)

# નીચે દર્શાવેલ example માં lambda નો ઉપયોગ કરવામાં આવેલ છે lambda એટલે કે વગર બન ની નાની definition જેને આપડે વધારે વાર ઉપયોગ માં નથી લેવાના અને lambda નું કઈ નામ તો હોય નઇ એટલે એને variable ની અંદર store કરવામાં આવે અને એક જ line ની અંદર લખવામાં આવે છે 

cube = lambda x, y: (x ** 3, y ** 2)
print(cube(3, 2))