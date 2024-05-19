import math


while True:
    thing = input("What would you like to convert? If unsure please type 'help': ")

    # Need better name for the input :(
    if thing == "help":
        # Note: Add Exchange Rate API if available !!!

        print("----------")
        print("Please enter a subject from the list below!")
        print("Conversion-Subjects: mass, length, temperature, currency, tbc ")
        print("Shape-Subjects: rectangle, square, circle, triangle, tbc ")
        print("----------")
        subject = input("Please enter a subject for further commands: ")
        if subject == "mass" or subject == "Mass":
            print("The available mass conversions are:")
            print("'g to kg' & vice versa")
            print("'kg to t' & vice versa")
            continue
        elif subject == "length" or subject == "Length":
            print("The available length conversions are:")
            print("'m to km' & vice versa")
            print("'km to miles' & vice versa")
            continue
        elif subject == "temperature" or subject == "temp" or subject == "Temp" or subject == "Temperature":
            print("The available temperature conversions are:")
            print("'celsius to kelvin' or 'c to k' & vice versa")
            print("'fahrenheit to kelvin' or 'f to k' & vice versa")
            print("'celsius to fahrenheit' or 'c to f' & vice versa")
            continue
        elif subject == "currency conversion" or subject == "currency" or subject == "Currency":
            print("Subject to change due to realtime value adjustments")
            print("The available currency conversions are:")
            print("'euro to dollar' & vice versa")
            continue
        elif subject == "Triangle" or subject == "triangle":
            print("The available tools for triangles are:")
            print("'area of triangle'")
            continue
        elif subject == "Circle" or subject == "circle":
            print("The available tools for circles are:")
            print("'xxx'")
            continue
        elif subject == "Rectangle" or subject == "rectangle":
            print("The available tools for rectangles are:")
            print("'xxx'")
            continue
        elif subject == "Square" or subject == "square":
            print("The available tools for squares are:")
            print("'xxx'")
            continue
        else:
            print("Please enter a valid subject!")
            continue

    # LENGTH
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

    elif thing == "m to cm":
        m = float(input("How many m? "))
        cm = m * 100
        r_cm = round(cm, 2)
        print(m, "m =", r_cm, "cm")

    elif thing == "cm to m":
        cm = float(input("How many cm? "))
        m = cm / 100
        r_m = round(m, 2)
        print(cm, "cm =", r_m, "m")

    # MASS
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

    # CURRENCY - NEED API (16.05.2025)
    elif thing == "euro to dollar":
        euro = float(input("How many €? "))
        dollar = euro * 1.09
        r_dollar = round(dollar, 2)
        print(euro, "€ =", r_dollar, "$")

    elif thing == "dollar to euro":
        dollar = float(input("How many $? "))
        euro = dollar / 1.09
        r_euro = round(euro, 2)
        print(dollar, "$ =", r_euro, "€")

    # CIRCLES
    elif thing == "circumference circle":
        U = float(input("Whats the diameter (cm)? "))
        d = U / math.pi
        d_round = round(d, 2)
        print("The circle has a circumference of", d_round,"cm")

    # TRIANGLES
    # TEST-CODE not fully tested yet!
    elif thing == "area of triangle":
        try:
            s_a = float(input("Enter side a (cm): "))
            s_b = float(input("Enter side b (cm): "))
            s_c = float(input("Enter side c (cm): "))

            # Test if shape == triangle
            if s_a + s_b > s_c and s_a + s_c > s_b and s_b + s_c > s_a:
                s = (s_a + s_b + s_c) / 2
                area = math.sqrt(s * (s - s_a) * (s - s_b) * (s - s_c))
                a_rou = round(area, 2)
                # Print the area
                print("The area (A) of the triangle is:", a_rou, "square cm")
            else:
                print("Entered sides DON'T form a triangle!")
        except ValueError:
            print("Invalid input!")

    # TEMPERATURE
    elif thing == "celsius to kelvin" or thing == "c to k":
        celsius = float(input("How many °Celsius? "))
        kelvin = celsius + 273.15
        r_kelvin = round(kelvin, 3)
        print(celsius, "°Celsius =", r_kelvin, "°Kelvin")

    elif thing == "kelvin to celsius" or thing == "k to c":
        kelvin = float(input("How many °Kelvin? "))
        celsius = kelvin - 273.15
        r_celsius = round(celsius, 3)
        print(kelvin, "°Kelvin =", r_celsius, "°Celsius")

    elif thing == "celsius to fahrenheit" or thing == "c to f":
        celsius = float(input("How many °Celsius? "))
        fahrenheit = (celsius * 9/5) + 23
        r_fahrenheit = round(fahrenheit, 3)
        print(celsius, "°Celsius =", r_fahrenheit, "°Fahrenheit")

    elif thing == "fahrenheit to celsius" or thing == "f to c":
        fahrenheit = float(input("How many °Fahrenheit? "))
        celsius =  (fahrenheit - 32) * 5/9
        r_celsius = round(celsius, 3)
        print(fahrenheit, "°Fahrenheit =", r_celsius, "°Celsius")

    elif thing == "fahrenheit to kelvin" or thing == "f to k":
        fahrenheit = float(input("How many °Fahrenheit? "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        r_kelvin = round(kelvin, 3)
        print(fahrenheit, "°Fahrenheit =", r_kelvin, "°Kelvin")

    elif thing == "kelvin to fahrenheit" or thing == "k to f":
        kelvin = float(input("How many °Kelvin? "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        r_fahrenheit = round(fahrenheit, 3)
        print(kelvin, "°Kelvin =", r_fahrenheit)

    else:
        print("Please enter a valid command!")

    restart = input("Restart? (y/n): ")
    if restart.lower() != "yes" and restart.lower() != "y":
        print("Goodbye.")
        break
