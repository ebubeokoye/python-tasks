def pivot_index (nums):
    i=0 
# i is pointing at the pivot index
    lastIndex = len(nums) - 1
    while i < len(nums):
        ints_on_the_right = []
        ints_on_the_left = []
        
        if (i == 0):
            ints_on_the_right = nums[i+1:lastIndex + 1]
            ints_on_the_left = []
        elif (i == lastIndex):
            ints_on_the_right = []
            ints_on_the_left = nums[0:lastIndex - 1]
        else:
            ints_on_the_right = nums[i+1:lastIndex + 1]
            ints_on_the_left = nums[0:i]

        sum_ints_on_the_right = sum(ints_on_the_right)
        sum_ints_on_the_left = sum(ints_on_the_left)
        
        if sum_ints_on_the_right == 0:
            if i == 0: return i
        if sum_ints_on_the_left == 0:
            if i == lastIndex: return i
        if sum_ints_on_the_left == sum_ints_on_the_right:
            return i
        i+=1
    return -1

nums = [1,7,3,6,5,6]
print (pivot_index(nums))