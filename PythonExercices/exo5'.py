# exo 5 modifie not finished yet
runners ={}
numberRunners = 2
i = 1
while i <= numberRunners:
    print(f"Runner {i}: ")
    runners["name"] = input("Name: ")
    runners["time"] = float(input("Time (in seconds): "))
    i = i + 1
fasterRunTime = runners[0]["time"]
i==1
while i < numberRunners:
    if fasterRunTime < runners[i]["time"]:
        fasterRunTime = runners[i]["time"]
        k = i
    i = i+1
print (f"The faster runner is {runners[k]["time"]}")   
    
       
