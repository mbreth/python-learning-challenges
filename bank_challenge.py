balance = 500.00

choices = ["1. Check balance", "2. Deposit money", "3. Withdraw money", "4. Exit"]

for choice in choices:
  print(choice)
  
user_input = 0

def check_balance():
  print(f"Current balance: ${balance:.2f}")

def deposit(balance):
  dep_ammount = float(input("How much would you like to deposit?: "))
  if dep_ammount <= 0:
    print("Not a valid ammount!")
  else:
    balance += dep_ammount
  return balance

def withdraw(balance):
  withdraw_ammount = float(input("How much would you like to withdraw?: "))
  if withdraw_ammount > balance:
    print("You cant withdraw that much!")
  elif withdraw_ammount <= 0:
    print("Not a valid ammount!")
  else:
    balance -= withdraw_ammount
  return balance

while user_input != 4:
  print("Please select an option: ")
  user_input = int(input())
  if user_input == 1:
    check_balance()
  elif user_input == 2:
    balance = deposit(balance)
    print(f"Current balance: ${balance:.2f}")
  elif user_input == 3:
    balance = withdraw(balance)
    print(f"Current balance: ${balance:.2f}")
  elif user_input > 4:
    print("Not a valid input!")
    
print("Thanks for banking with us!")
    
