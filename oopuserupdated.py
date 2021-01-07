class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
   
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
sofia = User("Sofia Kenin", "skenin@python.com")
elina = User("Elina Svitolina", "esvitolina@python.com")
maria = User("Maria Sharapova", "msharapova@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(200).display_user_balance()

monty.make_deposit(100).make_deposit(100).make_withdrawal(25).make_withdrawal(150).display_user_balance()

sofia.make_deposit(500).make_withdrawal(100).make_withdrawal(50).make_withdrawal(300).display_user_balance()

guido.transfer_money(elina, 100).display_user_balance()

elina.display_user_balance()
