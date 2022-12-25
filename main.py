from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
    text = x["text"]
    answer = x["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.stil_has_question():
    quiz.next_question()
print(f"Selamat anda menyelesaikan quiz nya\nSkor akhir anda adalah : {quiz.current_score} ")
