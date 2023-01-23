from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    question_bank.append(Question(entry["question"], entry["correct_answer"]))


brain = QuizBrain(question_bank)


while brain.still_has_questions():
    brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {brain.score}/{brain.q_number}")
