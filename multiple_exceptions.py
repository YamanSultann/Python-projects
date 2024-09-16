try:
    num1, num2 = eval(input("Enter 2 numbers with a comma in between: "))
    result = num1/num2
    print("The division of the numbers are", result)

except ZeroDivisionError:
    print("Division by zero is error")

except SyntaxError:
    print("Comma is missing, make sure to write it like 1,2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")