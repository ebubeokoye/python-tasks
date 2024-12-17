
    i=0
    j=i+1
    k = 2
    counter = 0
    adding_zeroes_infront = []
#adding zeros infront to values > 1
#when i and j are pointing at zeroes converted to 1s, that is when we use the counter
while i <len(sum_of_1s_list_of_0s) and j <len(sum_of_1s_list_of_0s):
        if sum_of_1s_list_of_0s[i] == 1:
                while sum_of_1s_list_of_0s[j]==1:
                        counter+=1
                        j+=1
                        if len(counter) < k:
                            while sum_of_1s_list_of_0s[j]>1:   
                                actual_sum_of_1s_list_of_0s = sum_of_1s_list_of_0s[i] + len(counter) + sum_of_1s_list_of_0s[j]
                                adding_zeroes_infront.append (actual_sum_of_1s_list_of_0s)
                                  
                        elif len(counter) >= k:
                            while sum_of_1s_list_of_0s[j]>1:
                                adding_zeroes_infront.append (sum_of_1s_list_of_0s[i])
                                actual_sum_of_1s_list_of_0s = sum_of_1s_list_of_0s[j] + k
                                adding_zeroes_infront.append (actual_sum_of_1s_list_of_0s)
                              
                i=j+1
                j=i+1
        elif sum_of_1s_list_of_0s[i] > 1:
                adding_zeroes_infront.append (sum_of_1s_list_of_0s[i])
        i+=1
        j+=1
i=0
j=i+1
k=2
counter=0
adding_zeroes_behind = []
#adding zeros behind to values greater than ones
#i is pointing at values greater than ones and j at 1, then increase counter
while i <len(sum_of_1s_list_of_0s) and j <len(sum_of_1s_list_of_0s):
    if sum_of_1s_list_of_0s[i] > 1:
        while sum_of_1s_list_of_0s[j]==1:
            counter+=1
            j+=1
            if len(counter) <= k:
                while sum_of_1s_list_of_0s[j]>1:
                    actual_sum_of_1s_list_of_0s = sum_of_1s_list_of_0s[i] + len(counter)
                    adding_zeroes_behind.append (actual_sum_of_1s_list_of_0s)

            elif len(counter) > k:
                while sum_of_1s_list_of_0s[j]>1:
                    actual_sum_of_1s_list_of_0s = sum_of_1s_list_of_0s[i] + k
                    adding_zeroes_behind.append (actual_sum_of_1s_list_of_0s)
                    adding_zeroes_behind.append (sum_of_1s_list_of_0s[j-1])
        i=j
        j=i+1
    elif sum_of_1s_list_of_0s[i] == 1:
         adding_zeroes_behind.append (sum_of_1s_list_of_0s[i])
    i+=1
    j+=1  

j=0
i=j+1
l=j-1
k=2
counter_l=0
counter_i=0
adding_zeroes_front_back = []
#adding zeros behind and infront of values greater than ones
#i is pointing to the zeroes behind and l to the zeroes in front converted to 1s,
# j is pointing to values >1 , then increment counter
while j <len(sum_of_1s_list_of_0s):
    if sum_of_1s_list_of_0s[j] > 1:
        i=j+1
        l=j-1
        while sum_of_1s_list_of_0s[i]==1:
            counter_i+=1
            i+=1
        while sum_of_1s_list_of_0s[l]==1:
            counter_l+=1
            l-1
            if len(counter_i) <= k:
                while sum_of_1s_list_of_0s[i]>1:
                    actual_sum_of_1s_list_of_0s = sum_of_1s_list_of_0s[j] + len(counter_i)
                    adding_zeroes_front_back.append (actual_sum_of_1s_list_of_0s)
            elif len(counter) > k:
                while sum_of_1s_list_of_0s[i]>1:
                    actual_sum_of_1s_list_of_0s = sum_of_1s_list_of_0s[j] + k
                    adding_zeroes_front_back.append (actual_sum_of_1s_list_of_0s)


    elif sum_of_1s_list_of_0s[j] == 1:
         j+=1