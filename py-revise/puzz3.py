'''
How to count the occurrences of a particular element in the list?
'''

from typing import Counter


weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']

#my_map = Counter(weekdays)
#print(my_map)
dic = {}
for key in weekdays:
    if dic.get(key):
        dic[key] +=1
    else:
        dic[key] = 1

print(dic)
