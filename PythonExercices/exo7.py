                     #Leap Year 
Year = int(input("Please type in a year: "))
if (Year%4==0 and Year%100!=0) or (Year%100==0 and Year%400==0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year")