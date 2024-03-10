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
        
        
def delete_acc ():
    account_number = input("\nEnter Account Number: ")
    atm_pin = input("\nEnter ATM pin: ")
    cvv=input("\n Enter your cvv number:")
    try:
        query = "SELECT * FROM userDetails WHERE account_number = %s AND atm_pin = %s AND cvv = %s"
        cursor.execute(query, (account_number, atm_pin,cvv))
        data = cursor.fetchall()
        
        if data:
            query2 = "DELETE from userDetails WHERE account_number = %s AND atm_pin = %s AND cvv = %s"
            cursor.execute(query2, (account_number, atm_pin,cvv))
            connection.commit()
            print("Account successfully deleted.")
        else:
            print("\nPlease enter correct account number and ATM pin")
            
    except Exception as e:
        print(f"Error: {e}")
        
        
def update_acc():
    
    account_number = input("\nEnter Account Number: ")
    atm_pin = input("Enter ATM pin :")
    
    try:
        query ="SELECT * FROM userDetails WHERE account_number = %s AND atm_pin = %s"
        cursor.execute(query,(account_number, atm_pin))
        data = cursor.fetchall()
        
        if data:
            new_email = input("Enter Your New Email_id :")
            new_mobile_number =input("Enter your New Mobile number :")
            new_atm_pin =input("Enter Your New ATM_PIN :")
            query2 = "UPDATE userDetails SET email = %s, mobile = %s , atm_pin = %s WHERE account_number = %s AND atm_pin = %s"
            cursor.execute(query2, ( new_email ,new_mobile_number,new_atm_pin,account_number, atm_pin))
            connection.commit()
            print("Account successfully Updated.")
        else:
            print("\nPlease enter correct account number and ATM pin")
            
    except Exception as e:
        print(f"Error: {e}")



def display_acc():
    
    account_number = input("\nEnter Account Number: ")
    atm_pin = input("Enter ATM pin :")
    
    try:
        query ="SELECT * FROM userDetails WHERE account_number = %s AND atm_pin = %s"
        cursor.execute(query,(account_number, atm_pin))
        data = cursor.fetchall()
        
        if data:
            print("\n*****ACCOUNT DETAILS*****\n")
            print(f"Account Holder's Name: {data[0][1]}")
            print(f"Age: {data[0][2]}")
            print(f"Email: {data[0][3]}")
            print(f"Mobile Number: {data[0][4]}")
            print(f"Account Number: {data[0][6]}")
            print(f"ATM Number: {data[0][7]}")
            print(f"Balance: {data[0][11]}")
                 
        else:
            print("\nPlease enter correct account number and ATM pin")
            
    except Exception as e:
        print(f"Error: {e}")

# Example usage

# Menu
def Menu ():
    print("******Bank Of Bob******")
    option = int(input("Please enter : \n1. Create Account\n2.Creadit\n3. Withdraw \n4.Delete Account\n5.Update Account\n6.Display Account Detail\n -> "))
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
    elif option == 4:
        delete_acc()
    elif option == 5:
        update_acc()
    elif option == 6:
        display_acc()
    else:
        print("INVALID INPUT")

Menu()
