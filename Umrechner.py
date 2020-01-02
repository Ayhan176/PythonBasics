print("Hallo... Das ist ein Umrechner von Kilometer zu Meilen!")

while True:
    print("Bitte gib eine Kilometerzahl ein, um es in Meilen umrechnen zu lassen!")

    km = input("Kilometer: ")

    km = float(km.replace(",", "."))  # replace comma with dot, if user entered a comma

    miles = km * 0.621371

    print("{0} Kilometers sind {1} Meilen.".format(km, miles))

    choice = input("Möchtest du eine neue Umrechnung starten (j/n): ")

    if choice.lower() != "j" and choice.lower() != "ja":
     break