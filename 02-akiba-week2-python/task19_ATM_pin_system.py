counter = 0
attempt_remaining = 3

while counter < 3:
    pin = int(input("Enter your PIN: "))

    if pin == 1234:
        print("Correct PIN")
        break
    else:
        print("Incorrect PIN")

    counter = counter + 1
    attempt_remaining = attempt_remaining - 1
    print("Attempts remaining:", attempt_remaining)
