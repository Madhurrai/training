class Bank():
    def __init__(self,bname,address,ifsc):
        self.bname = bname
        self.address = address
        self.ifsc = ifsc

class BankAccount():

    def __init__(self):
        pass

    def create_acc(self,accType,name,balance,pin,interestrate):
        self._pin = pin
        self._accNo = 999
        self._accType = accType
        self._name = name
        self._interest = interestrate
        if self._accType == "SA":
            if balance>=5000:
                self._balance = balance
            else:
                print("less balance to start the account")
                self._accType = None
                self._name = None
        elif self._accType == "ODA":
            self._eStatement = list()
            self._eStatement.append(balance)
            self._balance = balance
        else:
            self._balance = balance

    def withdraw(self,amt):
        if self._accType == "SA":
            if self._balance-amt>=5000:
                self._balance = self._balance-amt
            else:
                print(f'Not able to withdraw {amt}')
        elif self._accType == "ODA":
            maximum_bal = max(self._eStatement)
            limit = self._balance+maximum_bal*0.1
            if  limit-amt>=0:
                    print("Limit:",limit)
                    print("state",self._eStatement)
                    odFee = 0
                    if self._balance-amt<0:
                        odFee = (self._balance-amt)*0.01
                        print(f'odFee:{odFee}')
                    self._balance = self._balance - amt + odFee
            else:
                print("The witdraw amount is off Limit")
        else:
            if self._balance - amt>=0:
                self._balance = self._balance - amt
            else:
                print(f'Low Balance')



    def deposit(self,amt):
        self._balance = self._balance + amt
        if self._accType=="ODA":
            self._eStatement.append(self._balance)
   

    def creditInterest(self):
        if self._accType == "SA":
            self._balance = self._balance + self._balance*self._interest/100
        elif self._accType == "ODA":
            if self._balance > 0:
                self._balance = self._balance + self._balance*self._interest/100
        else:
            print("No Interest on Current Account")

class atm(Bank,BankAccount):
    def __init__(self, bname, address, ifsc):
        Bank.__init__(self,bname, address, ifsc)
        BankAccount.__init__(self)

    def create(self,accType,name,balance,pin,interestrate):
        super().create_acc(accType,name,balance,pin,interestrate)

    def withdraw(self, amt):
        return super().withdraw(amt)   
    def deposit(self, amt):
        return super().deposit(amt)  

    def creditInterest(self):
        return super().creditInterest()

    def info(self):
        print("*"*100)
        print(f'ACCNUM:{self._accNo}\tNAME:{self._name}\nAccType:{self._accType}\tBALANCE:{self._balance}')
        print("_"*100)




    
b = atm("SBI","BLR","SBI1000")
b.create("SA","Madhur",600000,1000,6)
b.info()
b.deposit(10000)


c = atm("IOB","MLR","IOB2000")
c.create("ODA","Vivek",800000,2000,6)
c.info()
c.deposit(40000)
c.withdraw(560)
b.transfer(c,5000,1018)
c.info()