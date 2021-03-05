import re
#initializing parameters
j=0
list=[]

with open('task.txt', 'r') as file:
    data = file.read()
    numbers = re.findall(r'[\d.]+', data)  # reading a numbers into a list

for i in range(0,5):    #for loop creates 5x5 list from numbers list
    list.append(numbers[j:j+5])
    j+=5

a=int(list[0][0]) #initilizing point to find a number which equals its position
while True:
    x=a//10
    y=a%10
    if int(list[x-1][y-1])==a:
        break
    else: a=int(list[x-1][y-1])

print (a)
