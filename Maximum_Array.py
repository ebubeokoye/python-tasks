from functools import reduce
nums = [1,12,-5,-6,50,3]
average_const = []
k = 4
i = 0
while i <= (len(nums))-k:
        sliced_list = nums[i:i+k]
        average_of_sliced =  reduce(lambda x,y: x + y, sliced_list)/k
        average_const.append (average_of_sliced)
        i+=1
        
maximum_number = max(average_const)
print (maximum_number)

