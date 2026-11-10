try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError:
    print("Please enter a valid numerical age.")

else:
    print("Your age is:", age)
    print("Age entered successfully!")
    