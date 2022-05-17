'''Write a Python Program to Find the Second Largest Number in a List?'''
input_list = [53,54,2,2,2,1,1,1113,4,7,4,1,68679]
input_list = list(set(input_list))
input_list.sort(reverse=True)

print(f'{input_list[1]}')