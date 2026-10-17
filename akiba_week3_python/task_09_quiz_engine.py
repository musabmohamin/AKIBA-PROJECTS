
score = 0
answer = []

def display_question():
    answer = []

    questions = [
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean",
                        "C. Pacific Ocean", "D. Arctic Ocean"]
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"]
        },
        {
            "question": "Who wrote the play Romeo and Juliet?",
            "options": ["A. Charles Dickens", "B. William Shakespeare",
                        "C. Mark Twain", "D. George Orwell"]
        },
        {
            "question": "What is the capital city of Japan?",
            "options": ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok"]
        },
        {
            "question": "How many sides does a hexagon have?",
            "options": ["A. Five", "B. Six", "C. Seven", "D. Eight"]
        }
    ]

    for item in questions:
        print("\n" + item["question"])

        for option in item["options"]:
            print(option)

        user_answer = input("Enter your answer (A, B, C, or D): ").lower()

        while user_answer not in ["a", "b", "c", "d"]:
            print("Invalid option. Please enter A, B, C, or D.")
            user_answer = input("Enter your answer: ").lower()

        answer.append(user_answer)

    return answer


def check_answer(answer):
    correct_answer = ["c", "b", "b", "c", "b"]
    return correct_answer


def update_score(answer):
    correct_answer = check_answer(answer)
    score = 0

    for i in range(len(answer)):
        if answer[i] == correct_answer[i]:
            score += 1

    return score


def main():
    while True:
        answer = display_question()
        score = update_score(answer)
        correct_answer = check_answer(answer)

        number_of_incorrect = len(answer) - score
        number_of_correct = score
        percentage = score / len(answer) * 100

        print("\n===============================")
        print("         QUIZ SUMMARY")
        print("SCORE:", score)
        print("NUMBER OF CORRECT:", number_of_correct)
        print("NUMBER OF INCORRECT:", number_of_incorrect)
        print("TOTAL QUESTIONS:", len(answer))
        print("PERCENTAGE:", percentage, "%")
        print("YOUR ANSWERS:", answer)
        print("CORRECT ANSWERS:", correct_answer)
        print("===============================")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("Thank you for playing!")
            break


main()
