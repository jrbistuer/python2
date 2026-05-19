like_coffe: bool = True
like_tea: bool = False
print(like_coffe)  # Printing the value of like_coffe
print(like_tea)  # Printing the value of like_tea

# greater than
num1 = 5
num2 = 10
print(num1 > num2)  # Printing the result of the comparison
# less than
print(num1 < num2)  # Printing the result of the comparison
# equal to
print(num1 == num2)  # Printing the result of the comparison
# not equal to
print(num1 != num2)  # Printing the result of the comparison
# greater than or equal to
print(num1 >= num2)  # Printing the result of the comparison
# less than or equal to
print(num1 <= num2)  # Printing the result of the comparison

# logical operators
is_raining = True
is_cold = False
print(is_raining and is_cold)  # Printing the result of the logical AND operation
print(is_raining or is_cold)  # Printing the result of the logical OR operation
print(not is_raining)  # Printing the result of the logical NOT operation

print("Do you like coffee? " + str(like_coffe))  # Printing a message with the value of like_coffe
print("Do you like tea? " + str(like_tea))  # Printing a message with the value of like_tea
print("Do you love coffee and tea? " + str(like_coffe and like_tea))  # Printing a message with the result of the logical AND operation
print("Do you like coffe but not tea? " + str(like_coffe and not like_tea))  # Printing a message with the result of the logical AND and NOT operations
