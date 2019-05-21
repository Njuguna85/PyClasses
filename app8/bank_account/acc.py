"""
    OOP for one account
"""


class bank_account:
    def __init__(self, filepath):
        self.path = filepath
        # path is an instance variable
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
            # balance is an instance variable and self is a bank_account object

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.path, 'w') as file:
            file.write(str(self.balance))


# calling an instance of bank_account class
myAccount = bank_account("acc.txt")
# print(myAccount.balance)
# myAccount.withdraw(100)
# myAccount.commit()
# print(myAccount.balance)
# myAccount.deposit(1600)
# myAccount.commit()
# print(myAccount.balance)


class checking_account(bank_account):
    def __init__(self, path):
        bank_account.__init__(self, path)

    def transfer(self, amount):
        fee = 27
        self.balance = self.balance - amount - fee
        bank_account.commit(self)


checking = checking_account("acc.txt")
checking.transfer(200)
print(checking.balance)
