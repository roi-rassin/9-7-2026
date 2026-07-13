#Star

print("Hi, welcome to the Number Checker!\n")

your_number = int(input("Enter a two-digit number: "))

if 10 <= your_number <= 99:
    tens = your_number // 10
    ones = your_number % 10
    if tens == ones:
        print("Tens equal to ones!")
    else:
        print("Tens not equal to ones :(")
else:
    print("Number should be between 10 - 99!")

#Stop