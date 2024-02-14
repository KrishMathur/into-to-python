'''this takes the length and width of the rectangle and finds the area'''


#by krish mathur
#Wed Feb 7, 2023

import math 
from time import sleep

while True:
    try:
        h = float(input("Enter height of rectangle:"))
        

        if h <= 0:
            print("please only put numbers above 0")
            sleep(1)
            continue 
        break 
    except ValueError:
        print("Please only put numbers")
    
    

while True:
    try:
        l = float(input("Enter the length of the rectangle:"))
        

        if l <= 0:
            print ("please only put numbers above 0 ")
            sleep(1)
            continue 
        break 
    except ValueError:
        print("Please only put numbers")

area = l * h 

print (f"the area is = {area}^2 cm")



        