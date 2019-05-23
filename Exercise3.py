import random

first_massive = random.sample(range(200), 20)
second_massive = random.sample(range(200),20)


tretiy_massive = list(set(first_massive + second_massive))
tretiy_massive.sort()
for item in tretiy_massive[:]:
	if item%5 == 0 :
		tretiy_massive.remove(item)


print ("lenght of list = ",(len(tretiy_massive)))
print (tretiy_massive)