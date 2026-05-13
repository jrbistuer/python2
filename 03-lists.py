"""
Lists in Python
LISTS
SETS
TUPLES"""

"""
LISTS in Python are ordered, mutable, and allow duplicate elements, and different data types.
They are defined using square brackets []."""
my_list: list = [1, "hello", 3.14, True, [1, 2, 3]]
print(my_list)
print(my_list[0])  # Accessing the first element
print(my_list[1])  # Accessing the second element
# print(my_list[10])  # This will raise an IndexError ERROR
print(my_list[-1])  # Accessing the last element
print(my_list[-2])  # Accessing the second to last element
my_list_of_strings: list[str] = ["apple", "banana", "cherry"]

# Modifying a list
my_list[0] = 42  # Changing the first element to 42
print(my_list)
my_list.append("new element")  # Adding a new element to the end of the list
print(my_list)
my_list.insert(2, "inserted element in index 2")  # Inserting an element at index 2
print(my_list)
my_list.remove("hello")  # Removing the element "hello"
print(my_list)
# my_list.remove(132234234)  # This will raise a ValueError ERROR because the element is not in the list
my_list.pop()  # Removing the last element
print(my_list)
my_list.pop(2)  # Removing the element at index 2
print(my_list)

my_list2 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1]
print(my_list2)
my_list2.sort()  # Sorting the list in ascending order
print(my_list2)

print(my_list2.count(1))  # Counting how many times the element 1 appears in the list
print(my_list2.count(4))  # Counting how many times the element 4 appears

print(len(my_list2))  # Getting the length of the list
print(len(my_list))  # Getting the length of the list

print(1 in my_list2)  # Checking if the element 1 is in the list
print(10 in my_list2)  # Checking if the element 10 is in the list

for element in my_list:  # Iterating over the list
    print(element)

# unpacking a list
print(len(my_list))
a, b, c, d = my_list # Unpacking
print(a)
print(b)
print(c)
print(d)
a, b = my_list[0], my_list[1] # Unpacking only the first two elements
print(a)
print(b)
a, *rest = my_list # Unpacking the first element and the rest of the list
print(a)
print(rest)

"""
SETS in Python are unordered, mutable, and do not allow duplicate elements. They are defined using curly braces {}."""
my_set: set = {1, 1, 1, 2, 2, 3, 7, 6, 5, 5, 5, 4, 23, 65, 12, 1, 1, 1, 1, 1, 1, 1}
print(my_set)  # Duplicates are removed and the order is not guaranteed
print(len(my_set))  # Getting the length of the set
my_set.add(1)  # Adding an element to the set (if it already exists, it will not be added again)
print(my_set)
my_set.remove(2)  # Removing an element from the set
print(my_set)
my_set.remove(1)
print(my_set)
# my_set.remove(1)
my_set.discard(1)  # Removing an element from the set (if it does not exist, it will not raise an error)
print(my_set)
my_set.clear()  # Removing all elements from the set
print(my_set)
my_set.add(1)
my_set.update({2, 3, 4})  # Adding multiple elements to the set
print(my_set)

for element in my_set:  # Iterating over the set
    print(element)

"""TUPLES in Python are ordered, immutable, and allow duplicate elements, and different data types.
They are defined using parentheses (). The difference between a list and a tuple is that a tuple 
cannot be modified after it is created, while a list can be modified."""
my_tuple: tuple = (1, "hello", 3.14, True, [1, 2, 3])
print(my_tuple)
my_tuple_of_strings: tuple[str, ...] = ("apple", "banana", "cherry")
print(my_tuple_of_strings)
print(my_tuple_of_strings[0])  # Accessing the first element
# my_tuple_of_strings[0] = "grape"  # This will raise a TypeError ERROR because tuples are immutable
my_tuple_of_int = (1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1)
print(my_tuple_of_int)
# my_tuple_of_int[0] = 10  # This will raise a TypeError ERROR because tuples are immutable

# unpacking a tuple
a, b, c = my_tuple_of_strings # Unpacking
print(a)
print(b)
print(c)
a, *rest = my_tuple_of_strings # Unpacking the first element and the rest of the tuple
print(a)
print(rest)