num1 = 1
num2 = 1
 
text = input("Indeks of element: ")
number = int(text) 

i = 0
while number - 2 > i: #loop while satisfying the condition. For example number = 5 - 2 = 3.
    suma = num1 + num2 #first loop suma = 1+1, second suma 1 + 2, third = 2+3
    num1 = num2 # 1=1, second loop 2=2 and third 3 = 3
    num2 = suma # suma values is to assign to num2(2 = 2) then 3 = 3 and the last 5 = 5.
    i += 1
 
print("Result =", num2)
