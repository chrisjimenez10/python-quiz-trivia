from question_model import Question
from data import trivia_questions
from quiz_brain import QuizBrain
from tools import logo

question_bank = [Question(item['text'], item['answer']) for item in trivia_questions()]

quiz = QuizBrain(question_bank)
print(logo)
quiz.next_question()