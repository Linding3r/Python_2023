class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)

class Account:
    def __init__(self, account_number, balance, customer):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer

class Customer():
    def __init__(self, name, address=None, phone=None, email=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
    


bank1 = Bank("Danke Bank", "Nørregade 1")
bank2 = Bank("Nordea", "Østerbrogade 2")

customer1 = Customer("John Doe", "Vesterbrogade 34", "12345678", "john.doe@gmail.com")
customer2 = Customer("Jane Doe", "Vesterbrogade 34")

account1 = Account("123456789", 1000, customer1)
account2 = Account("987654321", 500, customer2)

bank1.add_account(account1)
bank2.add_account(account2)

print(bank1.accounts[0].customer.name)
print(bank2.accounts[0].customer.name)