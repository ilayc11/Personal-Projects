class QuizBrain:
    def __init__(self, qlist):
        self.questionNum = 0
        self.questionList = qlist
        self.score = 0

    def stillHasQuestions(self):
        return self.questionNum < len(self.questionList)

    def nextQuestion(self):
        currQuestion = self.questionList[self.questionNum]
        self.questionNum += 1
        userAnswer = input(f"Q.{self.questionNum}: {currQuestion.text} (True/False): ")
        self.checkAns(userAnswer, currQuestion.answer)

    def checkAns(self, userAns, currQuestionAns):
        if userAns.lower() == currQuestionAns.lower():
            self.score += 1
            print("You Got it right!")
        else:
            print("That's Wrong")
        print(f"The correct answer was: {currQuestionAns}")
        print(f"Your current score is: {self.score}/{self.questionNum}")
