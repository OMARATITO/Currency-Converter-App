print("======================\nCurrency Converter App\n======================")
name = input("please enter your name: ")
print(f"hello ({name}) welcome to my currency converter app")

the_currency = input("please enter the currency[pound ,dollar ,euro]: ").lower()

if the_currency == "pound":
    while True:
        currency = input("please enter the currency[dollar ,euro ,riyal ,dinar ,aed ,gbp ,cad]: ").lower()
        the_money = float(input("Please enter the money in pound: "))

        if currency == "dollar":
            print(str(the_money / 30.92) + " dollar")
        elif currency == "euro":
            print(str(the_money / 34.12) + " euro")
        elif currency == "riyal":
            print(str(the_money / 8.24) + " riyal")
        elif currency == "dinar":
            print(str(the_money / 100.67) + " dinar")
        elif currency == "aed":
            print(str(the_money / 8.42) + " aed")
        elif currency == "gbp":
            print(str(the_money / 39.77) + " gbp")
        elif currency == "cad":
            print(str(the_money / 23.51) + " cad")
        else:
            print("sorry i cannot convert that currency")
            continue

        answer = input("do you want to change currency again [Yes,No]").lower()
        if answer == "yes":
            continue
        else:
            print("have a nice day :)")
            break

elif the_currency == "dollar":
    while True:
        currency = input("please enter the currency[pound ,euro ,riyal ,dinar ,aed ,gbp ,cad]: ").lower()
        the_money = float(input("Please enter the money in dollar: "))

        if currency == "pound":
            print(str(the_money / 0.032) + " pound")
        elif currency == "euro":
            print(str(the_money / 1.10) + " euro")
        elif currency == "riyal":
            print(str(the_money / 0.27) + " riyal")
        elif currency == "dinar":
            print(str(the_money / 3.25) + " dinar")
        elif currency == "aed":
            print(str(the_money / 0.27) + " aed")
        elif currency == "gbp":
            print(str(the_money / 1.28) + " gbp")
        elif currency == "cad":
            print(str(the_money / 0.75) + " cad")
        else:
            print("sorry i cannot convert that currency")
            continue

        answer = input("do you want to change currency again [Yes,No]").lower()
        if answer == "yes":
            continue
        else:
            print("have a nice day :)")
            break

elif the_currency == "euro":
    while True:
        currency = input("please enter the currency[pound ,dollar ,riyal ,dinar ,aed ,gbp ,cad]: ").lower()
        the_money = float(input("Please enter the money in euro: "))

        if currency == "pound":
            print(str(the_money / 0.030) + " pound")
        elif currency == "dollar":
            print(str(the_money / 0.91) + " dollar")
        elif currency == "riyal":
            print(str(the_money / 0.24) + " riyal")
        elif currency == "dinar":
            print(str(the_money / 2.97) + " dinar")
        elif currency == "aed":
            print(str(the_money / 0.25) + " aed")
        elif currency == "gbp":
            print(str(the_money / 1.16) + " gbp")
        elif currency == "cad":
            print(str(the_money / 0.68) + " cad")
        else:
            print("sorry i cannot convert that currency")
            continue

        answer = input("do you want to change currency again [Yes,No]").lower()
        if answer == "yes":
            continue
        else:
            print("have a nice day :)")
            break

else:
    print("This option is not in the list!")
    quit()
# this is my Currency Converter App