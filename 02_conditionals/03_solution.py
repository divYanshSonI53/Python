# Friday, 12th April

score = input("Provide Score: ")
score_int = int(score)

if score_int >= 101:
    print("Please verify your grade again")
    exit() # આ program માં exit() function નો ઉપયોગ કરેલ છે જેના ઉપયોગ થી અગર if condition માન્ય ગણાશે તો program માંથી નિકડી જવાશે 

if score_int >= 90:
    grade = "A"
elif score_int >= 80:
    grade = "B"
elif score_int >= 70:
    grade = "C"
elif score_int >= 60:
    grade = "D"
else:
    grade = "F" 

print("Your grade is:",grade)