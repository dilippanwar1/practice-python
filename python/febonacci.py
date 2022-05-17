'''
def a(num):
    if num is 0: return num
    elif num is 1: return num
    else:
        print(f'num is {num} and num-1 is {num-1} and num-2 is {num-2}')
        return a(num -1) + a(num-2)
    

for i in range (0,12):
    print(f'I i {i}')
    print(a(i))

Range: 12 numbers febonacci

What is required.
current = sum of (previous 2)
prev2 = list[n-1] + list[n-1]

'''
my_list= [0,1]
for i in range (0,12):
    if i>1:
        febo_num = my_list[i-1] + my_list[i-2]
        my_list.append(febo_num)

print(my_list)
    
