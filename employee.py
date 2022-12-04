"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, paymentType, paymentInfo):
        #PaymentType is either monthly or hourly
        #PaymentInfo is a dictionary of stuff to add in
        self.name = name
        self.paymentType = paymentType
        self.paymentInfo = paymentInfo

    def get_pay(self):
        return self.paymentInfo['total']
        #pass

    def __str__(self):
        returnStr = self.name

        if self.paymentType == "monthly":
            returnStr = returnStr + " works on a monthly salary of " + str(self.paymentInfo['salary'])
        elif self.paymentType == "hourly":
            returnStr = returnStr + " works on a contract of " + str(self.paymentInfo['hours']) + " hours at " + str(self.paymentInfo['hourlyRate']) + "/hour"

        if 'contract' in self.paymentInfo.keys():
            returnStr = returnStr + " and receives a commission for " + str(self.paymentInfo['contract']) + " contract(s) at " + str(self.paymentInfo['contractPrice']) + "/contract"

        if 'bonus' in self.paymentInfo.keys():
            returnStr = returnStr + " and receives a bonus commission of " + str(self.paymentInfo['bonus'])


        returnStr = returnStr + ". Their total pay is " + str(self.paymentInfo['total']) + "."


        return returnStr


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly",  {'salary' : 4000, 'total' : 4000})

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", {'hours' : 100, 'hourlyRate' : 25, 'total' : 2500})

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", {'salary' : 3000, 'contract' : 4, 'contractPrice' : 200 , 'total' : 3800} )

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", {'hours' : 150, 'hourlyRate' : 25, 'contract' : 3, 'contractPrice' : 220 , 'total' : 4410})

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly",  {'salary' : 2000, 'bonus' : 1500, 'total' : 3500})

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", {'hours' : 120, 'hourlyRate' : 30, 'bonus' : 600, 'total' : 4200})

print(str(ariel))