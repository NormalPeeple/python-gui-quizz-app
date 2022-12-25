class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def stil_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False) ? ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_question):
        if user_answer.lower() == correct_question.lower():
            print("Anda benar")
            self.score += 1
        else:
            print("Anda salah")
        print(f"Jawaban yang benar adalah {correct_question}")
        self.current_score = f"{self.score}/{self.question_number}"
        print(f"Skor anda saat ini adalah : {self.current_score}\n")
