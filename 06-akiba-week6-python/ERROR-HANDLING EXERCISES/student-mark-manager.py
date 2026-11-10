try:
    name = input("Enter student name: ")
    mark = int(input("Enter student mark: "))

    if mark < 0 or mark > 100:
        raise ValueError

except ValueError :
    print("Error: Student mark must be between 0 and 100")

else:
    print("Student name:", name)
    print("Student mark:", mark)