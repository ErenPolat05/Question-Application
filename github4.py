


class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer


    def checkAnswer(self,answer):
        return self.answer == answer


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1 }: {question.text}")

        for q in question.choices:
            print("-"+q)

        answer = input("Your Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
    

    def loadQuestion(self):
        if len(questions) == self.questionIndex:
            self.showScore()
        else:
         self.displayProgress()

         self.displayQuestion()

    def showScore(self):
        print("Score : ", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print("Quest is over.")
        else:
            print(f"Quest continue : {questionNumber}/{totalQuestion}")

 

q1 =Question("Which Team Is the most Powerful?",["Fb","Gs","Bjk" ,"Ts"],"Gs")
q2 =Question("Which Team Is the most Successful?",["Gs","Ts","Fb","Bjk" ],"Gs")
q3 =Question("Which Team Is the most Expensive?",["Gs","Bjk" ,"Ts","Fb"],"Gs")
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()