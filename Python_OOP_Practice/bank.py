class BankAccount:
    MAX_DEPOSIT_LIMIT = 5000
    def __init__(self):
        self.name = str(input("Enter Account Holder Name: "))
        self.balance = 0
    

    def deposit(self):
        try:
            deposit_amount = int(input("Enter Amount you want to deposit: "))
            if deposit_amount > self.MAX_DEPOSIT_LIMIT:
                print(f"Can not deposit more than {self.MAX_DEPOSIT_LIMIT} at a time")
            else:
                print("Deposit Successful")
                self.balance += deposit_amount 
        except ValueError:
              print("Invalid input. Please enter a valid Amount.")
              self.deposit()
        self.choice()
    


    def withdraw(self):
        try:
            withdraw_amount = int(input("Enter Amount you want to Withdraw: "))
            if withdraw_amount > self.balance:
                print("Insufficient Balance.")
            elif withdraw_amount < 0:
                print("Invalid amount. Please enter a positive value.")
                self.withdraw()
            else:
                print("Amount Successfully Withdrawn.")
                self.balance -= withdraw_amount
        except ValueError:
             print("Invalid input. Please enter a valid integer.")
             self.withdraw()
        self.choice()



    def get_balance(self):
        if self.balance == 0:
            print("\nAccount Empty!!!!\n")
            self.choice()
        else:
            print(f"Your Account Balance is {self.balance}$") 
            self.choice()
    
    def choice(self):
        print("Enter 1. To check Balance")
        print("Enter 2. To Deposit")
        print("Enter 3. To Withdraw")
        print("Enter 4. To exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            self.get_balance()
        elif choice == 2:
            self.deposit()
        elif choice == 3:
            self.withdraw()
        elif choice == 4:
            print("Have a good day!")
        else:
            print("Invalid choice. Please enter a valid option.")
        

    
account = BankAccount()
account.choice()