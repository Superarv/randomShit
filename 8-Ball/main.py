import random
start = True

user = input('Enter your username: ')

while start:

  
  i = input(f"{user}: ")

  if i in ['/logoff']:
    print(f'{user} has logged off')
    break
  else:
    
    encouraging_phrases = ['Good luck!','Try again tomorrow!','You can do it!','Never Give Up!','I will always be by your side.','Hope it works out well!','Good Job!','I support you 100%','I am your number one supporter']
    index_number = random.randint(0,8)
    phrase = encouraging_phrases[index_number]
    print('App:', phrase)
