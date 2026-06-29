# list of questions
# store the answers
# randomly pick questions
# ask the question
# see if they are correct
# keep track of the score
# tell the user their score

import random

questions = {
    "What is the capital of Japan?": "tokyo",
    "Which planet is closest to the Sun?": "mercury",
    "What is the largest ocean on Earth?": "pacific",
    "What gas do humans breathe in?": "oxygen",
    "What is the fastest land animal?": "cheetah",
    "What is the smallest prime number?": "two",
    "Which continent is Egypt in?": "africa",
    "What is the boiling point of water in Celsius?": "hundred",
    "Which planet is known as the Blue Planet?": "earth",
    "What is the main language of Brazil?": "portuguese"
}

def trivia_game():
   questions_list = list(questions.keys())
   total_questions = 5
   score = 0

   selected_questions = random.sample(questions_list, total_questions)

   for index, question in enumerate(selected_questions):
      print(f'{index + 1}. {question}')
      user_answer = input('Your answer: ').lower().strip()
      correct_answer = questions[question].lower()
      if correct_answer == user_answer:
         print("Correct!\n")
         score += 1
      else:
         print(f'Wrong! Correct answer is: {correct_answer}\n')
   print(f'Game over. Your final score is: {score}/{total_questions}')

trivia_game()