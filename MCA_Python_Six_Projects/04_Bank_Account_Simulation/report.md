# Project Report: Bank Account Simulation

**Student name:** ____________________  
**Roll number:** ____________________  
**Course:** MCA III Semester — Python Programming

## 1. Abstract
The Bank Account Simulation models basic banking actions in a local Python program. It supports account creation, PIN-based demo login, deposits, withdrawals, transfers, transaction history, and a simple interest estimate.

## 2. Objectives
- Represent multiple accounts and account types.
- Validate transaction amounts and available balance.
- Store timestamped transaction records.
- Persist data in JSON.
- Demonstrate transfer and interest calculations.

## 3. Tools and concepts
Python, JSON, lists, dictionaries, functions, conditionals, exception handling, timestamps, and floating-point arithmetic.

## 4. Algorithm
1. Load account records from JSON.
2. Create an account with a unique number and four-digit demo PIN.
3. Authenticate using account number and PIN.
4. For each transaction, validate the amount and balance.
5. Record the event with a timestamp.
6. Save account records after changes.

## 5. Sample calculations
For a balance of ₹1,000, simple one-year interest at 3% is `1000 × 0.03 = ₹30`. A transfer of ₹200 subtracts ₹200 from the sender and adds ₹200 to the destination account.

## 6. Testing
Test creating duplicate account numbers, invalid PIN length, a negative deposit, withdrawal above the balance, a valid deposit, a valid transfer, and transaction history. Use only fictional details.

## 7. Limitations and security
PINs are stored in plain text and balances use Python floats. There is no encryption, real authentication security, concurrency control, or integration with banks. It is not safe for real banking.

## 8. Conclusion
The project illustrates conditional validation, transaction logic, JSON persistence, and timestamped records.
