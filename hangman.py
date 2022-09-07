
import random as rand
import os as super_secret_library

words = ['car', 'plane', 'train', 'truck', 'bus'] # List of words 

word_list = ([*words[rand.randint(0,4)]]) # Selects random word and turns it's characters into a list
word = ''.join(word_list) # Makes turns back into string
censor = ("X" * len(word_list)) # Makes the censored word


print("Welcome to the game of hangman! You have five guesses to get the word. Enter a letter, or enter /word {word}.")

chances = 5

while True:
  guess = input("Enter your guess: ")

  if censor == word:
    print("Congrats, you won!")
  elif "/word " in guess:
    guess = guess.replace('/word ', '')
    if guess == word:
      print("Congrats, you won!")
      break
    if guess != word:
      print("You lost it all!")
      chances = 0
      break
    else:
      print("Congrats, you broke the laws of logic!")
  elif len(guess) > 1:
    print("Re-enter your guess, only use 1 character")
  elif chances <= 0:
    print(f"You lost, the word was {word}")
    break
  elif guess in word_list:
    pos = word.index(guess)
    censor = censor[0:pos] + guess + censor[pos+1: ]
    print(censor)
  else:
    chances -= 1
    print(f"Incorrect guess, you have {chances} chances left")
   
    
    

    
