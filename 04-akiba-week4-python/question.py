
# Akiba Technologies - Week 4
# Mutability, References and Memory Model
# Student: Musab Moahmmedamin


# Question 1: Mutable and Immutable Objects

print("=" * 50)
print("Question 1: Mutable and Immutable Objects")
print("=" * 50)

# A list can be changed after it is created.
fruits = ["apple", "banana", "orange"]

print("Original list:", fruits)

fruits[0] = "mango"

print("Modified list:", fruits)

# A string cannot be changed character by character.
word = "hello"

print("\nOriginal string:", word)

try:
    word[0] = "H"
except TypeError:
    print("A string cannot be changed like a list.")

# We can make a new string instead.
word = "H" + word[1:]

print("New string:", word)


# Question 2: References and Object Identity

print("\n" + "=" * 50)
print("Question 2: References and Object Identity")
print("=" * 50)

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)

# a and b refer to the same list.
# c is another list with the same values.
# is checks identity, while == checks values.


# Question 3: Shared References and Side Effects


print("Question 3: Shared References")


numbers = [1, 2, 3]
values = numbers

values.append(4)

print("Numbers:", numbers)
print("Values:", values)

# Both variables refer to the same list.
# Using copy() makes a separate list.

numbers = [1, 2, 3]
values = numbers.copy()

values.append(4)

print("\nAfter copying:")
print("Numbers:", numbers)
print("Values:", values)


# Question 4: Function Arguments and Mutability

print("\n" + "=" * 50)
print("Question 4: Function Arguments")
print("=" * 50)


def update_list(items):
    items.append(100)


scores = [50, 60, 70]

update_list(scores)

print("Scores after function call:", scores)


# This function makes a copy before adding a new value.
def create_updated_copy(items):
    new_items = items.copy()
    new_items.append(100)
    return new_items


scores = [50, 60, 70]
new_scores = create_updated_copy(scores)

print("Original scores:", scores)
print("New scores:", new_scores)


# Question 5: Memory Management and Garbage Collection

print("\n" + "=" * 50)
print("Question 5: Memory Management")
print("=" * 50)

numbers = [10, 20, 30]
other_numbers = numbers

print("Numbers:", numbers)
print("Other numbers:", other_numbers)
print("Same object:", numbers is other_numbers)

# Delete one variable.
del numbers

# The list is still available through other_numbers.
print("\nAfter deleting numbers:")
print("Other numbers:", other_numbers)

# Delete the remaining variable.
del other_numbers

print("\nBoth variable names have been deleted.")
print("If no other references exist, the list can be removed")
print("from memory by Python.")

# Python manages memory automatically.
# del removes a variable name, but does not always destroy
# the object because another reference may still exist.


print("\nAll questions completed.")
