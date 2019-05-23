import os, time

def create():
	f = open(user_input, 'w')
	f.write("Я люблю програмування")
	f.close()

def file_one_revers():
	global revers
	f = open(user_input, 'r')
	save = f.read()
	revers = ''.join(reversed(save))
	f.close()

def file_two_rewrite():
	get = os.path.dirname(user_input)
	suma = str(get +  "\\file2.txt")
	d = open(suma, 'w+')
	d.write(revers)
	d.close()



def cheker():
	global user_input
	print ("filename = file1.txt")
	user_input = input("Path to file with name of file. Example D:\\namefolder\\file1.txt \n")
	file = os.path.isfile(user_input)
	if file == True:
		print("Done")
		file_one_revers()
		file_two_rewrite()
	elif file == False:
		print ("file not found")
		message = input("Do you wanna create file?/n print Yes or No ")
		if message in ("Yes","yes", "ye","y"):
			print ("file is created")
			create()
			file_one_revers()
			file_two_rewrite()
		else:
			print("Ok, end")
			time.sleep(1)
			exit()

cheker()







