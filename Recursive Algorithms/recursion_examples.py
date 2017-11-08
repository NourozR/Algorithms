# SERIES CALCULATION USING RECURSION
def SeriesSum(n):
	if n==0:
		return 0
	else:	
		return(n+SeriesSum(n-1))
	
print(SeriesSum(100))	

# POWER CALCULATION USING RECURSION
def Power(x,n):
	if n==0:
		return 1
	else:
		return(x*Power(x, n-1))

print(Power(2,4))		

# FIBONACCI USING RECURSION		
def Fibonacci(n):
	if n==0 or n==1:
		return 1
	else:
		return (n+Fibonacci(n-1))

print(Fibonacci(10))	

# FACTORIAL USING RECURSION
def Factorial(n):
	if n==0:
		return 1
	else:
		return (n*Factorial(n-1))
print(Factorial(5))		
		

		