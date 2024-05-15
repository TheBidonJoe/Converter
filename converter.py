while True:

    print("All commands can be found by typing: 'help'")
    thing = input("What would you like to convert? ")

    if thing == "help":
        print("All available commands are:")
        print("'km to miles' or 'miles to km'")
        print("'kg to g' or 'g to kg'")
        print("'kg to t' or 't to kg'")
        print("'euros to dollars' or 'dollars to euros'")

    elif thing == "miles to km":
        miles = float(input("How many miles? "))
        km = float(miles) * 1.609
        r_km = round(km, 2)
        print(miles, "Miles =", r_km, "km")

    elif thing == "km to miles":
        km = float(input("How many km? "))
        miles = float(km) / 1.609
        r_miles = round(miles, 2)
        print(km, "km =", r_miles, "miles")

    elif thing == "kg to g":
        kg = float(input("How many kg? "))
        gram = float(kg) * 1000
        r_g = round(gram, 2)
        print(kg, "kg =", r_g, "gram")

    elif thing == "g to kg":
        g = float(input("How many g? "))
        kg = float(g) / 1000
        r_kg = round(kg, 2)
        print(g, "g =", r_kg, "kg")


    elif thing == "euros to dollars":
        euro = float(input("How many €? "))
        dollar = euro * 1.09
        r_dollar = round(dollar, 2)
        print(euro, "€ =", r_dollar, "$")

    elif thing == "dollars to euros":
        dollar = float(input("How many $? "))
        euro = dollar / 1.09
        r_euro = round(euro, 2)
        print(dollar, "$ =", r_euro, "€")

    elif thing == "kg to t":
        kg = float(input("How many kg? "))
        t = kg / 1000
        r_t = round(t, 2)
        print(kg, "kg =", r_t, "t")

    elif thing == "t to kg":
        t = float(input("How many tons? "))
        kg = t * 1000
        r_kg = round(kg, 3)
        print(t, "t =", r_kg, "kg")

    else:
        print("Please enter a valid command!")

    restart = input("Restart? (y/n): ")
    if restart.lower() != "yes" and restart.lower() != "y":
        print("Goodbye.")
        break


