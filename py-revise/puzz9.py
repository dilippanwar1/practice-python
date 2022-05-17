'''Write a Python Program to Check Common Letters in Two Input Strings?
set1&set2 returns the common elements set, where set1 is the list1 and set2 is the list2
'''

input_1 = "Hi Dilip"
input_2 = "How are you Dilip"

for str1 in input_1.replace(" ",""):
    for str2 in input_2.replace(" ", ""):
        if str1 is str2:
            print(f'common string is {str1}')

#Set way:

def getCommonElements(l1, l2):
    l1_set = set(l1)
    l2_set = set(l2)
    return l1_set&l2_set

print(getCommonElements(input_1, input_2))
