from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# The above code is the main file that runs the quiz game. It uses the classes and functions from the other files to create
# the quiz game. The main file imports the Question class from question_model.py, the question_data from data.py, the
# QuizBrain class from quiz_brain.py, and the QuizInterface class from ui.py. It then creates a list of Question objects
# using the question_data, creates a QuizBrain object using the list of questions, and creates a QuizInterface object to
# display the quiz game to the user. The main file then runs the quiz game and prints the final score to the console.±
