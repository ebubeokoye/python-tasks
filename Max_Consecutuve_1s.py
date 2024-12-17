def counter (nums):
     nums = [1,1,1,0,0,0,1,1,1,1,0]
     k= 2
     list_of_1s = []
     list_of_1s_0s = []
     group_of_zeroes = []
     sum_of_1s_list_of_0s =  []
     result = []
     #pointer j should only be valuable when its pointing at nums[j] = 0 else we keep it moving and increment
     # pointer (i) will point at the 1s and will append them to any provided list
     #pointer (j) will point at the zeroes and will append them to any provided list
     i = 0
     j = 1
     while i < len(nums) and j <len(nums):
          while nums[i] == 1:
               list_of_1s.append(nums[i])
               if nums[j] == 1:
                    i+=1
                    j+=1
                    #lets count  
               elif nums[j] == 0:
                    # we will end appending the group of ones to the list_of_1s list and count/check the length
                    sum_of_1s = len(list_of_1s)
                    sum_of_1s_list_of_0s.append(sum_of_1s)
                    #lets count the zeroes as 1 
                    sum_of_1s_list_of_0s.append(1)
                    i+=1
                    j+=1

          while nums[i] == 0:
               if nums[j] == 0:
                    #lets count the zeroes as 1 and append to them to list
                    sum_of_1s_list_of_0s.append(1)
                    i+=1
                    j+=1

               elif nums[j] == 1:
                    i+=1
                    j+=1


     #i is pointing at values> 1 and j pointing at 1s
     i=0
     j=i+1
     k = 2
     while i <len(sum_of_1s_list_of_0s) and j <len(sum_of_1s_list_of_0s):
          while sum_of_1s_list_of_0s[i] > 1:
               counter+=1
               if sum_of_1s_list_of_0s[j] == 1:
                    j+=1
               elif sum_of_1s_list_of_0s[j] > 1:
                    if len(counter) < k:
                         #we will add the large numbers and the single 1 value separating them
                         adding_one_to_zero = sum_of_1s_list_of_0s[j] + len(counter) + (sum_of_1s_list_of_0s[j] - len(counter))
                         result.append(adding_one_to_zero)

                    elif len(counter) > k:
                         if sum_of_1s_list_of_0s[j] < (sum_of_1s_list_of_0s[j] - len(counter)):
                              adding_one_to_zero = (sum_of_1s_list_of_0s[j] - len(counter)) + k
                              result.append(adding_one_to_zero)

                         elif sum_of_1s_list_of_0s[j] > (sum_of_1s_list_of_0s[j] - len(counter)):
                              adding_one_to_zero = sum_of_1s_list_of_0s[j] + k
                              break
               


          while sum_of_1s_list_of_0s[i] == 1:
               j = 0
               if sum_of_1s_list_of_0s[j] == 1:
                    counter+=1
                    j+=1
                    if sum_of_1s_list_of_0s[j] > 1:
                         if len(counter) < k:
                              i+=1
                              while sum_of_1s_list_of_0s[i] > 1:
                                   if sum_of_1s_list_of_0s[j] >1:
                                        j+=1
                                        if len(counter) == k:
                                             adding_one_to_zero = sum_of_1s_list_of_0s[i] + k
                                             j+=1




                    while

               elif sum_of_1s_list_of_0s[j] > 1:
                    if sum_of_1s_list_of_0s[j] > nums[sum_of_1s_list_of_0s[j] - len(counter)]:
                         adding_one_to_zero = sum_of_1s_list_of_0s[j] + len(counter)

                    i+=1
                    j+=1