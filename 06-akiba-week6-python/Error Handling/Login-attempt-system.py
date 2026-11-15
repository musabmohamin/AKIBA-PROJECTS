users = [
    {"username": "musab", "password": "python"},
    {"username": "ahmed", "password": "1234"},
    {"username": "ali", "password": "abc123"}
]

username = input("Enter username: ")
password = input("Enter password: ")

try:
    user_found = False

    for user in users:
        if user["username"] == username:
            user_found = True

            if user["password"] == password:
                print("Login successful!")
            else:
                raise ValueError("Incorrect password!")

            break

    if not user_found:
        raise LookupError("Username does not exist!")

except ValueError as error:
    print(f"Login error: {error}")

except LookupError as error:
    print(f"Login error: {error}")