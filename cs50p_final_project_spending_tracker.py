import re
import sys
import csv
import os
import pandas as pd
import maskpass
from datetime import date

#menu for login
def log_in_menu():
    print()
    while True:
        user_name = input("Please enter your user name: ").strip()
        password = maskpass.askpass(mask="*")
        print()
        print("Checking ...\n")
        flag = log_in(user_name, password)
        if flag:
            print(f"Hello {user_name}")
            break
        else:
            print("Invalid user_name or password!\n")
            print("Input 1 to re-input the password and user name")
            print("Input 2 to register an account")
            print()
            try:
                choice = int(input("Indicate your choice: "))
                if choice < 0 or choice > 2:
                    raise(Exception)
            except (ValueError, Exception) as e:
                print("Input can only either be 1 or 2!\n")
            else:
                if choice == 2:
                    print()
                    break
        if choice == 2:
            sign_up()    
    main_menu(user_name)  
#function for user to login the system
def log_in(user_name, password):
    info = {}
    try:
        f = open("spending_tracker.csv", "r")
    except FileNotFoundError:
        return False
    else:
        reader = csv.reader(f)
        for row in reader:
            if "username" in row and "pasword" in row:
                continue
            elif len(row) == 2:
                name = row[0]
                passw = row[1]
                info[name] = passw
        if user_name not in info.keys():
            return False
        else:
              stored_pass = info[user_name]
              if stored_pass != password:
                  return False
    return True
#function for user to create an account for the system
def sign_up():
    print("Welcome user!")
    print("You are going to register an account for this system\nUser name and password will be required for logging in the system\n")
    user_name = get_user_name()
    password = get_password()
    record_user(user_name, password)
    sign_up_menu()
    
#menu for sign up
def sign_up_menu():
    print()
    print("Input 1 to proceed to the login page")
    print("Input 2 to exit the system")
    while True:
        try: 
            choice = input("Indicate your choice: ")
        except ValueError:
            print("Input must be either 1 or 2! Please try again\n")
        else:
            if choice == "1" or choice == "2":
                print()
                break
    if choice == "1":
        log_in_menu()
    else:
        sys.exit("Thanks for using! Bye!")
        
                 
    
#function to get user's user name
def get_user_name():
    user_name_regex = r"^[a-zA-z]+([0-9_ ]+)?$"
    while True: 
        user_name = input("Please enter your user name: ")
        matches = re.search(user_name_regex, user_name)
        if not matches:
            print("Invalid user_name\nUser name must not begin with integers\nPuncuations are not allowed except _ and whitespce\n")
        else:
            break
    while True:
        flag = check_username_existence(user_name)
        if not flag:
            break
        else:
            print("Username already existed in the program!\nTry to register an account with another username\n")
            user_name = input("Please enter your user name: ")
    return user_name

#function to get user's password
def get_password():
    password_regex = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-.]).{8,}$"
    while True:
        print("This is the requirement for the password:\n1. The password length must be at least 8 digits \n2. Including at least one digit\n3. Including at least one upper case character\n4. Including at least one lower case character\n5. Including at least one special character\n")
        password = maskpass.askpass(mask="*")
        matches = re.search(password_regex, password)
        if matches:
            break
        else:
            print("Invalid password format, please try again\n")
    while True:
        re_password = maskpass.askpass(mask="*")
        if password == re_password:
            print("Register successfully!\n")
            break
    return password

