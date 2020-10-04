name = input("Enter your full name: ")
name = name.lower()
#output

# h : 0
# a : 1
# m : 2
# z : 3
# a : 4



tem_var = ""
i = 0

while i < len(name):
    if name[i] not in tem_var:
        tem_var = name[i] + tem_var
        print (f"{name[i]} : {name.count(name[i])} ")
    i = i +1
    


