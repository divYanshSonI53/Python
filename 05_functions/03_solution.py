# Saturday, 13th April

# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# Polymorphism નો મતલબ એ છે કે operators કેવી રીતે string અને numbers ને એની મેડે handle કરી લ્યે એને polymorphism કેવાય 

# મારી solve કરવાની રીત ⬇️ 

# def multiply():
#     a = int(input("Provide any number: "))
#     b = int(input("Provide any number: "))
#     return a * b

# while True:
#     print(multiply())

# hitesh choudhary ની rit ⬇️ 

def multiply(p1, p2):
    return p1 * p2

print(multiply(8, 5))
print(multiply('a', 5))
print(multiply(8, 'a'))
