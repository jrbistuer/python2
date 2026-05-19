my_list: list[int] = [1, 2, 3, 4, 5]

for num in my_list:
    print(num)  # Printing the current number in the loop

for i in range(5):
    print(i)  # Printing the current index in the loop

for i in range(3, 6):
    print(i)  # Printing the current index in the loop

for i in range(0, 10, 2):
    print(i)  # Printing the current index in the loop

suma: int = 0
for i in range(1, 6, 2):
    suma += i
print(suma)  # Printing the sum of odd numbers from 1 to 5

days: list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    print(day)  # Printing the current day in the loop

for index, day in enumerate(days):
    # Printing the index and the current day in the loop
    print(f"Day {index + 1}: {day}")

# While
# The difference between for and while loops is that for loops are used when you know the number
# of iterations in advance, while while loops are used when you want to repeat a block of code until a certain condition is met.
count = 0
while count < 5:
    print(count)  # Printing the current count in the loop
    count += 1  # Incrementing the count by 1

count = 0
while count >= 0:
    print(count)  # Printing the current count in the loop
    count += 1  # Incrementing the count by 1
    if count == 5:
        break  # Breaking the loop when count reaches 5
