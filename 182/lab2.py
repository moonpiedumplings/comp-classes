# Lab 2 of comp 182



# DigitCount: How many digits in an integer:

digitInput = input("Enter an integer: ")
digit = int(digitInput)
count = 1



# Use recursion to count how many digits are in a thing.

def digitLength():
    global digit
    global count
    if digit < 10:
        # A return would be better here
        print(count)
        exit()
    digit = digit / 10
    count = count + 1
    digitLength()
    


digitLength()