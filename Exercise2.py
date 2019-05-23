import math, time

def fibonacci(indeks):
	raw = pow((math.sqrt(5)+1)/2, indeks)/math.sqrt(5)
	check = round(raw)
	return check
	

while True:
	try:
		result = input("Vvedite indeks ")
		number = int(result)
		print (fibonacci(number))
		time.sleep(2)
		exit()
	except ValueError:
		print ("Only numbers")