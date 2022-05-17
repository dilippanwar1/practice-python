'''
for number in range (100, 200 + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:
                #print(f'number in break is {number} and i is {i}')
                break  
        else:  # Executed because no break in for
            print (number)

'''
for number in range(100,200):
    if number>1:
        for i in range(2, number):
            if number%i == 0:
                break

        else:
            print(f'Prime Number is  {number}')