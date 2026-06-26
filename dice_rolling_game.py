import random

roll_count = 0

def roll():
   dice1 = random.randint(1, 6)
   dice2 = random.randint(1, 6)
   print(f'You rolled a {dice1} and {dice2}.')

while True:
   choice = input('Roll the dice? (y/n): ').lower()
   if choice == 'y':
      try: 
         roll_num = int(input('How many times you wish to roll (between 1 and 10): '))
         type(roll_num)
         if isinstance(roll_num, int) and roll_num <= 10 and roll_num > 0:
            while roll_num > 0:
               roll()
               roll_count = roll_count + 1
               roll_num = roll_num - 1
      except ValueError:
         print('Invalid choice! Rolling once.')
         roll()

      
   elif choice == 'n':
      if roll_count > 0:
         print(f'You have rolled the dices {roll_count} times.')
      print('Thanks for playing. Bye!')
      break
   else:
      print('Invalid choice.')