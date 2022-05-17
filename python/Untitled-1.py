#https://medium.com/jen-li-chen-in-data-science/leetcode-algorithm-8a1a094138ae

nums = [1,2,3,4,5,6,7,3,2,1]
k = 3
k %= len(nums)
print(k)
nums[k:], nums[:k] = nums[:-k], nums[-k:]