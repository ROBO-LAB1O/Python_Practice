from atm import ATM

machine = ATM(10000, 9999)

while True:
    print("\n1. Check balance\n2. Withdraw\n3.Deposit\n4. Change Pin\n5. Exit")
    choice=int(input("Enter your choice: "))

    if choice ==5:
        print("Thankyou for coming to our bank!")
        break
    try:
        pin=int(input("ENter you pin: "))

        if choice==1:
            machine.check(pin)
        elif choice==2:
            amount=int(input("Enter you amount: "))
            machine.withdraw(pin,amount)
        elif choice==3:
            amount=int(input("Enter you amount: "))
            machine.deposit(pin,amount)
        elif choice==4:
            newpin=int(input("Entyer pin"))
            machine.changepin(pin, newpin)
        else:
            print("Invalid")
    except ValueError:
        print("please enter no. only")