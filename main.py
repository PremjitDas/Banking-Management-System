import mysql.connector
from config import DB_PASSWORD
import os
import random
from datetime import datetime, timedelta
connection = mysql.connector.connect(   
    host="localhost",
    user="root",
    password=DB_PASSWORD,
    database="test_1"
)
cursor = connection.cursor()

# GENERATING RANDOM DATES

def generate_random_date():
    current_date = datetime.now()
    end_date = datetime(2030, 12, 31)
    date_difference = (end_date - current_date).days
    random_days = random.randint(0, date_difference)
    random_date = current_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

# CREATING ACCOUNT

def acc_create(name, age, email, mobile,aadhar_number, atm_pin, balance):
    id = os.urandom(10).hex()
    name = name
    age = age
    email = email
    mobile = str(mobile)
    aadhar_number = str(aadhar_number)
    account_number = str(random.randint(10**9, 10**10 - 1))
    atm_number = str(random.randint(10**9, 10**10 - 1))
    cvv = random.randint(10**2, 10**3 - 1)
    expiry_date = generate_random_date()
    atm_pin = atm_pin
    balance = balance
    try:
        query = "INSERT INTO userDetails (id, name, age, email, mobile, aadhar_number, account_number, atm_number, cvv, expiry_date, atm_pin, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (id, name, age, email, mobile, aadhar_number, account_number, atm_number, cvv, expiry_date, atm_pin, balance)
        cursor.execute(query, values)
        connection.commit()
        print("Account Created Successfully!")
    except ValueError as e:
        print(e)
        
def credit():
    account_number = input("\nEnter Account Number: ")
    atm_pin = input("\nEnter ATM pin: ")
    deposit = float(input("\nEnter Deposit amount: "))
    try:
        query = "SELECT * FROM userDetails WHERE account_number = %s AND atm_pin = %s"
        cursor.execute(query, (account_number, atm_pin))
        data = cursor.fetchall()
        if data:
            current_balance = data[0][-1]  
            new_balance = current_balance + deposit

            query2 = "UPDATE userDetails SET balance = %s WHERE account_number = %s AND atm_pin = %s"
            cursor.execute(query2, (new_balance, account_number, atm_pin))
            connection.commit()

            print(f"Deposit of {deposit} successful. New balance: {new_balance}")
        else:
            print("\nPlease enter correct account number and ATM pin")
    except Exception as e:
        print(f"Error: {e}")

    
def withdraw():
    account_number = input("\nEnter Account Number: ")
    atm_pin = input("\nEnter ATM pin: ")
    withdrawal_amount = float(input("\nEnter Withdrawal amount: "))
    
    try:
        query = "SELECT * FROM userDetails WHERE account_number = %s AND atm_pin = %s"
        cursor.execute(query, (account_number, atm_pin))
        data = cursor.fetchall()
        
        if data:
            current_balance = data[0][-1]
            
            if withdrawal_amount <= current_balance:
                new_balance = current_balance - withdrawal_amount
                
                query2 = "UPDATE userDetails SET balance = %s WHERE account_number = %s AND atm_pin = %s"
                cursor.execute(query2, (new_balance, account_number, atm_pin))
                connection.commit()

                print(f"Withdrawal of {withdrawal_amount} successful. New balance: {new_balance}")
            else:
                print("\nInsufficient funds. Withdrawal amount exceeds available balance.")
        else:
            print("\nPlease enter correct account number and ATM pin")
    except Exception as e:
        print(f"Error: {e}")

# Example usage


    


# Menu
def Menu ():
    option = int(input("Please enter \n1. Create Account\n2.Creadit\n3. Withdraw \n>"))
    if option == 1:
        try:
            name=input("Enter your name :")
            age=input("Enter your age : ")
            email=input("Enter your email id :")
            mobile=input("Enter your mobile number :")
            aadhar_number=input("Ente your aadhar_number :")
            atm_pin=int(input("Enter your atm_pin :"))
            balance = float(input("Enter initial deposit amount: "))
            acc_create(name, age, email, mobile,aadhar_number, atm_pin, balance)
        except ValueError as e:
            print("Please enter your valid information :")
            print(e)
    elif option == 2:
        credit()
    elif option == 3:
        withdraw()
    else:
        print("INVALID INPUT")

Menu()
