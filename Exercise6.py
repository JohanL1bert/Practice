import re, os, time

from collections import Counter



def check():
	global data
	f = open("testing.txt", 'r+')
	data = f.read()
	f.close()

def create_file():
	f = open("testing.txt", 'w+')
	f.write("""At the start of the twentieth century, scientists believed that they understood the most fundamental principles of nature. 
		Atoms were solid building blocks of nature; people trusted Newtonian laws of motion; most of the problems of physics seemed to be solved. 
		However, starting with Einstein's theory of relativity which replaced Newtonian mechanics, scientists gradually realized that their knowledge was far from complete. 
		Of particular interest wast the growing field of quantum mechanics, which completely altered the fundamental precepts of physics.
		is is is is
		was was
		start
		ending, bad, quantum, theory, Roman
		Klava bravo""")






def first_method():
	if input_words not in data:
		print ("Not found")
	else:
		regex = re.compile(input_words)
		text = regex.findall(data)
		coun = Counter(text).most_common()
		for word, i in coun:
			print (word,"=", i)


def second_method():
	check()
	new_data = data.split()
	if input_words in new_data:
		resul = new_data.count(input_words)
		print (resul)
	else:
		print ("Not found")
	







print("Print words")
input_words = input("")
method = input("Method of work with words. Print first of second\n")
print ("filename = testing.txt")


def method_work():
	if method in ("first", "First"):
		first_method()
	elif method in ("second, Second"):
		second_method()

path_to = input("Path to file with name of file \n")
file = os.path.isfile(path_to)
if file == True:
	check()
	method_work()
elif file == False:
	print ("file no found \nCreate one in this folder? Yes or No\n")
	empty = input("")
	if empty in ("Yes"):
		create_file()
		check()
		method_work()
	else:
		time.sleep(1)
		exit()






















##print (word,"=", i)
#	resul = (word +"="+ str(i))
#print (resul)	
