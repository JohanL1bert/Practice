def pascal(number):
	line = [1]
	for k in range(number):
		line.append(line[k] * (number-k) / (k + 1))
		line = list(map(int, line))
	return line


result = input("print number ")
num = int(result)
print (pascal(num))