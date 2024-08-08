from tools import clear_console, logo


class QuizBrain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            user_response = input(F"Q.{self.question_number} - {current_question.text} (True/False):\n").title()
            if user_response == "True" or user_response == "False":
                break
            else:
                print("Please provide valid input")

        clear_console()
        print(logo)

        points = self.display_messages(current_question.answer, user_response)
        if points:
            self.score += 1
            print(F"Your current score is: {self.score}/{self.question_number}")
        else:
            print(F"Your current score is: {self.score}/{self.question_number}")

        if self.is_over():
            return
        else:
            return self.next_question()

    def is_over(self):
        if self.question_number > len(self.question_list) - 1:
            clear_console()
            print(F"You have completed the Quiz\nFinal Score: {self.score}/{self.question_number}")
            return True
        else:
            return False

    def display_messages(self, question, response):
        if question == response:
            print(F"Correct!\nThe answer was: {question}\n")
            return True
        else:
            print(F"Wrong!\nThe answer was: {question}\n")
            return False
