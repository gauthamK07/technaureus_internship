class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transaction=[]
    
    def widraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            self.transaction.append(amount)
            print("widrawal successful")
    def deposit(self,amount):
        self.balance+=amount
        self.transaction.append(amount)
        print("deposit successful")

    def transfer(self,amount,target):
        if amount<self.balance:
            self.widraw(amount)
            target.deposit(amount)
            print("transfered successfully")
        else:
            print("insufficient balance")
        
    def status(self):
        print("name :",self.name)
        print("balance :",self.balance)
        print("transaction :",self.transaction)


a1 = BankAccount("Rahul", 5000)

a2 = BankAccount("Arjun", 3000)

a1.deposit(1000)

a1.widraw(500)

a1.transfer(2000,a2)

a1.status()


print()

a2.status()


        
    
        

        