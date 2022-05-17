'''
Find prime number between 100 -200
'''

for num in range(100,200):
    if all(num%i!=0 for i in range(2,num)):
        print(f'Prime number is {num}')
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
newstr = ' '.join(weekdays)
print(newstr)