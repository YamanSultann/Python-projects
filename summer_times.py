season = input("Please enter which season it is: ")
cloth = input("Please enter if you want to wear Winter or Summer clothes: ")

if (season == "summer") or (season == "Summer"):
    if (cloth == "summer") or (cloth == "Summer"):
        print("You may wear as you please!")
    elif (cloth == "winter") or (cloth == "Winter"):
        print("You will feel extremely hot. Not recommended")
elif (season == "winter") or (season == "Winter"):
    if (cloth == "winter") or (cloth == "Winter"):
        print("You may wear as you please!")
    elif (cloth == "summer") or (cloth == "Summer"):
        print("You will feel too cold. Not recommended")