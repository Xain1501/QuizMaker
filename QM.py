def Take(ques, ans, num):
    score = 0
    print("\n--- Quiz Started ---\n")
    for index in range(num):
        print(f"Q{index + 1}. {ques[index]}")
        studAns = input("Your Answer: ").strip()
        while not studAns:
            studAns = input("Answer cannot be empty. Please enter your answer: ").strip()

        if studAns.lower() == ans[index].lower():
            score += 1
            print("✓ Correct\n")
        else:
            print("✗ Incorrect\n")
    print("--- Quiz Ended ---\n")
    return score

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

print("\nLet's create your quiz.\n")
numQ = input("Enter the number of questions (must be a multiple of 5 and less than 100, e.g., 5, 10, 15...95): ").strip()
while not numQ.isdigit() or int(numQ) <= 0 or int(numQ) >= 100 or int(numQ) % 5 != 0:
    numQ = input("Invalid input. Please enter a valid number (multiple of 5 and less than 100): ").strip()

numQ = int(numQ)
ques = []
ans = []

print("\n--- Enter Your Questions and Answers ---\n")
for index in range(numQ):
    question = input(f"Enter question {index + 1}: ").strip()
    while not question:
        question = input(f"Question cannot be empty. Please enter question {index + 1}: ").strip()
    ques.append(question)

    answer = input(f"Enter answer for question {index + 1}: ").strip()
    while not answer:
        answer = input(f"Answer cannot be empty. Please enter answer for question {index + 1}: ").strip()
    ans.append(answer)

print("\n--- Quiz Setup Complete ---\n")

StudNum = input("Enter the number of students taking this quiz: ").strip()
while not StudNum.isdigit() or int(StudNum) <= 0:
    StudNum = input("Invalid input. Please enter a valid number of students: ").strip()

StudNum = int(StudNum)

print("\n--- Quiz Begins Now ---\n")

for index in range(StudNum):
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

    score = Take(ques, ans, numQ)
    grade, percent = calculate_grade(score, numQ)

    print("--------------------------------------------------")
    print(f"Result for {name}")
    print(f"Score: {score}/{numQ}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Grade: {grade}")
    print("--------------------------------------------------\n")

print("Thank you for using Zain Quizzes!")

# instead of telling the answers right away give em a report of what they did correct and what they did wrong
# ask them if they would like multiple choice questions or like normal question answers 
#  figure out a ways to like make an admin screen and student screen so the student just cant scroll up and answer the stuff from there ony 
# add an option for children to skip the question or move fwd and backward to and fro so they can jump to some questions 
# tell them which questions would they like to attempt every turn they get 
# can also add an option to time the children and end the quiz if the time limit exceeds find out the current time and tell them what time its is and how much time they got
