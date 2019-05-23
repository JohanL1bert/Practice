import re
from collections import Counter


f = open("filelist.txt", 'w+')
print ("Use default text in file or u wana type something ? type Default or Write")
choice = input("")
if choice == "Default":
	f.write("""I watched you change
	Into a fly
	I looked away
	You're on fire
	I watched a change in you
	It's like you never had wings
	And you feel so alive
	I have watched you change
	I took you home
	Set you on the glass
	I pulled off your wings
	Then I laughed
	I watched a change in you
	It's like you never had wings
	Now you feel so alive
	I have watched you change
	It's like you never had wings
	Anh, ahah
	Anh, ahah
	Anh, ahah
	Anh, ahah
	Anh, ahah""")
	
else:
	checker = input("Type here\n")
	f.write(checker)

f.close()


f = open("filelist.txt", 'r')


data = f.read()


text =re.findall(r'\w+', data)
coun = Counter(text).most_common()
coun.sort(key = lambda x: (-x[1], x[0]))
for word, i in coun:
	print (word,"=", i)


# Some another method. All words will begin with a capital letter
# text = [i.title() for i in text]
# put this piece of code after lines 43
#--
