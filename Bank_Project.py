print("INDIAN BANK")
chances=3
balance = 50.13
restart="Y"
while chances >=0:
    pin=int(input("Enter the pin number"))
    if(pin==(1234)):
        print("You entered pin correctly")
        print("Enter option 1 for Balance Enquiry")
        print("Enter option 2 for Withdrawl")
        print("Enter option 3 for Deposit")
        print("Enter option 4 for Cancel")
        option=int(input("Enter your option"))
        if option ==1:
            print("Balance Enquiry :",balance)
            restart=input("You would like to go back: Y/N")
            if restart in ("No","N","NO","n"):
                print("Thank you")
                break
        elif option ==2:
            print("Withdrawl : $20 / $40 / $60 / $80 / $100")
            withdraw=int(input("Enter amount to withdraw"))
            if withdraw in [20,40,60,80]:
                Total=balance-withdraw
                print("Remaining Balance : ",Total)
            elif withdraw!=[20,40,60,80,100]:
                print("Enter a valid amount try again : Y/N" )
