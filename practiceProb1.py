"""Write a recursive function that takes an integer and returns that integer’s factorial. Remember that

factorial(4) is 4 * 3 * 2 * 1. Another way to think of that is factorial (4) = 4 * factorial(3)"""



def factorial(num):
	'''Takes in integer input from user and returns interger's factorial.'''
	for int in range(num):
		if num == 0: # terminating case
			return 1
		else:
			num * factorial(num - 1)

# ––––––––––––––––––––––Main Program–––––––––––––––––––––––––