
# Bank Management System

This Python script implements a simple Bank Account Management System using MySQL as the database. The system allows users to perform three main operations: create an account, deposit funds, and withdraw funds. The script uses the mysql.connector library for database connectivity.

## Prerequisites
Before running the script, make sure you have the following:
- MySQL installed on your local machine.
- A MySQL database named test_1.
- Configuration details such as the MySQL root user and password.

## Setup
### 1. Install the required libraries:
``` bash
    pip install mysql-connector-python

```
### 2. Create a config.py file with your MySQL database password:
``` bash
    # config.py
    DB_PASSWORD = "your_mysql_password"
```
### 3. Run the script:
``` bash
    python script_name.py
```

## Features
### 1. Create Account
- Collects user information such as name, age, email, mobile number, Aadhar number, ATM pin, and initial deposit amount.
- Generates a unique account number, ATM number, CVV, and expiry date.
- Inserts user details into the MySQL database.
### 2. Credit (Deposit)
- Allows users to deposit funds into their account.
- Validates the account number and ATM pin.
- Updates the account balance in the database.
### 3. Withdraw
- Enables users to withdraw funds from their account.
- Validates the account number and ATM pin.
- Checks for sufficient funds before processing the withdrawal.
- Updates the account balance in the database.
### 4. Update Account
- Permits users to update their account information such as name, email, and mobile number.
- Validates the account number and ATM pin.
- Updates the user details in the MySQL database.
### 5. Delete Account
- Allows users to close their account.
- Validates the account number and ATM pin.
- Removes the user's details from the MySQL database.
### 6. Display Account Information
- Displays detailed information about the user's account.
- Validates the account number and ATM pin.
- Retrieves and shows the user details from the MySQL database.

## Usage
- Create Account
- Credit (Deposit)
- Withdraw
- Update Account
- Display Account Information 
- Delete Account

