from collections import deque

my_q = deque()
my_q.append('el1')
my_q.append('el2')
my_q.append('el3')
my_q.append('el4')

print(my_q)

my_q.appendleft('newel1')
print(my_q)
print(my_q.pop())
print(my_q.pop())
print(my_q.pop())

print(my_q)


