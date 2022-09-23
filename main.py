print("welcome to calculator")
A = input("enter the first number")
while A.isdigit() == False :
    print("please enter an integer")
    A = input("enter the first number")
print("Please select the mathmatical operation you want to make")
print(" 1  for addition \n 2 for substraction \n 3 for multiplication \n 4 for dividing \n 5 for giving the power \n 6 the get the muduluos of dividing")

O = input("enter the number of the operation")


while O.isdigit() == False:
    print('please enter an integer')
    O = input("enter the number or sign of the operation")

val = O

if int(val)  == 1:
    print("you are adding",A,"with B")
    B = input("enter the other number B")
    while B.isdigit() != True:
        print("B is not a digit,please enter an integer")
        B = input("enter the integer B")
    res = int(A) + float(B)
    print(res)

if int(val) == 2:
    print("you are substractig", A, "from B")
    B = input("enter the other number B")
    while B.isdigit() != True:
        print("B is not a digit,please enter an integer")
        B = input("enter the integer B")
    res = int(A) - float(B)
    print(res)

elif int(val) == 3 :
    print("you are mutiplipying", A, "with B")
    B = input("enter the other number B")
    while B.isdigit() != True:
        print("B is not a digit,please enter an integer")
        B = input("enter the integer B")
    res = int(A) * float(B)
    print(res)

elif int(val) == 4 :
    print("you are dividing", A, "from B")
    B = input("enter the other number B")
    while B.isdigit() != True:
        print("B is not a digit,please enter an integer")
        B = input("enter the integer B")
    res = int(A) / float(B)
    print(res)

elif int(val) == 5:
    print("you are raising", A, "to the power B")
    B = input("enter the other number B")
    while B.isdigit() != True:
        print("B is not a digit,please enter an integer")
        B = input("enter the integer B")
    res = int(A) ** float(B)
    print(res)

elif int(val) == 6 :
    print("you are moduling", A, "from B")
    B = input("enter the other number B")
    while B.isdigit() != True:
        print("B is not a digit,please enter an integer")
        B = input("enter the integer B")
    res = int(A) % float(B)
    print(res)

