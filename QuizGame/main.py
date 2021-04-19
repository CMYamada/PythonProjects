from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:
    questionText = question['text']
    questionAnswer = question['answer']
    newQuestion = Question(questionText, questionAnswer)
    questionBank.append(newQuestion)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}")