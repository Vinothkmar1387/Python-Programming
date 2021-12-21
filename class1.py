# a = input("Enter the first number")
# b = input("Enter the second number")
# c = a+b
# print(c)

# # if and ifelse program
# a=11
# if a < 10:
#     print("a is lesser than 10")
# else:
#     print("a is greater than 10")

# Getting numbers and storing in another variable then using if else condition
# a = int (input("Enter the first value"))
# b = int (input("Enter the second value"))
# c=a+b
# print(c)
# if c < 10:
#     print("The result of C is lesser than 10 ")
# elif c > 10:
#     print("The result of C is greater than 10")
# else:
#     print("The result of C is equal to 10")
# largest of three numbers
# leap year
# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))
# c = int(input("Enter the third number"))
# if a>b and a>c :
#     print("a is greater")
# elif b>a and b>c:
#     print("B is greater")
# else:
#     print("C is greater")


# Find leap year
# a = 2000
# if (a % 4 == 0):
#     if (a % 100 == 0):
#         if (a % 400 == 0):
#             print(a,"is leap year")
#         else:
#             print(a,"is not leap year")
#     else:
#         print(a,"is not leap year")
# else:
#     print(a,"is not leap year")
a = 2000
if a % 4 == 0 and a % 100 == 0 or a % 400 == 0:
    print(a,"is leap year")
else:
    print(a,"is not leap year")


