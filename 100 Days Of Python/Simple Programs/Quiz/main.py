from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for x in question_data:
    question_bank.append(Question(text=x.get("text"),answer=x.get("answer")))
quiz = QuizBrain(question_bank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()

print("youve completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.questionNum}")