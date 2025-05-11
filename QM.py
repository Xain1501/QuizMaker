def Take(ques, ans, num):
    score = 0
    for index in range(num):
        print(ques[index])
        studAns = input("Enter your answer for this question: ").strip()
        while not studAns:
            studAns = input("Answer cannot be empty. Please enter your answer: ").strip()
        
        if studAns == ans[index]:
            score += 1
            print("You answered this question correctly. Good job!")
        else:
            print("You answered this question wrong. The correct answer was: " + ans[index])
    return score


print("Welcome to Zain Quizzes!\n")

print("Let's create a quiz together.\n")

numQ = input("Enter the number of questions you want to ask (not more than 100): ").strip()
while not numQ.isdigit() or int(numQ) <= 0 or int(numQ) > 100:
    numQ = input("Invalid input. Please enter a valid number of questions (1-100): ").strip()

numQ = int(numQ)
ques = [] * numQ
ans = [] * numQ

for index in range(numQ):
    question = input("Enter question number " + str(index + 1) + ": ").strip()
    while not question:
        question = input("Question cannot be empty. Please enter question number " + str(index + 1) + ": ").strip()
    ques.append(question)

    answer = input("Enter answer for question number " + str(index + 1) + ": ").strip()
    while not answer:
        answer = input("Answer cannot be empty. Please enter answer for question number " + str(index + 1) + ": ").strip()
    ans.append(answer)

print("Let's take the quiz together!\n")

StudNum = input("Enter the number of students taking this quiz: ").strip()
while not StudNum.isdigit() or int(StudNum) <= 0:
    StudNum = input("Invalid input. Please enter a valid number of students: ").strip()

StudNum = int(StudNum)

for index in range(StudNum):
    name = input("Enter your name: ").strip()
    while not name:
        name = input("Name cannot be empty. Please enter your name: ").strip()
    score = Take(ques, ans, numQ)
    print(name + " scored " + str(score) + "/" + str(numQ))

print("\nThank you for using Zain Quizzes!\n")


#features that can be added to improve the project
# instead of telling the answers right away give em a report of what they did correct and what they did wrong
# ask them if they would like multiple choice questions or like normal question answers 
# make  a standard use percentages and grades add formatting like dashes to separate sections figure out a ways to like make an admin screen and student screen so the student just cant scroll up and answer the stuff from there ony 
# make sure ppl make questions in a format to help grading like total questions can be like a multiple of 5s but still less than a hundred questions
# add an option for children to skip the question or move fwd and backward to and fro so they can jump to some questions 
# tell them which questions would they like to attempt every turn they get 
# can also add an option to time the children and end the quiz if the time limit exceeds find out the current time and tell them what time its is and how much time they got
