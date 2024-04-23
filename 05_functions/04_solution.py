# Saturday, 13th April

# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# મારી રીત ⬇️ 

# def area_and_circumference():
#     # Get the radius from the user
#     radius = float(input("Enter the radius of the circle: "))

#     # Calculate the area and circumference
#     area = 3.14 * radius ** 2
#     circumference = 2 * 3.14 * radius

#     # Return the area and circumference
#     return area, circumference


# # Call the function
# area, circumference = area_and_circumference()

# # Print the results
# print("Area:", area)
# print("Circumference:", circumference)

# hitesh choudhary ની રીત ⬇️

# આ example માં math import કરાવેલ છે જેમાં થી આપડે pi ની value direct math.pi લખીને લઈ આવી સકીએ પણ આની જરૂર નોહતી આ example માં 
 
import math

def area_circumference(radius):
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area, 3), round(circumference, 3) # આ line માં round method નો ઉપયોગ કરેલ છે જેના થી decimal point પછી ની values વધારે હશે તો round off થઈ ને આવી જશે જેમ કે round off માં value આપેલ છે 3 તો ડેસિમલ પછી 3 જ value આવશે result માં 

a, c = (area_circumference(3))

print(f"Area: {a} Circumference: {c}")

