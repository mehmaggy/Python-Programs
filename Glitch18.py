answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=2

if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct answer')
    else:
        print('Wrong Answer')
    
    answer=input('Question 2: What is the name of your favourite gaming project? ')
    if answer.lower()=='quizgame':
        score += 1
        print('correct answer')
    else:
        print('Wrong Answer')
print('your marks are :',score,'out of', total_questions)
