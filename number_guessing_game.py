import random

number_to_guess = random.randint(1, 100)
guess_count = 10

while True:
   try:
      guess = int(input('Guess the number between 1 and 100: '))
      if guess < number_to_guess:
         print('Too low!')
      elif guess > number_to_guess:
         print('Too high!')
      else:
         print('Congratulations! You guessed the number.')
         break
      guess_count = guess_count - 1
      if guess_count == 0:
         print(f'The answer was {number_to_guess}. You have failed.')
         break       
      print(f'You have {guess_count} more times to guess.')
   except ValueError:
      print('Please enter a valid number.')
      
