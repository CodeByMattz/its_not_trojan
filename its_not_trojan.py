import random
import socket
import threading


def game():


	number = random.randint(0, 1000)
	tries = 1
	done = False



	while not done:
		guess = int(input("Enter a guess: "))


		if guess == number:
			done = True
			print("You won!")
		else:
			tries += 1
			if guess > number:
				print("The actual number is smaller!")
			else:
				print("The actual number is larger!")

	print(f"You needed {tries} tries!")



game()















