"""
Print the given Story in reverse order
"""
str = 'revereseme please'

str_list = str.split(" ")
#print(str_list)
for line in str_list[::-1]:
    print(line)