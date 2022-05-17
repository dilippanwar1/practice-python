'''Write a Python Program to Count the Number of Vowels in a String?'''
vow_list = ['a','e','o','u','v']

input_string = "Hi I am an engineer. I like to travel and eat"
vow = 0

for i in input_string:
    if i in vow_list:
        vow +=1


print(f'Total number of vowels: {vow} ')
        