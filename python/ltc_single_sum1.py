from typing import Counter

'''
Given an integer array nums where every element appears three times except for one, 
which appears exactly once. Find the single element and return it.
'''
nums = [2,2,3,2]
nums1 = [0,1,0,1,0,1,99]
my_map = Counter(nums)

print(my_map)
nums.sort(reverse=True)
#print(nums)