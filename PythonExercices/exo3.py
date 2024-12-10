
totalAmount = float(input("Total amount: "))
numberItems = int(input("Number of items: "))
dayOfWeek = input("Day of the week: ").strip().capitalize()

while True :
    if dayOfWeek in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
       discount = 0.10  
       break
    elif dayOfWeek in ["Saturday", "Sunday"]:
       discount = 0.20
       break  
    else:
       print("Invalid day of the week entered.")
       dayOfWeek = input("Retype Day of the week: ").strip().capitalize() 

discountedPrice = totalAmount * (1 - discount)

if numberItems > 5:
    discountedPrice *= 0.95

print(f"Total price after discount: {discountedPrice:.1f} dinars")