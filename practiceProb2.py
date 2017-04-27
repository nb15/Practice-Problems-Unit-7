

def sum(l):
	'''Takes in a list of numbers and returns the sum of the list.'''
	if len(l) == 0:
		return 0
	else:
		total = 0
		num = l[0]
		total += num 
		l = l[1:]
		total += sum(l)
		return total



# ----------------------Main List--------------------
sumL = [2, 3, 4, 5, 6, 7, 8]
print(sum(sumL))
