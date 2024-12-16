from math import sqrt
while True :
    number = int (input("Please enter a number: "))
    if number == 0 :
        break
    elif number>0:
        print(f"The sqrt of ur number is : {sqrt(number)}")
    else:
        print("Invalid number")
