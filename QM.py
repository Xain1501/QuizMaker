def take_quiz(mcqs, short_ques, student_name):
    score = 0
    correct = []
    incorrect = []

    print("\n--- Quiz Started ---\n")

    # MCQ Section
    if mcqs:
        print("--- Multiple Choice Questions ---\n")
        for idx, mcq in enumerate(mcqs):
            print(f"Q{idx + 1}. {mcq['question']}")
            for option in ['a', 'b', 'c', 'd']:
                print(f"  {option.upper()}. {mcq['options'][option]}")
            ans = input("Your answer (a/b/c/d): ").strip().lower()
            while ans not in ['a', 'b', 'c', 'd']:
                ans = input("Invalid input. Enter only a/b/c/d: ").strip().lower()

            if ans == mcq['answer']:
                score += 1
                correct.append(mcq['question'])
            else:
                incorrect.append((mcq['question'], mcq['answer'].upper(), mcq['options'][mcq['answer']]))
            print()

    # Short Question Section
    if short_ques:
        print("--- Short Answer Questions ---\n")
        for idx, (question, answer) in enumerate(short_ques):
            print(f"Q{idx + 1 + len(mcqs)}. {question}")
            ans = input("Your answer: ").strip()
            while not ans:
                ans = input("Answer cannot be empty. Please enter your answer: ").strip()

            if ans.lower() == answer.lower():
                score += 1
                correct.append(question)
            else:
                incorrect.append((question, answer))
            print()

    print("--- Quiz Ended ---\n")
    return score, correct, incorrect


def calculate_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90:
        return "A+", percentage
    elif percentage >= 80:
        return "A", percentage
    elif percentage >= 70:
        return "B", percentage
    elif percentage >= 60:
        return "C", percentage
    elif percentage >= 50:
        return "D", percentage
    else:
        return "E (Fail)", percentage


print("--------------------------------------------------")
print("           Welcome to Zain Quizzes!")
print("--------------------------------------------------\n")

quiz_title = input("Enter a title for your quiz (type 'skip' to leave it blank): ").strip()
if quiz_title.lower() == "skip":
    quiz_title = ""

quiz_description = input("Enter a short description or instructions for the quiz (type 'skip' to leave it blank): ").strip()
if quiz_description.lower() == "skip":
    quiz_description = ""

# Get number of MCQs and short-answer questions
print("\nLet's create your quiz.\n")
max_total_questions = 100

while True:
    mcq_input = input(f"Enter number of MCQs (0 to skip, max total questions: {max_total_questions}): ").strip()
    short_input = input("Enter number of short-answer questions (0 to skip): ").strip()

    if not mcq_input.isdigit() or not short_input.isdigit():
        print("Both values must be non-negative numbers. Please try again.\n")
        continue

    mcq_count = int(mcq_input)
    short_count = int(short_input)

    if mcq_count % 5 != 0 or short_count % 5 != 0:
        print("Please enter questions in multiples of 5 (e.g., 0, 5, 10, ...).\n")
        continue

    total_questions = mcq_count + short_count
    if total_questions == 0:
        print("You must have at least one question.\n")
    elif total_questions > max_total_questions:
        print(f"Total questions exceed limit of {max_total_questions}. Please try again.\n")
    else:
        break

# Enter MCQs
mcqs = []
if mcq_count > 0:
    print("\n--- Enter Your MCQs ---\n")
    for i in range(mcq_count):
        print(f"MCQ {i + 1}")
        question = input("Enter the question: ").strip()
        while not question:
            question = input("Question cannot be empty. Please enter again: ").strip()

        options = {}
        for opt in ['a', 'b', 'c', 'd']:
            val = input(f"Enter option {opt.upper()}: ").strip()
            while not val:
                val = input(f"Option {opt.upper()} cannot be empty: ").strip()
            options[opt] = val

        answer = input("Enter the correct option (a/b/c/d): ").strip().lower()
        while answer not in ['a', 'b', 'c', 'd']:
            answer = input("Invalid input. Enter only a/b/c/d: ").strip().lower()

        mcqs.append({'question': question, 'options': options, 'answer': answer})
        print()

# Enter Short Questions
short_ques = []
if short_count > 0:
    print("\n--- Enter Your Short Answer Questions ---\n")
    for i in range(short_count):
        question = input(f"Enter short question {i + 1}: ").strip()
        while not question:
            question = input("Question cannot be empty. Please enter again: ").strip()

        answer = input("Enter answer: ").strip()
        while not answer:
            answer = input("Answer cannot be empty. Please enter again: ").strip()

        short_ques.append((question, answer))
        print()

print("\n--- Quiz Setup Complete ---\n")

# Number of students
StudNum = input("Enter the number of students taking this quiz: ").strip()
while not StudNum.isdigit() or int(StudNum) <= 0:
    StudNum = input("Invalid input. Please enter a valid number of students: ").strip()
StudNum = int(StudNum)

# Begin Quiz
print("\n--- Quiz Begins Now ---\n")

for _ in range(StudNum):
    print("--------------------------------------------------")
    name = input("Enter your name: ").strip()
    while not name:
        name = input("Name cannot be empty. Please enter your name: ").strip()

    print("--------------------------------------------------")
    if quiz_title:
        print(f"Quiz Title: {quiz_title}")
    if quiz_description:
        print(f"About This Quiz: {quiz_description}")
    print(f"\nHello, {name}! Get ready to begin.\n")

    score, correct, incorrect = take_quiz(mcqs, short_ques, name)
    grade, percent = calculate_grade(score, len(mcqs) + len(short_ques))

    print("--------------------------------------------------")
    print(f"Result for {name}")
    print(f"Score: {score}/{len(mcqs) + len(short_ques)}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Grade: {grade}")
    print("\nCorrectly Answered Questions:")
    for q in correct:
        print(f"✓ {q}")

    print("\nIncorrectly Answered Questions:")
    for entry in incorrect:
        if isinstance(entry, tuple) and len(entry) == 3:
            print(f"✗ {entry[0]} (Correct: {entry[1]}. {entry[2]})")
        else:
            print(f"✗ {entry[0]} (Correct: {entry[1]})")
    print("--------------------------------------------------\n")

print("Thank you for using Zain Quizzes!")


#  figure out a ways to like make an admin screen and student screen so the student just cant scroll up and answer the stuff from there ony 
# add an option for children to skip the question or move fwd and backward to and fro so they can jump to some questions 
# tell them which questions would they like to attempt every turn they get 
# can also add an option to time the children and end the quiz if the time limit exceeds find out the current time and tell them what time its is and how much time they got
