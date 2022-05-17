'''Write a Python Program to Swap the First and Last Value of a List?'''

input_list = [1,45,32,32,214,5,7,8,4,24]
list_len = len(input_list)

last_ele = input_list[list_len -1]
first_ele = input_list[0]
print(f'Before swap first ele was {first_ele} and last ele was {last_ele} ')

input_list[list_len -1] = first_ele
input_list[0] = last_ele
print(f'After swap first ele is {input_list[0]} and last ele is {input_list[list_len -1]} ')

