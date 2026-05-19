# if else basico
num1 = 1
num2 = 2

if num1 > num2:
    print("num1 es mayor que num2")
else:
    print("num1 es menor o igual que num2")

# if else con elif
if num1 > num2:
    print("num1 es mayor que num2")
elif num1 < num2:
    print("num1 es menor que num2")
else:
    print("num1 es igual a num2")

# using if-else statements to check multiple conditions
age = 25
if age < 18:
    print("You are a minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# ternary operator
age = 65
is_adult = "Yes" if age >= 18 else "No"

# matching multiple conditions with if-elif-else
match age:
    case age if age < 18:
        print("You are a minor.")
    case age if 18 <= age < 65:
        print("You are an adult.")
    case _:
        print("You are a senior citizen.")
