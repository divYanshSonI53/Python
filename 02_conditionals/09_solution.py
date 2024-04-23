# Friday, 12th April

# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0): # આ example માં ખૂબ જ સારી રીતે સમજાવેલ છે and અને or logical operator 
    print(year, "is a leap year.")

else:
    print(year, "isn't a leap year.")