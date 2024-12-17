def move_zeroes (nums):
    nums = [0,1,0,3,12]
#determine the index of the numbers you want to change ie position 0 and 2 using the index() method
#use the pop() function to remove those numbers at their specific positions and it returns them
#then insert the elements at the new position using insert()

#Nb .index can take 3 arguments, the first is the itemwhose index you want to find. the 2nd and the last are the indices of the 
# starting and ending items where you want to begin and end the search.
    
    i = 0
    while i < len(nums):
        if nums[i]==0:
            numbers_to_move = nums.pop(i)
#insert function takes two arguments: the new position you want to insert and the item you want to insert
            nums.append(numbers_to_move)
        i+=1
    return (nums)

print(move_zeroes([0,1,0,3,12]))

