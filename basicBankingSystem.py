class MyBank:
    maxWithdraw = 20000
    minWithdraw = 500

    def __init__(self, amount) -> None:
        if amount >= self.minWithdraw and amount <= self.maxWithdraw:
            self.amount = amount
        else:
            self.amount = 0
            print("Invalid amount!(Accepting between 500-20000 only)")

    def amountCheck(self):
        return self.amount
    
    def deposit(self, amount):
        if amount >= self.minWithdraw and amount <= self.maxWithdraw:
            self.amount += amount
        else:
            print("Invalid amount!(Accepting between 500-20000 only)")

    def withdraw(self, amount):
        if self.amount < amount:
            print("Amount not available in your account!")
        elif amount >= self.minWithdraw and amount <= self.maxWithdraw:
            self.amount -= amount
        else:
            print("Invalid amount!(Accepting between 500-20000 only)")

myAcc = MyBank(int(input("Enter your initial amount : ")))
while(1):
    print("\nYour transection will be accepted between 500-20000!\n1 : Deposit\n2 : Withdraw\n3 :Check Balance\n0 : Exit\n")
    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        amount = int(input("Enter your amount : "))
        myAcc.deposit(amount)
    elif choice == 2:
        amount = int(input("Enter your amount : "))
        myAcc.withdraw(amount)
    elif choice == 3:
        print("Your balance is : ", myAcc.amountCheck())
    elif choice == 0:
        break
    else:
        print("Wrong choice!")