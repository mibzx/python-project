"""Educational bank-account simulation. Do not use for real money or real credentials."""

import json
import os
from datetime import datetime

DATA_FILE = "accounts.json"


def load_accounts():
    """Load accounts from JSON or return an empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not load accounts: {error}")
        return []


def save_accounts(accounts):
    """Persist all account data to JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(accounts, file, indent=4)


def transaction(account, kind, amount, note):
    """Append a transaction record with timestamp to an account."""
    account["history"].append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "type": kind,
        "amount": round(amount, 2),
        "note": note
    })


def create_account(accounts):
    """Create a demo account with a unique account number and PIN."""
    number = input("New account number: ").strip()
    if not number or any(a["number"] == number for a in accounts):
        print("Account number is blank or already used.")
        return
    name = input("Account holder name: ").strip()
    pin = input("Choose a 4-digit demo PIN: ").strip()
    if not name or len(pin) != 4 or not pin.isdigit():
        print("Enter a name and exactly four digits for the PIN.")
        return
    kind = input("Account type (savings/current): ").strip().lower()
    if kind not in {"savings", "current"}:
        print("Invalid type; using savings.")
        kind = "savings"
    accounts.append({
        "number": number, "name": name, "pin": pin, "type": kind,
        "balance": 0.0, "history": []
    })
    save_accounts(accounts)
    print("Account created. Deposit money to begin.")


def authenticate(accounts):
    """Find an account and verify its demo PIN."""
    number = input("Account number: ").strip()
    pin = input("PIN: ").strip()
    account = next((a for a in accounts
                    if a["number"] == number and a["pin"] == pin), None)
    if account is None:
        print("Account or PIN is incorrect.")
    return account


def deposit(account):
    """Add a positive amount to the account."""
    try:
        amount = float(input("Deposit amount: ₹"))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError as error:
        print(f"Invalid amount: {error}")
        return
    account["balance"] = round(account["balance"] + amount, 2)
    transaction(account, "DEPOSIT", amount, "Cash deposit simulation")
    print(f"New balance: ₹{account['balance']:.2f}")


def withdraw(account):
    """Withdraw only when the amount is valid and affordable."""
    try:
        amount = float(input("Withdrawal amount: ₹"))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError as error:
        print(f"Invalid amount: {error}")
        return
    if amount > account["balance"]:
        print("Insufficient balance.")
        return
    account["balance"] = round(account["balance"] - amount, 2)
    transaction(account, "WITHDRAWAL", amount, "Cash withdrawal simulation")
    print(f"New balance: ₹{account['balance']:.2f}")


def transfer(account, accounts):
    """Transfer a positive amount between two demo accounts."""
    target_number = input("Destination account number: ").strip()
    target = next((a for a in accounts if a["number"] == target_number), None)
    if target is None or target["number"] == account["number"]:
        print("Destination account is invalid.")
        return
    try:
        amount = float(input("Transfer amount: ₹"))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError as error:
        print(f"Invalid amount: {error}")
        return
    if amount > account["balance"]:
        print("Insufficient balance.")
        return
    account["balance"] = round(account["balance"] - amount, 2)
    target["balance"] = round(target["balance"] + amount, 2)
    transaction(account, "TRANSFER_OUT", amount, f"To {target_number}")
    transaction(target, "TRANSFER_IN", amount, f"From {account['number']}")
    print("Transfer completed in this simulation.")


def calculate_interest(account):
    """Estimate simple annual interest at 3% for savings accounts."""
    if account["type"] != "savings":
        print("Interest demo is available for savings accounts only.")
        return
    interest = account["balance"] * 0.03
    print(f"Estimated one-year simple interest at 3%: ₹{interest:.2f}")
    print("This is an estimate; it is not added to the balance.")


def show_history(account):
    """Print the transaction history."""
    if not account["history"]:
        print("No transactions yet.")
        return
    for item in account["history"]:
        print(f'{item["time"]} | {item["type"]} | ₹{item["amount"]:.2f} | {item["note"]}')


def account_menu(account, accounts):
    """Show actions available after successful login."""
    while True:
        print(f"\nWelcome, {account['name']} | {account['type']} | ₹{account['balance']:.2f}")
        print("1 Deposit  2 Withdraw  3 Transfer  4 Interest estimate  5 History  0 Logout")
        choice = input("Choose: ").strip()
        if choice == "1":
            deposit(account)
        elif choice == "2":
            withdraw(account)
        elif choice == "3":
            transfer(account, accounts)
        elif choice == "4":
            calculate_interest(account)
        elif choice == "5":
            show_history(account)
        elif choice == "0":
            break
        else:
            print("Choose a valid option.")
        save_accounts(accounts)  # Save after each operation/menu action.


def main():
    """Main menu."""
    accounts = load_accounts()
    while True:
        print("\n=== Bank Account Simulation ===\n1 Create account\n2 Login\n0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            account = authenticate(accounts)
            if account is not None:
                account_menu(account, accounts)
        elif choice == "0":
            break
        else:
            print("Choose a valid option.")
        save_accounts(accounts)


if __name__ == "__main__":
    main()
