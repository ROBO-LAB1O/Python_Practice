#atm def

class ATM:
    count=0
    def __init__(self,balance,pin):   #_ClassName__attributename.
        self.__balance=balance  #mangling
        self.__pin=pin
        self.__count=0
        self.__locked=False
    def __Verify(self,pin):
        if self.__locked:
            print("Your account is locked!")
            return False
        if pin==self.__pin:
            self.__count=0
            return True
        self.__count+=1
        if self.__count>=3:
            self.__locked=True
            print("Your account is locked!")
        else:
            print(f"Incorrect pin")
        return False
    def check(self,pin):
        if self.__Verify(pin):
            print(f"Your balance is: {self.__balance}")
            return self.__balance

    def withdraw(self,pin,amount):
        if self.__Verify(pin):
            if amount>self.__balance:
                print("INsufficient balance")
            elif amount<=0:
                print("Invalid amount")
            else:
                self.__balance-=amount
                print(f"your balance is : {self.__balance}")
                return self.__balance
    def deposit(self,pin,amount):
        if self.__Verify(pin):
            if amount>0:
                self.__balance+=amount
                print(f"Your balance is : {self.__balance}")
                return self.__balance
            elif amount<=0:
                print("Invalid amount")

    def changepin(self,pin,newpin):
        if self.__Verify(pin):
            if len(str(newpin))==4:
               self.__pin=newpin
               print("Pin changed successfully!")
        else:
            print("Incorrect pin!")

