# List of quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["1. Paris", "2. London", "3. Rome", "4. Berlin"],
        "correct_answer": 1
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["1. Hydrogen", "2. Oxygen", "3. Nitrogen", "4. Helium"],
        "correct_answer": 2
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["1. Charles Dickens", "2. Mark Twain", "3. William Shakespeare", "4. J.K. Rowling"],
        "correct_answer": 3
    }
]

# Welcome Message
def display_welcome():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple choice questions.")
    print("Select the correct answer by entering the corresponding number.\n")

# Present the quiz questions
def present_quiz_questions():
    user_score = 0
    for i, question in enumerate(quiz_questions):
        print(f"Question {i + 1}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        user_answer = int(input("Enter the number of your answer: "))
        user_score = evaluate_answer(question, user_answer, user_score)
    return user_score

# Evaluate the user's answer
def evaluate_answer(question, user_answer, score):
    if user_answer == question['correct_answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {question['correct_answer']}.\n")
    return score

# Display final score and results
def display_final_results(score):
    print(f"Your final score is {score}/{len(quiz_questions)}.")
    print("Thanks for playing!")

# Play again prompt
def play_again():
    response = input("Do you want to play again? (yes/no): ").lower()
    if response == 'yes':
        start_quiz_game()
    else:
        print("Goodbye!")

# Main function to start the quiz game
def start_quiz_game():
    display_welcome()
    final_score = present_quiz_questions()
    display_final_results(final_score)
    play_again()

# Start the game
if __name__ == "__main__":
    start_quiz_game()
