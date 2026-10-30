
scores = []

def validate(score):
    return 0 <= score <= 100

def calculate_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    if score >= 60:
        status = "Pass"
    else:
        status = "Fail"

    return grade, status


def calculate_average(scores):
    if len(scores) == 0:
        return None

    total = 0

    for student in scores:
        total += student[3]

    average = total / len(scores)
    return average

def highest_lowest(scores):
    if len(scores) == 0:
        return None, None

    highest = scores[0][3]
    lowest = scores[0][3]

    for student in scores:
        if student[3] > highest:
            highest = student[3]

        if student[3] < lowest:
            lowest = student[3]

    return highest, lowest

def count_pass_fail(scores):
    count_pass = 0
    count_fail = 0

    for student in scores:
        if student[3] >= 60:
            count_pass += 1
        else:
            count_fail += 1

    return count_pass, count_fail


while True:
    name = input("Enter the name of the student:")
                 
    while True:
            score = int(input(f"Enter the score of {name}: "))

            if validate(score):
                break
            else:
                print("Invalid score! Enter a score from 0 to 100.")

        

    scores.append(["name", name, "score", score])

    add_student = ("Enter 1 to add another student or 0 to finish: ")
    

    while add_student not in ("0", "1"):
        add_student = input("Enter only 1 or 0: ")

    if add_student == "0":
        break


if len(scores) == 0:
    print("No student records available.")

else:
    print("\n========== STUDENT REPORT ==========")

    for student in scores:
        name = student[1]
        score = student[3]
        grade, status = calculate_grade(score)

        print(f"Name: {name}")
        print(f"Score: {score}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")
        print("------------------------------------")

    average = calculate_average(scores)
    highest, lowest = highest_lowest(scores)
    count_pass, count_fail = count_pass_fail(scores)

    print("\n========== CLASS SUMMARY ==========")
    print(f"Total students: {len(scores)}")
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Passed students: {count_pass}")
    print(f"Failed students: {count_fail}")
    print("====================================")
