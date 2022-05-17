"""
there is a list of given numbers and also there is target number. Target number is the sum of any of the two numbers in the list.
You need to find those two numbers, whose sum is equal to TARGET number
"""
nums = [2,7,11,15,12,12,45,75,22,2,11,24]
target = 26

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] is target:
            print (f'Those two numbers are: {nums[i]} and {nums[j]}')
    


