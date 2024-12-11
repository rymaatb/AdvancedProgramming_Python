                #Separating Dinars and Centimes
price = float(input("Please type in a price: "))
Dinars = int(price)
Centimes = round((price - Dinars) * 100)
print(f"Dinars: {Dinars}")
print(f"Centimes: {Centimes}")