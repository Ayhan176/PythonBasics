price = 490


while True:

    discount_input = input("Wie hoch ist der Rabatt?: (in Prozent)")

    discount = price / 100 * float(discount_input)

    price = price - discount

    text = "Dein finaler Preislautet: "

    print(text + str(price))