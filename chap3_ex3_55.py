#sum natural numbers
#ask user for natural numbers

n = int(input("Enter any number: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

print(f"Sum is : {total}")