#function to record the user name and password to a csv file  
def record_user(user_name, password):
    flag = os.path.exists("spending_tracker.csv")
    headers = ["username", "password"]
    data = [user_name, password]
    with open("spending_tracker.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if flag:
            writer.writerow(data)    
        else:
            writer.writerow(headers)
            writer.writerow(data)
            
#function to check whether a username is being registered
def check_username_existence(username):
    try:
        f = open("spending_tracker.csv","r")
    except FileNotFoundError:
        return False
    else:
        reader = csv.reader(f)
        username_info = {}
        for row in reader:
            if "username" in row and "password" in row:
                continue
            elif len(row) == 2:
                username_from_csv= row[0]
                password = row[1] 
                username_info[username_from_csv] = password
                
        f.close()
        if username in username_info.keys():
            return True
        return False
                          
#menu for the spending tracker
def menu():
    print("Welcome to this spending trcker\n")
    print("Input 1 for logging into the spending tracker")
    print("Input 2 for signing up an account for the spending tracker")
    print("Input 3 for quitting the system\n")
    
    try:
        choice = int(input("Indicate your choice: "))
        if choice < 0 or choice > 3:
            raise(Exception)
    except (ValueError, Exception) as e:
        print("Input must be either 1, 2 or 3!\nPlease indicate your choice again!")
    else:
        if choice == 1:
            log_in_menu()
        elif choice == 2:
            sign_up()
        else:
            sys.exit("Thanks for using! Bye!")
    menu()
#menu after logging in the system
def main_menu(username):
    print("This is the main menu of the system\n")
    print("Input 1 to initialize the balance of your account")
    print("Input 2 to record your spendings and incomes")
    print("Input 3 to adjust the records of spendings of previous days") 
    print("Input 4 to see the summary of the spending")
    print("Input 5 to exit the system")
    print()          
    while True:
        try:
            choice = int(input("Indicate your choice: "))
        except ValueError:
            print("Input must be either 1, 2, 3, 4 or 5!\nPlease indicate your choice again!")
        else:
            break
    if choice == 1:
        balance_menu(username)
    elif choice == 2:
        record_menu(username)
    elif choice == 3:
        adjust_menu(username)
    elif choice == 4:
        summary_menu(username)
    elif choice == 5:
        print()
        exit(f"Goodbye {username}")
    main_menu(username)
#function to initalize the balance of different accounts
def init_bal(username):
    print("The account balance will be initialize with the following format:")
    print("Name of the account Inital balance for the account e.g. bank 10000\n")
    bal = {}
    read_bal = {}
    if os.path.exists(f"{username}_balance.csv"):
        with open(f"{username}_balance.csv") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                    read_bal[row[0]] = row[1]
    while True:
        try:
            account = input("Enter your details: ").capitalize().strip().split(" ")
            account[1] = round(float(account[1]),2)
        except IndexError:
            print("Input's format is not correct, please try again")
        else:
            """
            can have a better approach to adjust the account balance
            """
            if account[0] in read_bal.keys() or account[0] in bal.keys():
                print("The account has already stored! Invalid input")
            else:
                bal[account[0]] = account[1]
            cont = input("Continue? y/n: ").lower().strip()
            if cont == "n":
                print("Details stored!\n")
                flag = os.path.exists(f"{username}_balance.csv")
                with open(f"{username}_balance.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    if flag == False:
                        headers = ["account_name", "balance"]
                        writer.writerow(headers)
                    for element in bal:
                        if element != "":
                            data = [element, bal[element]]
                            writer.writerow(data)
                break
    balance_menu(username)
            
#menu inside the initialize function
def balance_menu(username):
    print()
    print("Input 1 to add balance to the current account")
    print("Input 2 to delete an account stored in balance")
    print("Input 3 to go back to the main menu of the system")
    while True:
        try:
            choice = int(input("Indicate your choice: "))
            if choice < 1 or choice > 3:
                raise(Exception)
        except (ValueError, Exception) as e:
            print("Input must be either 1, 2 or 3!\nPlease indicate your choice again!")
        else:
            break
    print()
    if choice == 1:
        init_bal(username)
    elif choice == 2:
        del_balance(username)
    elif choice == 3:
        main_menu(username)
        
#function to delete the balance stores
def del_balance(username):
    print("Balance stores inside the system")
    print_account(username)
    stored_balacnce = {}
    counter = 1
    with open(f"{username}_balance.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            stored_balacnce[counter] = row[0]
            counter += 1
    print()
    while True:
        print("Input the number of the balance of the accounts stored")
        choice = int(input("Indicate your choice: "))
        if choice < 0 or choice < counter-1:
            print("Invalid input, please try again!\n")
        else: 
            print("After deleting the account, the record cannot be restored")
            sure = input("Are you sure that you want to delete this account? y/n: ").strip().lower()
            #print(f"account: {stored_balacnce[choice]}")
            if sure == "y" or sure == "yes":
                df = pd.read_csv(f"{username}_balance.csv")
                df = df.drop(df[df.account_name == stored_balacnce[choice]].index)
                df.to_csv(f"{username}_balance.csv", index=False)
                break
            else:
                print("Operation failed, back to the balance menu")
                break
    balance_menu(username)
    
    
#function to print the account stores
def print_account(username):
    counter = 1
    print("Stored balance:")
    with open(f"{username}_balance.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(f"{counter} Account: {row[0]} with balance: {row[1]}")
            counter+=1
#menu for records spending per day
def record_menu(username):
    print()
    print("Input 1 to record the spending of today")
    print("Input 2 to record the spending of other days")
    print("Input 3 to go back to the main menu\n")
    while True:
        try:
            choice = int(input("Indicate your choice: "))
            if choice < 1 or choice >3:
                raise(Exception)
        except (ValueError, Exception) as e:
            print("Input must be either 1, 2 or 3!\nPlease indicate your choice again!")
        else:
            break
    print()
    if choice == 1:
        record(username)
    elif choice == 2:
        record_date = get_date()
        record(username, record_date)  
    elif choice == 3:
        main_menu(username)
    else:
        print("Invalid input! Please try again")
        record_menu(username)

#function to store the spending or income of today
def record(username, date=date.today()):
    print(f"Record date is {date}")
    bal_stored = get_balnce(username)
    records = []
    print("Enter the expenses or incomes of today in the following format: Category Amount Acoount e/i")
    print("Category means the type of spending e.g. food")
    print("Amount means money in integer")
    print("Account means the balance stores in the system")
    print("e stands for expenses i stands for incomes\n")
    while True:
        amount_flag = True
        account_flag = True
        applicable_flag = True
        record = []
        temp = input("Enter your record: ").strip()
        if len(temp) > 4:
            counter = 0
            category = ""
            temp = temp.split(" ")
            while counter < (len(temp) - 3):
                if category != "":
                    category = category + "_" + temp[counter]
                else:
                    category = category + temp[counter]
                counter+=1
            record.append(category)
            record.append(round(float(temp[len(temp)-3]),2))
            record.append(temp[len(temp)-2])
            record.append(temp[len(temp)-1])
        else:
            record = temp.split(" ")
        record.append(date)
        record[2] = record[2].capitalize()
        if record[2] not in bal_stored.keys():
            print("Account balance not found")
            amount_flag = False
        if float(record[1]) < 0:
            print("Invalid amount input, it must be greater than 0") 
            account_flag = False
        if amount_flag and account_flag:
            if record[3].lower() == "e" and bal_stored[record[2]] >= float(record[1]):
                bal_stored[record[2]] -= float(record[1])
            elif record[3].lower() == "i":
                bal_stored[record[2]] += float(record[1])
            else:
                print("Insufficient balance left")
                applicable_flag = False
            if applicable_flag:
                records.append(record)
                choice = input("Continue? y/n: ").strip().lower()
                if choice == "n" or choice == "no":
                    bal_stored_formatted = []
                    bal_stored_formatted = format_balance(bal_stored)
                    update_balance(username, bal_stored_formatted)
                    write_record(username, records)
                    break
            
    record_menu(username)

#function to check leap year
def check_leap_year(year):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0
        
#function to check the validate of date
def check_date(year, month, day):
    if month < 0 or month > 12:
        return False
    if month == 2 and day == 29:
        return check_leap_year(year)
    if day > 31 or day < 0:
        return False
    if month == 4 or month == 6  or month == 9 or month == 11:
        return day <= 30
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return day <= 31
    if month == 2:
        return day <= 28
    
#function to prompt user for date
def get_date():
    while True:
        year, month, day =[int(x) for x in input("Please input the date of the record in the format of YYYY-MM-DD: ").split("-")]
        if check_date(year, month, day):
            return date(year,month,day)
               
#function to adjust the balances store in the csv  
def adjust_balance(username, account, amount, type):
    bal_before_format = get_balnce(username)
    if type == "e":
        bal_before_format[account] += amount
    elif type == "i":
        bal_before_format[account] -= amount
    bal_after_format = format_balance(bal_before_format)
    update_balance(username, bal_after_format)

#function to update the balances store in the csv
def update_balance(username, balances):
    with open(f"{username}_balance.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["account_name","balance"])
        writer.writeheader()
        writer.writerows(balances)

#function to get the remaining balance stored in the account
def get_account_balance(username, account_name):
    with open(f"{username}_balance.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == account_name:
                return float(row[1]) 
      
#function to get the balances store in the csv file
def get_balnce(username):
    bal_dict = {}
    with open(f"{username}_balance.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            bal_dict[row[0]] = float(row[1])
    return bal_dict        

#function to check the exisitence of an account
def check_account(username, account_name):
    with open(f"{username}_balance.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == account_name:
                return True
    return False

#function to change the format of the dictionary
def format_balance(balances):
    balances_list = []
    for balance in balances:
        balances_dict = {}
        balances_dict["account_name"] = balance
        balances_dict["balance"] = balances[balance]
        balances_list.append(balances_dict)
    return balances_list

#function to write the records into a csv file
def write_record(username, records):
    header = ["catergory", "amount", "account_name", "type", "date"]
    if os.path.exists(f"{username}_records.csv") == False:
        f = open(f"{username}_records.csv", "a", newline="")
        writer = csv.writer(f)
        writer.writerow(header)
        f.close()
    else:     
        with open(f"{username}_records.csv", "a", newline="") as f:
            writer = csv.writer(f)
            for record in records:
                writer.writerow(record)
#menu for adjusting the records stored in the system
def adjust_menu(username):
    print()
    print("Input 1 to adjust the records stored in the system")
    print("Input 2 to go back to the main menu of the system")
    try:
        choice = int(input("Please indicate your choice: "))
        if choice < 1 or choice > 2:
            raise(Exception)
    except (ValueError, Exception) as e:
        print("Input must be either 1 or 2")
    else:
        print()
        if choice == 1:
            adjust(username)
            adjust_menu(username)
        elif choice == 2:
            main_menu(username)

#function to change the record stored in the program        
def adjust(username):
    print()
    if os.path.exists(f"{username}_records.csv") == False:
        print("Please add records to the system first!")
        return main_menu(username)
    date_to_change = get_date()
    all_records = get_records(username)
    records = print_records_with_date(username, all_records, date_to_change)
    while True:
        choice = int(input("Please enter the index of the record to change: "))
        if choice < 0 or choice > len(records):
            print("Invalid input")
        else:
            print(f"Record to change: {records[choice-1]}")
            break
    print(f"Input 1 for changing Category: {records[choice-1]['category']}\nInput 2 for changing Amount: {records[choice-1]['amount']}\nInput 3 for changing Account: {records[choice-1]['account_name']}\nInput 4 for changing Type: {records[choice-1]['type']}\nInput 5 for changing Date: {records[choice-1]['date']}\nInput 6 for retype the record\nInput 7 to delete the record")
    
    try:
        answer = int(input("Please indicate your choice: "))
        if answer < 0 or answer > 7:
            raise(Exception)
    except (ValueError, Exception) as e:
        print("Input must be either 1, 2, 3, 4, 5, 6 or 7")
    else:
        print()
        if answer == 1:
            change = input("Please enter the new category: ").strip()
            change_records(username, all_records, records, choice-1, 1, change) 
        
        elif answer == 2:
            remain_balance = get_account_balance(username, records[choice-1]["account_name"])
            flag = False
            try:
                change = float(input("Please enter the new amount: ").strip())
                if records[choice-1]["type"] == "e" and (change > float(records[choice-1]["amount"])) and (remain_balance < (change - float(records[choice-1]["amount"]))):
                    flag = True
                    raise(Exception)
                if records[choice-1]["type"] == "i" and (change < float(records[choice-1]["amount"])) and (remain_balance < (float(records[choice-1]["amount"]) - change)):
                    flag = True
                    raise(Exception)
            except (ValueError, Exception) as e:
                if flag:
                    print("Insufficient amount remain in the balance for the changes, operation failed...\n")
                    adjust_menu(username)
                else:
                    print("Input should in number")
            else:
                change_records(username, all_records, records, choice-1, 2, change) 
        elif answer == 3:
            while True:
                change = input("Please enter the new account: ").strip().capitalize()
                if check_account(username,records[choice-1]["account_name"]):
                    if get_account_balance(username, change) < float(records[choice-1]["amount"]) and records[choice-1]["type"] == "e":
                        print(f"Insufficient balance remain in {change}, operation failed...\n")
                        adjust_menu(username)
                    change_records(username, all_records, records, choice-1, 3, change) 
                    break
                else:
                    print("Account not exist")
                    continue_ = input("Coninue y/n: ").strip().lower()
                    if continue_ == "n":
                        adjust_menu(username)
                    
        elif answer == 4:
            if records[choice-1]["type"] == "i":
                balance = get_account_balance(records[choice-1]["account_name"])
                if balance < 2*float(records[choice-1]["ammount"]):
                    print("Insufficient money left in balance, operation failed\n")
                    adjust_menu(username)
            change_records(username, all_records, records, choice-1, 4, records[choice-1]["type"]) 
        elif answer == 5:
            year, month, day = [int(x) for x in input("Please enter the new date in the format of YYYY-MM-DD: ").strip().split("-")]
            change_records(username, all_records, records, choice-1, 5, date(year,month,day)) 
        elif answer == 6 or answer == 7:
            index = get_index(all_records, records, choice-1)
            if records[choice-1]["type"] == "i" and get_account_balance(username, records[choice-1]["account_name"]) < float(records[choice-1]["amount"]):
                print("Insufficient money left in the account, operation failed\n")
                adjust_menu(username)
            else:
                adjust_balance(username, records[choice-1]["account_name"], float(records[choice-1]["amount"]), records[choice-1]["type"])
                df = pd.read_csv(f"{username}_records.csv")
                df = df.drop(df.index[index])
                df.to_csv(f"{username}_records.csv", index=False)
                if answer == 6:
                    record_date = get_date()
                    record(username, record_date)
        adjust_menu(username)
        
#function to change the specific part of the records for part, 1:category, 2 amount, 3 account, 4 type, 5 date
def change_records(username, records_list, records, choice, part, change):
    for record in records_list:
        if record == records[choice]:
            record["amount"] = float(record["amount"])
            if part == 1:
                record["category"] = change
            elif part == 2:
                diff = abs(record["amount"] - float(change))
                if (record["amount"] > float(change)) and record["type"] == "e":
                    adjust_balance(username, record["account_name"], diff, "e")
                elif (record["amount"] > float(change)) and record["type"] == "i":
                    adjust_balance(username, record["account_name"], diff, "i")
                elif (record["amount"] < float(change)) and record["type"] == "e":
                    adjust_balance(username, record["account_name"], diff, "i")
                else:
                    adjust_balance(username, record["account_name"], diff, "e")
                record["amount"] = change
            elif part == 3:
                if record["type"] == "e":
                    adjust_balance(username, record["account_name"], record["amount"], "e")
                    adjust_balance(username, change, record["amount"], "i")
                else:
                    adjust_balance(username, record["account_name"], record["amount"], "i")
                    adjust_balance(username, change, record["amount"], "e")
                record["account_name"] = change
            elif part == 4:
                if record["type"] == "e":
                    change = "i"
                    adjust_balance(username, record["account_name"], 2*float(record["amount"]), "e")
                elif record["type"] == "i":
                    change = "e"
                    adjust_balance(username, record["account_name"], 2*float(record["amount"]), "i")
                record["type"] = change
            elif part == 5:
                record["date"] = change
            output = record
            break
            
    print(f"\nThe record has changed from Category: {records[choice]['category']}, Amount: {records[choice]['amount']}, Account: {records[choice]['account_name']}, Type: {records[choice]['type']}, Date: {records[choice]['date']}")
    print(f"To Category: {output['category']}, Amount: {output['amount']}, Account: {output['account_name']}, Type: {output['type']}, Date: {output['date']}\n")
    update_records(username, records_list)
    
#function to update the records stored in the system
def update_records(username, records):
    with open(f"{username}_records.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["category","amount","account_name","type","date"])
        writer.writeheader()
        writer.writerows(records)

#function to get all the records stored in the system
def get_records(username):
    records = []
    with open(f"{username}_records.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            record = {}
            record["category"] = row[0]
            record["amount"] = row[1]
            record["account_name"] = row[2]
            record["type"] = row[3]
            record["date"] = row[4]
            records.append(record)
    return records

#function to print the records on a specific date            
def print_records_with_date(username, records, date_to_change):
    output_records = []
    print(f"All the records found for {date_to_change} are: ")
    date_flag = False
    counter = 1
    for record in records:
        year,month,day = record['date'].split("-")
        if date(int(year),int(month),int(day)) == date_to_change:
            print(f"{counter}. Category: {record['category']}, Amount: {record['amount']}, Account: {record['account_name']}, Type: {record['type']}")
            date_flag = True
            counter += 1
            output_records.append(record)
            
    if date_flag == False:
        print("Records not found")
        main_menu(username)
    print()
    return output_records

#function to print records 
def print_records(username):
    counter = 1
    with open(f"{username}_records.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(f"{counter}. Category: {row[0]}, Amount: {row[1]}, Account: {row[2]}, Type: {row[3]}, Date: {row[4]}")
            counter+=1

#function to get the index of the records to be deleted
def get_index(records, record, index):
    counter = 0
    for element in records:
        if element == record[index]:
            return counter
        counter += 1
            
#function to get all the category of the records stored in the system
def get_category(username, type):
    return_list = []
    with open(f"{username}_records.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] in return_list:
                continue
            elif row[3] == type:
                return_list.append(row[0])
    return return_list

#function to sum all the spends by each category
def sum_by_category(username, category_list, type):
    return_dict = {}
    #init the return_dict
    for category in category_list:
        return_dict[category] = 0
    with open(f"{username}_records.csv","r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[3] == type:
                return_dict[row[0]] += float(row[1])
                return_dict[row[0]] = round(return_dict[row[0]],2)
    return return_dict

#function to sort the records by the amount 
def sort_dict(category_dict):
    sorted_dict = sorted(category_dict.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_dict)
    return converted_dict

#function to print the summary of records 
def print_summary(dictionary, type):
    counter = 1
    if type == "e":
        print("\nThe expenses summary: ")
    elif type == "i":
        print("\nThe incomes summary: ")
    for element in dictionary:
        ordinal = ordinal_number(counter)
        print(f"{ordinal} {element}: {dictionary[element]}")
        counter+=1
    print()
#menu for the summary function
def summary_menu(username):
    print()
    print("Input 1 to display the account store in the system")
    print("Input 2 to display all the records stored in the system")
    print("Input 3 to view the overall summary for all expenses stored in the system.")
    print("Input 4 to view the overall summary for all incomes stored in the system.")
    print("Input 5 to go back to the main menu")
    
    try:
        choice = int(input("Please indicate your choice: "))
        if choice < 1 or choice > 5:
            raise(Exception)
    except (ValueError, Exception) as e:
        print("Input must be either 1, 2, 3, 4 or 5! Please try again")
    else:
        print()
        if choice == 1:
            if os.path.exists(f"{username}_balance.csv"):
                print_account(username)
            else:
                print("Please initialize your account first")
        elif choice == 2:
            print_records(username)
            print()
        elif choice == 3:
            category_list = get_category(username, "e")
            category_dict = sum_by_category(username, category_list, "e")
            sorted_dict = sort_dict(category_dict)
            print_summary(sorted_dict, "e")    
        elif choice == 4:
            category_list = get_category(username, "i")
            category_dict = sum_by_category(username, category_list, "i")
            sorted_dict = sort_dict(category_dict)
            print_summary(sorted_dict, "i")
        elif choice == 5:
            main_menu(username)           
    summary_menu(username)
    
#function to return the ordinal number of a value
def ordinal_number(n):
    unit_digit = ""
    unit_digit = str(n)[-1]
    if unit_digit == "1":
        return str(n) +"st"
    elif unit_digit == "2":
        return str(n) + "nd"
    elif unit_digit == "3":
        return str(n) + "rd"
    else:
        return str(n) + "th"


def main():
    menu()
    
if __name__ == "__main__":
    main()