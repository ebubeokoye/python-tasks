def unique_number_of_occurences (arr):
    # this array will be used to compare integers coming in to see if they already exist in it
    single_number_from_each_group=[]
    identicals_on_the_right=[]
    k=0
    i=0
    j=i+1
    # j is searching for the repetitions of the value at index i
    while i<len(arr):
        j=1+1
        counter=0
        if i == 0:
            single_number_from_each_group.append(arr[i])
            counter+=1
            while j<len(arr):
                if arr[j] == arr[i]:
                    counter+=1
                    j+=1
                elif arr[j] != arr[i]:
                    j+=1
            identicals_on_the_right.append(counter)
            counter=0
        
        for number in arr :
                j=i+1
                k=0
                if number in single_number_from_each_group:
                    k+=1
                    i+=1
                else:
                    counter+=1
                    single_number_from_each_group.append(number)
        
                    while i<len(arr)-1:
                        j=i+1
                        while j<len(arr):
                            if arr[i] == arr[j]:
                                counter+=1
                                j+=1
                            elif arr[i] != arr[j]:
                                j+=1 
                        break 
                    identicals_on_the_right.append(counter)   
                    i+=1
                    j=i+1
                    counter=0
    
    i=0
    while i<len(identicals_on_the_right)-1:
        j=i+1
        while j<len(identicals_on_the_right):
            if identicals_on_the_right[i] != identicals_on_the_right[j]:
                j+=1
            else:
                return False
        i+=1
    return True
    
arr = [-3,0,1,-3,1,1,-3,10,0]
print (unique_number_of_occurences (arr))