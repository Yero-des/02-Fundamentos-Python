# Pooo 2 in Python
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance
        

    # Encapsulamiento
    """ You can create private and protected variables """
    def _get_balance(self):
        return self.__balance
    
    def _set_balance(self, new_balance):
        self.__balance = new_balance
            
    # Abstraccion
    """ A method can be abstract and don't have any logic """
    @abstractmethod
    def withdraw(self, amount):
        pass 
    
    def deposit(self, amount):
        if amount > 0:
            self._set_balance(self._get_balance() + amount)
            
    def check_balance(self):
        return f"Saldo actual: ${self._get_balance()}"

""" A class can be hereded from another object """
class SavingAccount(BankAccount): # Herencia
    # Polimorfismo
    """ Same method, diferent behavior """
    def withdraw(self, amount):
        penalty = amount * 0.05
        total = amount + penalty
        if 0 < total <= self._get_balance():
            self._set_balance(self._get_balance() - total)
        else:
            print("Fondos insuficientes en la cuenta de ahorro")
            
class PayrollAccount(BankAccount): # Herencia
    # Polimorfismo
    """ Same method, diferent behavior """
    def withdraw(self, amount):
        if 0 < amount <= self._get_balance():
            self._set_balance(self._get_balance() - amount)
        else:
            print("Fondos insuficientes en la cuenta de ahorro")
            
saving = SavingAccount("Ricardo", 1000)
payroll  = PayrollAccount("Ricardo", 1000)

saving.deposit(500)
payroll.deposit(500)
saving.withdraw(100)
payroll.withdraw(100)

print(f"Cuenta de ahorro: {saving.check_balance()}")
print(f"Cuenta de nómina: {payroll.check_balance()}")