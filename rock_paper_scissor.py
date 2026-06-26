import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
choice_emojis = {
   ROCK: '🪨',
   PAPER: '📄',
   SCISSORS: '✂️'
}
choices = tuple(choice_emojis.keys()) # tuples to make it read-only list

def get_user_choice():
   while True:
      # Ask the user to make a choice
      user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
      # User choice is valid
      if user_choice in choices:
         return user_choice
      # User choice is not valid
      else: 
         print('Invalid choice! Try again.')

def display_choices(user_choice, computer_choice):
      print(f'You chose {choice_emojis[user_choice]} and computer chose {choice_emojis[computer_choice]}')   
      
def determine_winner(user_choice, computer_choice):
   # Computer and my chocices are equal
   if computer_choice == user_choice:
      print('It\'s a tie! One more time.')
      return False
   # User wins
   elif (
      (user_choice == ROCK and computer_choice == SCISSORS) or
      (user_choice == PAPER and computer_choice == ROCK) or
      (user_choice == SCISSORS and computer_choice == PAPER) 
   ):
      print('You win!')
   # User looses
   else:
      print('You loose.')
   return True

def play_game():
   while True:
      user_choice = get_user_choice()
      computer_choice = random.choice(choices)

      display_choices(user_choice, computer_choice)
      result = determine_winner(user_choice, computer_choice)
      if not result:
         continue
      
      # Game is over
      continue_play = input('Continue? (y/n): ').lower()
      if continue_play == 'n':
         print('Bye for now! 👋')
         break

play_game()


# import random

# choices = ('r', 'p', 's') # tuples to make it read-only list
# choice_emojis = {
#    'r': '🪨',
#    'p': '📄',
#    's': '✂️'
# }

# def get_user_choice():
#    while True:
#       # Ask the user to make a choice
#       user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
#       # User choice is valid
#       if user_choice in choices:
#          return user_choice
#       # User choice is not valid
#       else: 
#          print('Invalid choice! Try again.')

# def display_choices(user_choice, computer_choice):
#       print(f'You chose {choice_emojis[user_choice]} and computer chose {choice_emojis[computer_choice]}')   
      
# def determine_winner(user_choice, computer_choice):
#    # Computer and my chocices are equal
#    if computer_choice == user_choice:
#       print('It\'s a tie! One more time.')
#       return False
#    # User wins
#    elif (
#       (user_choice == 'r' and computer_choice == 's') or
#       (user_choice == 'p' and computer_choice == 'r') or
#       (user_choice == 's' and computer_choice == 'p') 
#    ):
#       print('You win!')
#    # User looses
#    else:
#       print('You loose.')
#    return True

# def play_game():
#    while True:
#       user_choice = get_user_choice()
#       computer_choice = random.choice(choices)

#       display_choices(user_choice, computer_choice)
#       result = determine_winner(user_choice, computer_choice)
#       if not result:
#          continue
      
#       # Game is over
#       continue_play = input('Continue? (y/n): ').lower()
#       if continue_play == 'n':
#          print('Bye for now! 👋')
#          break


# play_game()