number=int(input("Enter the number:"))
if number==0 or number==1:
    print("The number you entered is not a prime number")
 # We check divisors only up to the square root because
# any larger divisor has a matching smaller divisor.
# We add 1 because range() excludes its ending value.
for i in range(2,(number**0.5) + 1):
    if number%i==0:
        print("The number you entered is not a prime number")
        break
    else:
        print("The number you entered is a prime number")
        