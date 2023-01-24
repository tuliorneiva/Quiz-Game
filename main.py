from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    question_bank.append(Question(question_text, question_answer))


quiz = QuizBrain(question_bank)

#print(quiz.question_list[quiz.question_number].text)
#print(quiz.question_list[quiz.question_number].text)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz! Your final score is: {quiz.score}/ {quiz.question_number}.")