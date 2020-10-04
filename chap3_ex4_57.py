
name = input("Enter a number containing more then one digit: ")
#exmlpe 1234 input

i = 0
total = 0

while i < len(name):
    total = int(name[i]) + total #1 ,3 , 6, 10
    i = i + 1

print(total)