# POO in python
class BankAcccount:
    def __init__(self, owner, username, password, initial_balance):
        self.owner = owner
        self.username = username
        self.__password = password
        self.__balance = initial_balance # Encapsulation
        
    def login(self, username, password):
        return username == self.username and password == self.__password

    def deposit(self, amount, menu):
        if amount > 0:
            self.__balance += amount
            self.print_message_according_menu(
                menu, f"${amount:.2f} deposit successfully."
            )
        else:
            self.print_message_according_menu(
                menu, "Deposit amount must be positive"
            )
            
    def withdraw(self, amount, menu):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.print_message_according_menu(
                menu, f"${amount:.2f} whitdraw successfully"
            )
        else: 
            self.print_message_according_menu(
                menu, "Insufficient funds or invalid amount"
            )
            
    def check_balance(self):
        return f"Currency balance ${self.__balance:.2f}"
    
    @staticmethod
    def search_accounts(accounts, username):
        for account in accounts:
            if account.username == username:
                return account
            
    @staticmethod
    def print_message_according_menu(menu, message):
        print(f"\n--- {menu.capitalize()} Menu ---")
        print(message)
    
# Uso de la clase
# account = BankAcccount("Alice", 1000) # Abstraction (user don't need to know internal details)
# account.deposit(500)
# account.withdraw(700)
# print(account.check_balance())  # Output: Saldo actual $800.00

accounts = [
    BankAcccount("Yeromi", "yeromi", "123", 1000.00),
    BankAcccount("Fiorela", "fiore", "12345", 1500.00)
]

menu = ""

def bank_account_menu():
    
    while True:
        print("\n--- Bank Account Menu ---")
        print("1. Create Account")
        print("2. Login Account")
        
        option = input("Select an option (1-2) or 'q' to quit: ")
        
        if option == '1':
            
            menu = "create account"
            
            # Ask data to cliento to create his account
            owner = input("Enter account owner name: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            initial_balance = float(input("Enter initial balance: "))
            
            account = BankAcccount(
                owner=owner,
                username=username,
                password=password,
                initial_balance=initial_balance
            )
            accounts.append(account)
            BankAcccount.print_message_according_menu(
                menu,
                f"Account created for {owner} with balance ${initial_balance:.2f}"
            )
            
        elif option == '2':
            
            menu = "login account"
            
            # Ask data to cliente to access to his account
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            bank_account : BankAcccount = BankAcccount.search_accounts(accounts, username)
            
            if bank_account:
                if bank_account.login(username, password):
                    BankAcccount.print_message_according_menu(
                        menu, "You acccess successfully to your account"
                    )
                    bank_account_menu_user(bank_account)
                    
                else:
                    BankAcccount.print_message_according_menu(
                        menu, "Your credentials are incorrect"
                    )
            else:        
                BankAcccount.print_message_according_menu(
                    menu, "Your bank account haven't founded"
                )
            
        elif option == 'q':
            break

def bank_account_menu_user(account: BankAcccount):
    while True:
        print(f"\n--- {account.owner.capitalize()} Bank Account ---")
        print(account.check_balance())
        print("1. Deposit Account")
        print("2. Withdraw Account")
        
        menu = "user account"
        option = input("Select an option (1-2) or 'q' to quit: ")
        
        if option == '1':
            
            try:
                # Pide entrada y trata de convertirla a entero
                option = input("Enter your deposit: ")
                deposit = float(option)
                
                account.deposit(deposit, menu)
                
            except ValueError:
                BankAcccount.print_message_according_menu(
                    menu, "Please enter a valid option"
                )
        
        elif option == '2':
            try:
                # Pide entrada y trata de convertirla a entero
                option = input("Enter your whitdraw: ")
                whitdraw = float(option)
                
                account.withdraw(whitdraw, menu)
                
            except ValueError:
                BankAcccount.print_message_according_menu(
                    menu, "Please enter a valid option"
                )
        
        elif option == 'q':
            BankAcccount.print_message_according_menu(
                menu, "You logout of your account successfully."
            )
            break
                    
bank_account_menu() 