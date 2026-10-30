balance=10000

transaction_history = [
    {
        "transaction_type": "Deposit",
        "amount": 2000,
        "previous_balance": 1000,
        "new_balance": 3000,
        "status": "Successful"
    },
    {
        "transaction_type": "Withdrawal",
        "amount": 500,
        "previous_balance": 3000,
        "new_balance": 2500,
        "status": "Successful"
    },
    {
        "transaction_type": "Deposit",
        "amount": 1500,
        "previous_balance": 2500,
        "new_balance": 4000,
        "status": "Successful"
    },
    {
        "transaction_type": "Withdrawal",
        "amount": 1000,
        "previous_balance": 4000,
        "new_balance": 3000,
        "status": "Successful"
    },
    {
        "transaction_type": "Withdrawal",
        "amount": 2000,
        "previous_balance": 3000,
        "new_balance": 1000,
        "status": "Successful"
    }
]
def deposite_money(balance):
    deposite=int(input("ENTER AMOUNT:"))
    if deposite<=0:
        return "INVALID NUMBER"
    balance=balance+deposite
    transaction_history.append({
    "transaction_type": "Deposit",
    "amount": deposite,
    "previous_balance": balance - deposite,
    "new_balance": balance,
    "status": "Successful"
})
    return f"""========== DEPOSIT RECEIPT ==========
Transaction Type : Deposit
Transaction Status: Successful
Deposit Amount   : {deposite}
Available Balance: {balance}

Your deposit has been completed successfully.
Thank you for banking with us.
======================================
"""
def withdrawal_money(balance):
    withdraw=int(input("ENTER AMOUNT:"))
    if withdraw<=0:
        return "INVALID AMOUNT"
    elif withdraw<balance:
        return "INSUFFICENT BALANCE"
    balance=balance-withdraw

    transaction_history.append({
    "transaction_type": "Withdrawal",
    "amount": withdraw,
    "previous_balance": balance + withdraw,
    "new_balance": balance,
    "status": "Successful"
})
    return f"""========== WITHDRAWAL RECEIPT ==========
    Transaction Type : Deposit
    Transaction Status: Successful
    withdrawal Amount   : {withdraw}
    Available Balance: {balance}

    Your withdrawal has been completed successfully.
    Thank you for banking with us.
    ======================================"""

def check_current_balance(balance):
            return f"""========== ACCOUNT BALANCE ==========
        Account Holder : [MUSAB MOHAMMEDAMIN]
        Account Status : Active
        Available Balance: {balance} ETB

        Your account balance has been retrieved successfully.
        Thank you for banking with us.
        ====================================="""


def display_transaction_history():
    for transaction in transaction_history:
        print(transaction)

while True:
    print("""
========================================
       AKIBA BANK
========================================
1. Deposit Money
2. Withdraw Money
3. Check Account Balance
4. View Transaction History
5. Exit
========================================
""")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(deposite_money(balance))

    elif choice == "2":
        print(withdrawal_money(balance))

    elif choice == "3":
        print(check_current_balance(balance))

    elif choice == "4":
        display_transaction_history()

    elif choice == "5":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")