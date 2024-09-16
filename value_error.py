try:
    number = int(input("Enter a number: "))
    print("The number is", number)
except ValueError as t:
    print("Exception", t)