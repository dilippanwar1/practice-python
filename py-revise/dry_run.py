nums = [2,7,1,11,15,12,12,45,75,22,2,11,24,25]
new_num = [1,2]
target = 26
for i in range( len(nums)):
  j=i+1
  for j in range( len(nums)):
   value=nums[i] +nums[j]  
   if value == target:
     print(f'sum of {nums[i]} and {nums[j]} equal to {target}')
    
