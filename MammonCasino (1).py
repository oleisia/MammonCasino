# Oleisia Johnson, CIS 113 Midterm Project

#Algorithm
#General Setup
  #Import the necessary modules: random and time.
  #Define a function type_text(text, delay) to print text with a typewriter effect.
  #Ask the user if they want to skip the intro dialogue. If they choose not to skip, display the introductory dialogue.

#Game Setup
  #Display the available betting options, ranging from 1 to 7.
  #Create a list named roulette_wheel containing numbers from 1 to 36.
  #Initialize variables: round_counter to 1, winnings to 0, and losses to 0.

#Game Loop
  #Start an infinite loop to keep the game running.
  #Inside the loop, display the current round number.
  #Prompt the user to enter their choice (a number from 1 to 7).

#Check the user's choice:

  #If the choice is 1:
    #Prompt the user to select a number for a straight bet.
    #Check if the selected number is valid (between 1 and 36).
    #Spin the wheel and compare the result to the user's choice.
    #Update winnings and losses accordingly.
  #If the choice is 2:
    #Prompt the user to select a number for a split bet.
    #Check if the selected number is valid.
    #Spin the wheel and compare the result to the user's choice.
    #Update winnings and losses accordingly.
  #If the choice is 3:
    #Prompt the user to select a number for a street bet.
    #Check if the selected number is valid.
    #Spin the wheel and compare the result to the user's choice.
    #Update winnings and losses accordingly.
  #If the choice is 4:
    #Spin the wheel.
    #Check if the result is within the range (1-18).
    #Update winnings and losses accordingly.
  #If the choice is 5:
    #Spin the wheel.
    #Check if the result is within the range (19-36).
    #Update winnings and losses accordingly.
  #If the choice is 6:
    #Prompt the user to choose "Even" or "Odd."
    #Check if the choice is valid.
    #Spin the wheel and compare the result to the user's choice.
    #Update winnings and losses accordingly.
  #If the choice is 7:
    #Display a farewell message and exit the game loop.
    #If the choice is not valid (not in the range 1-7), display an error message.
    #Ask the user if they want to play again (yes/no).

#If the user does not want to play again, exit the game loop.
#Increment the round counter.
#Display a blank line to separate rounds.

#After the game loop, display the user's final soul gem balance.

#General Setup
import random
import time

def type_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

#Intro Dialouge
skip_dialogue = input("Do you want to skip the intro dialogue? (yes/no): ").lower()
if skip_dialogue == "no":
  type_text("Welcome to Mammon's Infernal Paradise, the very heart of Hell's unquenchable greed! Souls and secrets are our chips, and desire is the name of the game.")
  print()
  time.sleep(1)
  type_text("So, tell me, what brings you to my domain, seeking the thrill of a lifetime or the price of your very soul?")
  time.sleep(1)
  print()
  type_text("Ah, to hell with the damn questions! I have an aching feeling that you're dying to play with me.")
  print()
  type_text("Here are the rules chap, read them well because you never know how far your greed will take you. ")
  time.sleep(2)
  print()
  print("Casino Rules:")
  print("• Every bet costs 5 soul gems.")
  print("• In the Greed Ring of Hell, under the dominion of Mammon, the sin of greed, soul gems are a highly coveted form of currency often used for high-stakes gambling and transactions within the casino. However, using soul gems is a perilous endeavor. Losing a bet with them can result in the permanent loss of a piece of one's soul, so patrons play at their own risk.")
  print()
  time.sleep(1)
  type_text("The rules seem simple enough don't they? Win, and you may grasp your heart's darkest desires. Lose, and your precious soul shall become mine to savor for all eternity. OH we're going to have so much fun! ↜(⃔•w•)⃕Ψ")
  print()
  time.sleep(1)
  type_text("Now, dear soul, it's time to pick your poison... ahem, I mean your betting option.")
  time.sleep(1)
  print()

#Game
  
#Betting Options
print("Betting Options:")
print("1. Straight Up: Single number selection. Potential payout is 35 to 1.")
print("2. Split: Single number selection. Covers the chosen number and one adjacent number (either above or below). Potential payout is 17 to 1.")
print("3. Street: Single number selection. Covers the chosen number and the next two numbers in sequence. Potential payout is 11 to 1.")
print("4. Top: Any number from 1-18. Potential payout is even soul gems (10).")
print("5. Bottom: Any number from 19-36. Potential payout is even soul gems (10).")
print("6. Even/Odd: Covers all even or all odd numbers from 1-36. Potential payout is even soul gems (10).")
print("7. Quit Game.")
print()

roulette_wheel = list(range(1,37))
round_counter = 1
winnings = 0
losses = 0

