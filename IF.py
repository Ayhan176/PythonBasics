tv_available = True
bank_balance = 400.10

price = float(input("Wieviel möchtest du ausgeben?"))
bank_balance = bank_balance - price

if bank_balance> 0:
    print("Kontostand ist positiv!")

else:
    print("Kontostand ist negativ!")
