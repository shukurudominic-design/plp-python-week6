balance = 1000
correct_pin = 1234

pin = int(input("Enter your 4-digit PIN: "))

# Check whether the PIN entered by the user is correct.
if pin == correct_pin:
    amount = int(input("Enter amount to withdraw: "))

    # Check whether the withdrawal amount is within the available balance.
    if amount <= balance:
        balance = balance - amount
        print(f"Withdrawal successful. New balance: {balance}")
    else:
        print("Insufficient funds")
else:
    # The PIN is incorrect, so the program stops without asking for a withdrawal.
    print("Incorrect PIN")