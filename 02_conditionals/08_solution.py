# Friday, 12th April

password = input("Enter Password: ").strip().lower()

if len(password) < 6: # len() is a function that returns the length of a string
    strength = "Weak"
elif len(password) <= 10: # <= is a comparison operator that checks if the length of the password is less than or equal to 10
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is:", strength)