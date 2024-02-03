# By Jeffrey Fonseca
# For Comp 182, at CSUN, taught by Prof Freedman
#  

integerlist = input("Give a list of integers, seperated by spaces. The first integer is how long the list should be: ").split(' ')

integerlist.reverse()

integerlist = integerlist[:-1]

for item in integerlist:
    if item != integerlist[-1]:
        print(item, end=',')
    else:
        print(item)

