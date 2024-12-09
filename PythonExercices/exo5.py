print("Runner 1: ")
name1 = input("Name: ")
time1 = float(input("Time (in seconds): "))
print("Runner 2: ")
name2 = input("Name: ")
time2 = float(input("Time (in seconds): "))
if name1 != name2:
    if time1==time2:
        print(f"{name1} and {name2} have the same time")
    elif time1<time2:
        print(f"The faster runner is {name1}")
    else:
        print(f"The faster runner is {name2}")
else:
    if time1==time2:
        print(f"{name1} the first runner and {name2} the second runner have the same time")
    elif time1<time2:
        print(f"The faster runner is {name1} the first runner")
    else:
        print(f"The faster runner is {name2} the second")