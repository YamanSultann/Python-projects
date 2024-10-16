age = input("Enter your age without a decimal place: ")
has_alpha = False
has_num = False

for char in age:
    if char.isalpha():
        has_alpha = True
    elif char.isdigit():
        has_num = True
    if has_alpha and has_num:
        break

if has_alpha and has_num:
    print("Please remove any alphabet from your age.")
elif has_alpha:
    print("Please write a proper number for your age.")
elif has_num:
    age = int(age)
    if age % 2 == 0:
        print("You are",age,"years old and your age is an even number")
    else:
        print("You are",age,"years old and your age is an odd number")
else:
    print("Please enter your age first.")