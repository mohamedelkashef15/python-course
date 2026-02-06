# Quiz System in Python
questions = [
    {
        "question": "What is the output of 3 + 2 * 2?",
        "options": ["7", "10", "8", "None of the above"],
        "answer": "7"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which of these is a mutable data type?",
        "options": ["tuple", "string", "list", "int"],
        "answer": "list"
    },
    {
        "question": "What does 'len()' function do?",
        "options": ["Returns the number of elements", "Adds elements", "Deletes elements", "None"],
        "answer": "Returns the number of elements"
    }
]

print("Welcome to Python Quiz!\n")
score = 0
try:
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"  {idx}. {option}")

        # Get user input

        while True:
            choice = int(input("\nEnter the option number: "))
            if 1 <= choice <= len(q['options']):
                break
            print("Invalid input! Enter a valid option number.")
        # Check answer
        if q['options'][choice - 1] == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

except ValueError:
    print("Enter a valid number")

print(f"Quiz finished! Your score: {score}/{len(questions)}")
