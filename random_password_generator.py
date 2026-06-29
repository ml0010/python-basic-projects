# ceollect user preferences
# - length
# - should contain uppercase
# - should contain special character
# - should contain digits

# create all available characters
# randomly pick characters up to the length
# ensure we hava at least one of each character type
# ensure length is valid

import random
import string

def generate_password():
   while True:
      try: 
         length = int(input('Enter the desired password length: ').strip())

         if length < 4:
            print('Password length must be at least 4 characters.')
            continue
         
         include_uppdercase = input('Include uppercase letters? (y/n): ').strip().lower()
         include_special = input('Include special characters? (y/n): ').strip().lower()
         include_digits = input('Include digits? (y/n): ').strip().lower()
         
         lower = string.ascii_lowercase
         uppercase = string.ascii_uppercase if include_uppdercase == 'y' else ''
         special = string.punctuation if include_special == 'y' else ''
         digits = string.digits if include_digits == 'y' else ''
         all_characters = lower + uppercase + special + digits

         required_characters = []
         if include_uppdercase == 'y':
            required_characters.append(random.choice(uppercase))
         if include_special == 'y':
            required_characters.append(random.choice(special))
         if include_digits == 'y':
            required_characters.append(random.choice(digits))


         remaining_length = length - len(required_characters)
         password = required_characters

         for _ in range(remaining_length):
            character = random.choice(all_characters)
            password.append(character)

         random.shuffle(password)
         str_password = "".join(password)

         return str_password
      
      except ValueError:
         print('Wrong password length. Please enter valid number.')

password = generate_password()
print(password)



