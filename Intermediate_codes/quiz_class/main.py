from Intermediate_codes.quiz_class.data import question_data
from Intermediate_codes.quiz_class.question_model import Question
from Intermediate_codes.quiz_class.quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    text = item["question"]
    answer = item["correct_answer"]
    questions = Question(text, answer)
    question_bank.append(questions)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
