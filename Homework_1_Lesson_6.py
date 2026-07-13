#Star

print("Hi, welcome to the Grade Checker!\n")

your_grade = int(input("What is your grade? "))

if 0 <= your_grade <= 100:
    print(f'{your_grade} is valid grade!')
else:
    print(f'{your_grade} is illegal grade :(')

#Stop