# The Spending Tracker
The Spending Tracker allows users to record and display expenses and incomes. This is the product for the CS50P final project. 

## Requirement
To compile the program, two libraries are needed to install. They are pandas and maskpass.
1. Install pandas with the command: **pip install pandas**
2. Install maskpass with the command: **sudo pip3 install maskpass**

## How to use
You will see the below menu after compiling the program.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/2fe63aae-2087-4666-b661-b064f94240c4">

### Sign-up for an account 
Input 2 after seeing the prompt shown in above. Afterwards, you will proceed to the following menu. Follow the requirements to create an account.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/69027313-7771-4be0-961a-0f378694cb02">

### Log-into an account
If 1 is inputted, enter your username and password. If they are all correct, the below menu will be shown.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/ac1113f0-5962-49c7-ac5c-6cee053136cf">

### The Main Menu
Below is the main menu for the system, the menu will be shown after logging into the system.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/df9d9aa3-f5dd-4410-96ff-439ab7774eca">

### The balance menu
The balance menu will be shown after inputting 1 from the main menu.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/d8e3b161-802a-41ce-bcf9-98fb272195ce">

### The record menu
The record menu will be shown after inputting 2 from the main menu.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/cf50668b-8727-4af6-931f-f2df46c9271e">

### The adjust menu
The adjust menu will be shown after inputting 3 from the main menu.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/b100e1c8-28f1-4303-9970-2a49a6713e8a">

### The display menu
The display menu will be shown after inputting 4 from the main menu.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/a43abb95-a799-4c18-a4d6-1f95fcf29caf">

### To quit the program
Input 5 from the main menu. The below message will be shown and the program will be terminated.

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/1779c095-179d-4d75-9ad3-872759f9caa7">

### Initial an payment account and balance
After inputting 1 from the balance menu, you will be prompted to enter a line in the format of **payment_account amount** e.g. **cash 2000**

<img width="281" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/480de314-9e2b-4bc6-aa96-28bac0e4046b">


Afterwards, you will be prompted to enter "y" to continue enter the payment account details or "n" to go back to the balance menu.

<img width="86" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/82191c4e-9123-48be-8c56-56a77512484b">

### Delete an payment account from the system
After inputting 2 from the balance menu, the account stored in the program will be listed. You are requested to input the index of the payment account that you want to delete. 

<img width="275" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/ed9586a3-52b7-42d3-9246-788f3440353b">

Afterwards, you will be prompted to input either "y" to confirm the deletion of payment account or "n" to cancel the delete operation.

<img width="266" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/8d1753a5-c35c-490e-8bfe-834f47f6aa9c">

### Insert records into the system
Input 1 from the record menu to record the spendings of today.
Input 2 from the record menu to record the spendings of specify date. The date will be prompted for user to input. Please input in the format of **YYYY-MM-DD** for example, 2023-09-24 means 24th September, 2023.

Afterwards, users will be prompted to input the record in the format of **category amount payment_account type** for example, **food 100 cash e**.

<img width="433" alt="image" src="https://github.com/JimmyLam0215/CS50P-Final-Project/assets/117706705/da66468e-8c63-4aeb-af88-c203dfd3d0fd">




