'''
Sort the items in a list
Sort without a sort function
'''
list1 = [11,51,12]
#list1.sort(reverse=True)
#print(f'sorted list is {list1}')
new_list = []
while list1:
    mininum = list1[0]   
    for num in list1:
        print(f'NUM is:{num}')
        if mininum > num:
            mininum = num
            print(f'MIN is:{mininum}')
    new_list.append(mininum)
    print(f'new_list is {new_list}')
    list1.remove(mininum)

print(f'Sorted list is {new_list}')




