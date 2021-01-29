###import random

#player = input("Play rock, paper or scissors:")

#aioptions = [ "Rock", "Paper", "Scissors"]
#ai = random.choice(aioptions)
#
#print("You chose " + player +". AI chose " + ai +"." )
#
#if player == ai:
#	print("Draw.")
#
#
#elif player == "Rock":
#
#	if ai == "Scissors":
#		print("Rock destroys scissors. You win.")
#
#	else:
#		print("Paper suffocates rock. You lose.")
#
#
#elif player == "Scissors":
#
#	if ai == "Paper":
#		print("Scissors rip paper into shreds. You win.")
#
#	else:
#		print("Rock destroys scissors. You lose.")
#
#
#elif player == "Paper":
#
#	if ai == "Rock":
#		print("Paper suffocates rock. You win.")
#
#	else:
#	print("Scissors rip paper into shreds. You lose.")



#the above code only lets you play one game. need to make it so you can play several in a row.

#need a while loop


import random


#keeps track of wins, draws and losses

playerwins = 0
draws = 0
aiwins = 0

import sys

#player choice
def playeroption():
	player = input("Choose rock, paper or scissors:")
	if player in ["Rock", "rock", "r", "R"]:
		player = "Rock"


	elif player in ["Paper", "paper", "p", "P"]:
		player = "Paper"


	elif player in ["Scissors", "scissors", "scissor", "Scissor", "s", "S"]:
		player = "Scissors"

#first invalid input
	else:
		print("Invalid input.")

		player = input("Choose rock, paper or scissors:")
		if player in ["Rock", "rock", "r", "R"]:
			player = "Rock"


		elif player in ["Paper", "paper", "p", "P"]:
			player = "Paper"


		elif player in ["Scissors", "scissors", "scissor", "Scissor", "s", "S"]:
			player = "Scissors"

#second invalid input
		else:
			print("Invalid input.")

			player = input("Choose rock, paper or scissors:")
			if player in ["Rock", "rock", "r", "R"]:
				player = "Rock"


			elif player in ["Paper", "paper", "p", "P"]:
				player = "Paper"


			elif player in ["Scissors", "scissors", "scissor", "Scissor", "s", "S"]:
				player = "Scissors"

#third invalid input
			else:
				print("\nmate this is your third time. clearly you're too stupid to read instructions. make sure you don't play again")


	return player



#computer choice

while True:

	aioptions = ["Rock", "Paper", "Scissors"]
	ai = random.choice(aioptions)

	player = playeroption()

	print("\nYou chose " + player.lower() +".\n\n" + "AI chose " + ai.lower() + ". \n")


#accounting for all the possibilities
	if player == ai:

		print("Draw.\n")
		draws +=1


	elif player == "Rock":

		if ai == "Scissors":
			print("Rock destroys scissors. You win.\n")
			playerwins += 1

		else:
			print("Paper suffocates rock. You lose.\n")
			aiwins += 1


	elif player == "Scissors":

		if ai == "Paper":
			print("Scissors rip paper into shreds. You win.\n")
			playerwins += 1

		else:
			print("Rock destroys scissors. You lose.\n")
			aiwins += 1


	elif player == "Paper":

		if ai == "Rock":
			print("Paper suffocates rock. You win.\n")
			playerwins += 1

		else:
			print("Scissors rip paper into shreds. You lose.\n")
			aiwins += 1

	print("You have won " + str(playerwins) + ", drawn " + str(draws) + ", and lost " + str(aiwins) + ".\n")


#playagain
	playagain = input("Do you want to play again? Yes or no?\n")
	if playagain in ["Yes", "yes", "Y", "y"]:
		pass

	elif playagain in ["No","no", "N", "n"]:
		print("Game terminated.")
		break

	else:
		print("Invalid input.")

		playagain = input("Do you want to play again? Yes or no?\n")
		if playagain in ["Yes", "yes", "Y", "y"]:
			pass

		elif playagain in ["No", "no", "N", "n"]:
			print("Game terminated.")
			break































