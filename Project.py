import random
import os
import json
Questions_file = "Questions.json"
Score_file = "Scores.json"
def load_question():
    if os.path.exists(Questions_file):
        with open(Questions_file,"r") as file:
            return json.load(file)
    return []
def save_question(questions):
    if os.path.exists(Questions_file):
        with open(Questions_file,"w") as file:
            json.dump(questions,file,indent=4)
def load_score():
    if os.path.exists(Score_file):
        with open(Score_file,"r") as file:
            return json.load(file)
    return []
def save_score(Scores):
    if os.path.exists(Score_file):
        with open(Score_file,"w") as file:
            return json.dump(Scores,file,indent=4)
def add_question():
    question_text=input("Enter Your Question : ")
    options = []
    for i in range(1,5):
        option=input(f"Enter Option {i}: ")
        options.append(option)
    while True:
        try:
            correct_answer = int(input("Enter the correct answer option (1/2/3/4): "))
            if 1<=correct_answer<=4:
                break
            else :
                print("Please enter valid answer option between 1-4.")
        except ValueError:
            print("Invalid Format!!Choose Number only")
    question = {
        "Question":question_text,
        "Options":options,
        "Correct":int(correct_answer)
    }
    questions=load_question()
    questions.append(question)
    save_question(questions)
    print("Well Done user !! Question is successfully Added..")
def edit_question():
    questions=load_question()
    if not questions:
        print("No Quuestion is available to edit.")
        return
    for i,q in enumerate(questions):
        print(f"Question {i+1}. {q['Question']}")
    choice=int(input("Select the question you want to edit : "))-1
    if 0<= choice<=len(questions):
        q=questions[choice]
        q['Question']=input(f"Edit question({q['Question']}): ")
        for i in range(4):
            q['Options'][i]=input(f"Edit option {i+1} : ")
        answer = input("Edit the correct answer now : ")
        q['Correct'] = int(answer) 
        save_question(questions)
        print("Question successfully edited..")
    else:
        print("Invalid Selection!! Choose correct question to edit")
def take_quiz():
    questions=load_question()
    if not questions:
        print("No questions are available to be presented in quiz.")
        return
    random.shuffle(questions)
    score=0
    for i,q in enumerate(questions[:5]):
        print(f"Question {i+1} : {q['Question']}")
        for index,opt in enumerate(q['Options']):
            print(f"{index+1}. {opt}")
        answer = int(input("Your answer (1-4): "))
        if answer ==q['Correct']:
           print("Congo!! Your Answer is Correct.")
           score+=1
        else:
            print(f"Wrong!! Correct Answer is : {q['Correct']}")
        print(f"Your Total Score is {score}/{len(questions[:5])}")
        name = input("Enter Your Name to Save the Score : ")
        Scores = load_score()
        Scores.append({"Name":name,"Score":score})
        save_score(Scores)
        print("Score Added Successfully!!")
def view_scores():
    Scores = load_score()
    if not Scores:
        print("No Scores are available to Display..")
        return
    for s in Scores:
        print(f"{s['Name']}: {s['Score']}")

print("-------------------------------Quiz Management System--------------------------------------")
while True:
    print("1. Add Your Question.")
    print("2. Edit your Existing Questions.")
    print("3. Perform the Quiz.")
    print("4. View Your Past Scores.")
    print("5. Exit from System.")
    print("---------------Don't Press Other Choices than(1-5)--------------------------")
    choice = int(input("Enter your choice (1-5): "))
    if(choice==1):
        add_question()
    elif(choice==2):
        edit_question()
    elif(choice==3):
        take_quiz()
    elif(choice==4):
        view_scores()
    elif(choice==5):
        print("Exiting from System...")
        break
    else :
        print("----------------------------Told You Nothing will Happen-----------------------")