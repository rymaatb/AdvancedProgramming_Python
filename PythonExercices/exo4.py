agePerson1 = -1
while True:
    if agePerson1<0:
           agePerson1 = int(input("please type in the age of the first person: "))
           print("Age should be positif!")
    else:
       agePerson2 = int(input("please type in the age of the second person: "))
       if agePerson2<0:
           print("Age should be positif!")
       else:
             break
if agePerson1 == agePerson2:
        print("Both people are the same age!")
elif agePerson1 > agePerson2 :
        print(f"The older age is: {agePerson1}")
else:
        print(f"The older age is: {agePerson2}")
