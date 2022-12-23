print("WELCOME to the GAME!!")
Magic_number=7

while True:
  user_input = input("Would you like to play the game? (Y/n) ")
  if user_input=='n':
    break

  number=int(input("Guess the Number:"))
  if number==Magic_number:
        print("You guessed it correctly!")
  elif abs(number-Magic_number)==1:
        print("You were off by one")
  else:
        print("Sorry,it's wrong.")

