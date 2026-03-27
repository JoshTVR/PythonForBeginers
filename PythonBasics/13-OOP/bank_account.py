"""
bank_account.py — OOP Capstone Project
Chapter 13: OOP

Full-circle moment: remember the ATM PIN from Chapter 4?
Now we build the bank account itself as a class.

Demonstrates:
- Class with business logic (no negative balance withdrawals)
- Guard clauses inside methods
- __str__ for readable output
- Multiple instances operating independently
- Objects in a list, sorted by balance
"""

class BankAccount:
    """
    Represents a bank account with deposit and withdrawal functionality.
    Balance can never go below zero.
    """

    def __init__(self, owner, balance=0):
        """
        owner  : str   — account holder's name
        balance: float — starting balance (default: 0)
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add funds to the account."""
        if amount <= 0:
            print('❌ Deposit amount must be greater than zero.')
            return
        self.balance += amount
        print(f'✅ ${amount:,.2f} deposited. Balance: ${self.balance:,.2f}')

    def withdraw(self, amount):
        """
        Remove funds from the account.
        Refuses if amount exceeds current balance.
        """
        if amount <= 0:
            print('❌ Withdrawal amount must be greater than zero.')
            return
        if amount > self.balance:
            print(f'❌ Insufficient funds. Balance: ${self.balance:,.2f}')
            return
        self.balance -= amount
        print(f'✅ ${amount:,.2f} withdrawn. Balance: ${self.balance:,.2f}')

    def transfer(self, amount, target_account):
        """Transfer funds from this account to another BankAccount."""
        if amount > self.balance:
            print(f'❌ Cannot transfer ${amount:,.2f} — insufficient funds.')
            return
        self.balance -= amount
        target_account.balance += amount
        print(f'✅ ${amount:,.2f} transferred from {self.owner} to {target_account.owner}.')

    def show_balance(self):
        """Print the current balance."""
        print(f'{self.owner}\'s balance: ${self.balance:,.2f}')

    def __str__(self):
        return f'BankAccount({self.owner}, ${self.balance:,.2f})'


# ─────────────────────────────────────────
# USING THE CLASS
# ─────────────────────────────────────────

account1 = BankAccount('Valentina', 1000)
account2 = BankAccount('Lucas')             # starts at $0 (default)
account3 = BankAccount('Camila', 500)

print('--- Initial State ---')
print(account1)
print(account2)
print(account3)

print('\n--- Transactions ---')
account1.deposit(2500)
account1.withdraw(300)
account2.deposit(800)
account2.withdraw(1500)   # should fail — insufficient funds
account3.deposit(200)
account1.transfer(500, account2)

print('\n--- Final Balances ---')
accounts = [account1, account2, account3]
for acc in accounts:
    acc.show_balance()

# Sort accounts by balance (richest first)
ranked = sorted(accounts, key=lambda a: a.balance, reverse=True)
print(f'\nRichest account: {ranked[0].owner} (${ranked[0].balance:,.2f})')

# Output:
# --- Initial State ---
# BankAccount(Valentina, $1,000.00)
# BankAccount(Lucas, $0.00)
# BankAccount(Camila, $500.00)
#
# --- Transactions ---
# ✅ $2,500.00 deposited. Balance: $3,500.00
# ✅ $300.00 withdrawn. Balance: $3,200.00
# ✅ $800.00 deposited. Balance: $800.00
# ❌ Insufficient funds. Balance: $800.00
# ✅ $200.00 deposited. Balance: $700.00
# ✅ $500.00 transferred from Valentina to Lucas.
#
# --- Final Balances ---
# Valentina's balance: $2,700.00
# Lucas's balance: $1,300.00
# Camila's balance: $700.00
#
# Richest account: Valentina ($2,700.00)
