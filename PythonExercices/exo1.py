ticketCost = 15.50
name = input ("Please enter your name: ")
if name == 'VIP':
    print("Enjoy the show for free!")
else:
    while True:
        numberTickets = int(input("How many tickets would you like to buy? "))
        if numberTickets<=0:
            print("The number of tickets should be 1 or more")
        else:
            break
    print(f"The total cost is {ticketCost*numberTickets}")
    print("Enjoy your tickets!")
