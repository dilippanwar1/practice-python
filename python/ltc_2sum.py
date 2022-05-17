nums = [2,7,11,15]
target = 26
num_l = len(nums)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target : 
            print( f"These two numbers {nums[i]} and  {nums[j]} represnts sum as same as target")

