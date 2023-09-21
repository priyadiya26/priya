'''
'''
class bankaccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self,amount):
    if amount > 0:
     self.__account_balance += amount
     print("deposited ${}. new balance:${}".format(amount,self.__account_balance))
    else:
     print("invalid deposit amount.")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdraw ${}.new balance: ${}".format(amount,self.__account_balance))
    else:
      print("invalid withdraw amount or insufficient balance:")
  def display_balance(self):
    print("account balance for {} (account #{}: ${}".format(self.__account_holder_name,self.__account_number,
                                                  
                                     self.__account_balance))
    account=bankaccount(account_number="9865636946",account_holder="priya",initial_balance=500.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(2000.0)
account.display_balance()
    
      
