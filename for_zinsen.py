bank_account = "Ayhan"
bank_balance = 2000
interest = 1.5
year = 2019

for x in range(25):
    bank_balance = bank_balance + bank_balance * (interest / 100)
    year = year + 1
    print(str(year) + " Neuer Kontostand: " + str(bank_balance))