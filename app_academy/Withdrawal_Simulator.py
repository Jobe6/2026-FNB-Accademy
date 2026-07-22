bank_balance = 500
Withdrwal_Amount = float(input("How much do you want to WITHDRAW!!??? : "))


if Withdrwal_Amount <= 0:
    print(f"Invalid amount!!!." +" You must withdraw more that R" + str(Withdrwal_Amount))
elif Withdrwal_Amount <= bank_balance:
    Remaining_balance = bank_balance - Withdrwal_Amount
    round(Remaining_balance, 2)
    print(f"Withdrawal successful! Remaining Balance is R" + str(Remaining_balance))
else:
    print("Declined. Insufficient funds!!")
    