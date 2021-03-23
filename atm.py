class atm:
    bank = 'National Bank'

    def _init_(self, cardNumber, pinNumber, balance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = balance



    def greeting(self):
        print("Welcome back to your account!")

    def balanceInquiry(self):
        print("balance is 87.00 dollars")

    def pinNumberInquiry(self):
        print("Your PIN number is 76541")

    def cardNumberInquiry(self):
        print("Your card number ends with 2983")
    



    

acc1 = atm()


acc1.greeting()
acc1.pinNumberInquiry()
acc1.cardNumberInquiry()

print("Your account balance is:")
acc1.balanceInquiry()







