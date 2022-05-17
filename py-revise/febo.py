'''
my_list = []

for i in range(0,12):
    if i>1:
        my_list.append(my_list[i-1] + my_list[i-2])
    else:
        my_list.append(i)

print(my_list)
'''
'''
febo_list = []
def getnum(num):
    if num < 2:
        print(num)
        return num
    else:
        return febo_list[i-1] + febo_list[i-2]
        
    

for i in range(0,12):
    febo_list.append(getnum(i))

print(f'Final febo list is {febo_list}')
'''
febonac = []
for i in range(1,10 +1):
    if i < 4:
        febonac.append(i)
    else:
        febonac.append(febonac[i-2] + febonac[i-3])

print(f'Febonaci series is {febonac}')