class User:
    # delaring a class attribute (bank_name)
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        # declaring instance attributes
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, to_user, amount):
        self.make_withdrawl(amount)
        to_user.make_deposit(amount)

    def display_user_balance(self):
        print("User:", self.name, ", Balance: $" + str(self.account_balance))
        return self

danielName = "Daniel Shoemaker"
adrianName = "Adrian Acosta"
keithName = "Keith Hastings"

daniel = User(danielName, "danielshoe@charter.net")
adrian = User(adrianName, "adrian@something.com")
keith = User(keithName, "keith@something.com")

daniel.make_deposit(1000).make_deposit(250).make_deposit(500).make_withdrawl(150).display_user_balance()
adrian.make_deposit(1500).make_deposit(1000).make_withdrawl(300).make_withdrawl(125).display_user_balance()
keith.make_deposit(1500).make_withdrawl(150).make_withdrawl(100).make_withdrawl(200).display_user_balance()

daniel.transfer_money(keith, 250)
daniel.display_user_balance()
keith.display_user_balance()