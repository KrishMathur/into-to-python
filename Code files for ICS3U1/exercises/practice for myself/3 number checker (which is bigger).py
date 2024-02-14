''' this code takes three numbers and gives back the biggest number'''





import math 

while True:
    try:
        num1 = float(input("Put in first number here: "))
        break 
        
    except ValueError:
        print("please put in actual number")

while True:
    try:
        num2 = float(input("put in second number here: "))
        break
    except ValueError:
        print ("please put in actual number")

while True:
    try:
        num3 = float(input("put in third number here: "))
        break 
    except ValueError:
        print ("put in actual number")



#all nums are same 
if num1 == num2 and num2 == num3:
    print ("all numbers are the same.", num3)


# establish if 2 ums are the same 
    
if num1 == num2 and num1 > num3:
    print (f"both the first and second number are the same being and the biggest {num1}")

if num1 == num3 and num1 > num2:
    print (f"both the first and third number are the same being and the biggest {num1}")

if num2 == num3 and num3 > num1:
    print(f"both the second and the third number are the same and the biggest being {num3}")

# establish print is all num are diffrent 
if num1 > num2 and num1 > num3:
    print(f"{num1} is the biggest number")

if num2 > num1 and num2 > num3:
    print(f"{num2} is the biggest number")

if num3 > num1 and num3 > num2:
    print (f"{num3} is the biggest number")

