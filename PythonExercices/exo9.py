                        #Name Length Kingdom
Cities = []
while True :
    City = input("Please type in a city (or 'stop' if u wanna stop): ")
    if City.lower() == "stop":
        break
    else:
        length = len(City)
        Population = length * 1000000
        Cities.append((City,Population))
print("The cities and their populations in order :")
Cities.sort(key=lambda x: x[1] , reverse=True)
for City,Population in Cities:
    print(f"{City} : {Population} persons")