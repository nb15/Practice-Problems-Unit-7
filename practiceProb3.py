
def fib(nth):
	'''Takes in a number as the nth number of a Fibonacci sequence, and returns the nth Fibonacci number.''' 
	if nth < 2 :
		return 1
	
	else :
		nthFib = fib(nth - 2) + fib(nth - 1)
		
		#l = [1, 1]
		#l[2] = l[0] + l[1]
		#lastTwoTotal = l[2]
		return nthFib

print(fib(4))
print(fib(8))