#Game Loop
while True:
  print ("Round " ,round_counter)
  user_choice = int(input("Your choice...(Enter a number 1 to 7): "))

  #Betting Option 1 : Straight Up
  if user_choice == 1:
    straight_bet = int(input("Which number would you like to select for the Split bet (1-36):"))
    if 1 <= straight_bet <= 36:
      type_text("𖣘....Spinning the wheel....𖣘 ")
      result = random.choice(roulette_wheel)
      print("Result: The rolled number is ", result)
      if straight_bet == result:
        earnings = (35 * 5) + 5
        winnings += earnings
        print("Outcome: Congratulations you greedy litte devil! You win ", earnings, "soul gems (35 to 1 on your bet of 5 soul gems)." )
      else:
        losses += 5
        print("Fortune's favor has abandoned you, You lose.")
    else:
        type_text("You're not getting away that easily, you sneaky bastard! Enter a valid number, or else.")
      
  #Betting Option 2 : Split
  elif user_choice == 2:
    split_bet = int(input("Which number would you like to select for the Split bet (1-36): "))
    if 1 <= split_bet <= 36:
      type_text("𖣘....Spinning the wheel....𖣘 ")
      result = random.choice(roulette_wheel)
      print("Result: The rolled number is ", result)
      if split_bet == result or abs(split_bet - result) == 1:
        earnings = (17 * 5) + 5
        winnings += earnings
        print("Outcome: Congratulations you greedy litte devil! You win ", earnings, "soul gems (17 to 1 on your bet of 5 soul gems).")
      else:
        losses += 5
        print("Fortune's favor has abandoned you, You lose.")
    else:
        type_text("You're not getting away that easily, you sneaky bastard! Enter a valid number, or else.")
    
  #Betting Option 3 : Street
  elif user_choice == 3:
    street_bet = int(input("Which number would you like to select for the Street bet (1-36): "))
    if 1 <= street_bet <= 36:
      type_text("𖣘....Spinning the wheel....𖣘 ")
      result = random.choice(roulette_wheel)
      print("Result: The rolled number is ", result)
      if street_bet <= result <= street_bet + 2:
        earnings = (11 * 5) + 5 
        winnings += earnings
        print("Outcome: Congratulations you greedy litte devil! You win ", earnings, "soul gems (11 to 1 on your bet of 5 soul gems).")
      else:
        losses += 5
        print("Fortune's favor has abandoned you, You lose.")
    else:
        type_text("You're not getting away that easily, you sneaky bastard! Enter a valid number, or else.")
      
  #Betting Option 4 : Top (Numbers 1-18)
  elif user_choice == 4:
    type_text("𖣘....Spinning the wheel....𖣘 ")
    result = random.choice(roulette_wheel)
    print("Result: The rolled number is ", result)
    if result >= 1 and result <= 18: 
      earnings = 10
      winnings += earnings
      print("Outcome: Congratulations you greedy litte devil! You win ", earnings, "soul gems (fixed earnings on your bet of 5 soul gems).")
    else:
      losses += 5
      print("Fortune's favor has abandoned you, You lose.")
      
  #Betting Option 5 : Bottom (19-36)
  elif user_choice == 5:
    type_text("𖣘....Spinning the wheel....𖣘 ")
    result = random.choice(roulette_wheel)
    print("Result: The rolled number is ", result)
    if result >= 19 and result <= 36: 
      earnings = 10
      winnings += earnings
      print("Outcome: Congratulations you greedy litte devil! You win ", earnings, "soul gems (fixed earnings on your bet of 5 soul gems).")
    else:
      losses += 5
      print("Fortune's favor has abandoned you, You lose.")
      
  #Betting Option 6 : Even/Odd
  elif user_choice == 6:
    even_odd_choice = input("Your preference for Even/Odd (Enter 'Even' or 'Odd'): ")
    if even_odd_choice.lower() == "even" or even_odd_choice.lower() == "odd":
      type_text("𖣘....Spinning the wheel....𖣘 ")
      result = random.choice(roulette_wheel)
      print("Result: The rolled number is ", result)
      if (even_odd_choice == "Even" and result % 2 == 0) or (even_odd_choice == "Odd" and result % 2 != 0):
        earnings = 10
        winnings += earnings 
        print("Outcome: Congratulations you greedy litte devil! You win ", earnings, "soul gems (fixed earnings on your bet of 5 soul gems).")
      else:
        losses += 5
        print("Fortune's favor has abandoned you, You lose.")
    else:
      type_text("You're not getting away that easily, you sneaky bastard! Enter a valid number, or else.")
      
  #Betting Option 7 : Quit
  elif user_choice == 7:
      type_text("Ah, a decision to quit? You leave with your soul intact, but remember, the gates of Mammon's Infernal Paradise are always open, ready to test your resolve again. Should you ever return, you'll find the temptation waiting, and I'll be here to welcome you back into the fold.")
      break
  else:
        type_text("You're not getting away that easily, you sneaky bastard! Enter a valid number, or else.")
    
  play_again = input("Do you want to play again? (yes/no): ").lower()
  if play_again != "yes":
    break
  round_counter += 1
  print()

print("Game over. Your final soul gem balance: ", winnings-losses)
