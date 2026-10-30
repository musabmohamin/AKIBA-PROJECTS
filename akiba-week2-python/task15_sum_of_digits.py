number = int(input("Enter a number:"))
total = 0

while number > 0:
    digit = number % 10
    # Add digit to total
    # Remove the last digit from number
    total += digit
    number //= 10

print("The sum of the digits is", total)