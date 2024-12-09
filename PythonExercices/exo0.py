nubmerPeople = int(input("How many people need a ride ? "))
nubmerPlaces = int(input("How many people fit in one taxi ? "))
while (nubmerPeople < 0 or nubmerPlaces <= 0   ):
    if nubmerPeople<0 :
      print ("Number of people should be positif!")
      nubmerPeople = int(input("How many people need a ride ? "))
    if nubmerPlaces<=0 :
      print("Number of places should be at least 1 !")
      nubmerPlaces = int(input("How many people fit in one taxi ? "))
if nubmerPeople == 0:
   NumberTaxiNeeded = 0
elif nubmerPeople <= nubmerPlaces:
    NumberTaxiNeeded = 1
elif nubmerPeople % nubmerPlaces > 0:
    NumberTaxiNeeded = nubmerPeople//nubmerPlaces +1
else: 
    NumberTaxiNeeded = nubmerPeople//nubmerPlaces
print (f"Number of taxis needed: {NumberTaxiNeeded}")