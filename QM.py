def take_quiz(mcqs, short_ques, student_name):
    score = 0
    correct = []
    incorrect = []
    skipped = set()
    answers = {}

    # Combine both MCQs and Short Questions
    all_questions = []

    for mcq in mcqs:
        all_questions.append({
            'type': 'mcq',
            'question': mcq['question'],
            'options': mcq['options'],
            'answer': mcq['answer']
        })

    for question, answer in short_ques:
        all_questions.append({
            'type': 'short',
            'question': question,
            'answer': answer
        })

    total = len(all_questions)
    status = ['Not Attempted'] * total
    index = 0

    while True:
        print("\n--- Quiz Menu ---")
        print(f"Question {index + 1} of {total}")
        print(f"Status: {status[index]}")
        print("1. Answer this question")
        print("2. Skip this question")
        print("3. Go to another question")
        print("4. View attempted/skipped status")
        print("5. Submit quiz\n")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            q = all_questions[index]
            print(f"\nQ{index + 1}. {q['question']}")
            if q['type'] == 'mcq':
                for opt in ['a', 'b', 'c', 'd']:
                    print(f"  {opt.upper()}. {q['options'][opt]}")
                ans = input("Your answer (a/b/c/d): ").strip().lower()
                while ans not in ['a', 'b', 'c', 'd']:
                    ans = input("Invalid input. Enter only a/b/c/d: ").strip().lower()
                answers[index] = ans
                status[index] = 'Attempted'
            else:
                ans = input("Your answer: ").strip()
                while not ans:
                    ans = input("Answer cannot be empty. Please enter your answer: ").strip()
                answers[index] = ans
                status[index] = 'Attempted'

        elif choice == '2':
            print(f"Question {index + 1} skipped.")
            skipped.add(index)
            status[index] = 'Skipped'

        elif choice == '3':
            goto = input(f"Enter question number to go to (1-{total}): ").strip()
            if goto.isdigit() and 1 <= int(goto) <= total:
                index = int(goto) - 1
            else:
                print("Invalid question number.")

        elif choice == '4':
            print("\nQuestion Status:")
            for i, s in enumerate(status):
                print(f"Q{i + 1}: {s}")
        
        elif choice == '5':
            confirm = input("Are you sure you want to submit the quiz? (yes/no): ").strip().lower()
            if confirm == 'yes':
                break
        else:
            print("Invalid option. Please choose again.")

    # Evaluate Answers
    for idx, q in enumerate(all_questions):
        if idx not in answers:
            continue
        user_ans = answers[idx]
        if q['type'] == 'mcq':
            if user_ans == q['answer']:
                score += 1
                correct.append(q['question'])
            else:
                incorrect.append((q['question'], q['answer'].upper(), q['options'][q['answer']]))
        else:
            if user_ans.lower() == q['answer'].lower():
                score += 1
                correct.append(q['question'])
            else:
                incorrect.append((q['question'], q['answer']))
    
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
#turn this into gui
#may be add filing for report that can be sent to the teacher after every body has been quizzed
#make separate panels with passwords for teachers and students so questions cant be accessed
#add an option to edit the question by entering  the question number
#add an option to add a question
#add an option to save the paper for later use in a file or sth




