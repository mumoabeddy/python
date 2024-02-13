class mpesa:
    def  __init__ (self,account_balance,phone_number):
        self.account_balance=account_balance
        self.phone_number=phone_number
    def sendmoney (self,account,receipient):
        if self.account_balance >= amount:
            self.account_balance-= amount
            print( f"{amount} kes sent to {receipient}")
        else:
            print("insuficient amount to send")
class personampesa(mpesa):
 def __init__(self,account_balance,phone_number):
    print()

 class bussinessmpesa(mpesa):
    def __init__(self,account_ibalancer,bussines_id,phone_numer):
        super().__init__(account_balance,phone_numer)
        print()
