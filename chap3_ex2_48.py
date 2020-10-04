#Exercise Watch COCO
print("****Watch COCO Movie****")


name = input("Enter Your Name: ")
user_name = name.lower()

age = int(input("Enter Your Age: "))

if user_name.startswith("a") and age > 10:
    print("You can watch COCO Movie")

# #another way to print if statement
# if (user_name[0]=='a' or user_name[0]=='A')  and age > 10:
#     print("You can watch COCO Movie")

else:
    print("Sorry You connot watch COCO")
