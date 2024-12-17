
#        - then if 
# 2b) for strings with occurence of characters > 1
#         - check that occurences of str1 is in str2 eg(1,2,3,4) is in (3,1,2,4)
# 2c) when a or b above is established, then start swapping i and j,
# based on some conditions of equality with m and n
# 2d) the convert the lists back to strings: new_word1 = "".join(list1), new_word2 = "".join(list2).
# so even when you print new_word1 and new_word2 they are thesame and same arrangement and occurence
 
def if_two_strings_are_close (word1, word2):
    list_word1 = list(word1)
    list_word2 = list(word2)
    # 2) check if the length of list1 is = len list2. if not we cant carry on
    if len(word1) != len(word2):
        return False    
    else:
    #1. check that they are made up of the same characters ie characters in str1 are in str2,
#           by saying: 1<len(word1) for str in word1,  if str in word2: i+=1 else return False
        i=0
        
        while i<len(word1):
            j=0
            if word1[i] == word2[j]:
                i+=1
            else:
                while j<len(word2):
                    if word1[i] != word2[j]:
                        j+=1
                    else: 
                        i+=1
                        break
    

        # 2) lets count the occurence of each char in the word1
        i=0  
        each_char_in_word1 = []
        occurence_of_each_charword1 =[]
        while i<len(word1): 
            j=0
            counter=0
            counter+=1
            compare = word1[i+1:len(word1)]
            if word1[i] in each_char_in_word1:
                i+=1
            else:
                while j<len(compare):
                    if word1[i] == compare[j]:
                        counter+=1
                        j+=1
                    else:
                        j+=1
                occurence_of_each_charword1.append (counter)
                each_char_in_word1.append (word1[i])
                i+=1
           
# 2) lets count the occurence of each char in the word2
        i=0  
        each_char_in_word2 = []
        occurence_of_each_charword2 =[]
        while i<len(word2): 
            j=0
            counter=0
            counter+=1
            compare = word2[i+1:len(word2)]
            if word2[i] in each_char_in_word2:
                i+=1
            else:
                while j<len(compare):
                    if word2[i] == compare[j]:
                        counter+=1
                        j+=1
                    else:
                        j+=1
                occurence_of_each_charword2.append (counter)
                each_char_in_word2.append (word2[i])
                i+=1

#as the have mixed numbers (not only 1) lets check if number in occurence 1 is in occurence2
# else we return false cause simply word1 cannot form word2
        i=0
        j=0
        while i<len(occurence_of_each_charword1):
            j=0
            while j<len(occurence_of_each_charword2):
                if occurence_of_each_charword1[i] != occurence_of_each_charword2[j]:
                    j+=1
                    return False
                else:
                    while i<len(occurence_of_each_charword1):
                        if occurence_of_each_charword1[i] == occurence_of_each_charword2[j]:
                            occurence_of_each_charword2.remove(occurence_of_each_charword2[j])
                            j=0
                            i+=1

        while i == len(occurence_of_each_charword1):
            if len(occurence_of_each_charword2) != 0:
                return False
            else:
# 2a) lets check if the occurence of characters are all = 1 eg (1,1,1)
                i=0
                occurence_of1=[]
                while i <len(occurence_of_each_charword1):
                    if occurence_of_each_charword1[i] == 1:
                        occurence_of1.append(occurence_of_each_charword1[i])
                        i+=1
                    elif len(occurence_of1) == len(occurence_of_each_charword1):

# 2c) when occurence of each number in both words is all 1, then start swapping i and j,
#swap letters in list_word1 so it will match list_word2 at the end of the day
# based on some conditions of equality with m and n.
#we are swapping only when i!= m
                        i=0
                        j=i+1
                        m=0
                        n=m+1
                        while i<len(list_word1)-1 and m<len(list_word2)-1:
                            while j<len(list_word1) and n<len(list_word2):
                                if list_word1[i] != list_word2[m]:
                                    if word1[j] != word2[n]:
                                        list_word1[i], list_word1[j] = list_word1[j], list_word1[i]
                                        if list_word1[i] == list_word2[m]:
                                            i+=1
                                            m+=1
                                            j+=1
                                            n+=1
                                        elif list_word1[i] != list_word2[m]:
                                            i+=1
                                            m+=1
                                    else:
                                        j+=1
                                        n+=1
                                else:
                                    i+=1
                                    m+=1
    # when occurence of some numbers in list_word1 is more than 1,
    #we will swap the letters in list_word1,
    # so that it is grouped, eg: a,a,b,b,c,c,c
                    else:
                        i=0
                        while i<len(list_word1)-1:
                            j=i+1
                            
                            while j<len(list_word1):
                                if list_word1[i] == list_word1[j]:
                                    list_word1[j], list_word1[i+1] = list_word1[i+1], list_word1[j]
                                    j+=1
                                else:
                                    j+=1
                            i+=1
# definitely, occurence of numbers in occurence_of_each_charword2 are not all 1
# so we will swap the letters in list_word2,
# so that it is grouped, eg: b,b,c,c,a,a,a
 
                        i=0
                        while i<len(list_word2)-1:
                            j=i+1
                            
                            while j<len(list_word2):
                                if list_word2[i] == list_word2[j]:
                                    list_word2[j], list_word2[i+1] = list_word2[i+1], list_word2[j]
                                    j+=1
                                else:
                                    j+=1
                            i+=1
#now lets count each grouped chars in list_word1
                        i=0
                        list_word1_groupedchars_counted=[]
                        while i <len(list_word1):
                            counter+=1
                            compare = list_word1[i+1:len(list_word1)]
                            j=0
                            while j<len(compare):
                                if list_word1[i] == compare[j]:
                                    counter+=1
                                    j+=1
                                else:
                                    j+=1
                            list_word1_groupedchars_counted.append(counter)
                            i+=1
#lets count each grouped chars in list_word1
                        i=0
                        list_word1_groupedchars_counted=[]
                        while i <len(list_word1):
                            counter+=1
                            compare = list_word1[i+1:len(list_word1)]
                            j=0
                            while j<len(compare):
                                if list_word1[i] == compare[j]:
                                    counter+=1
                                    j+=1
                                else:
                                    j+=1
                            list_word1_groupedchars_counted.append(counter)
                            i+=1
# this is time to swap  
                        i=0
                        j=0
                        arr2 = [None] * len(list)
                        while i<len(list_word1):
                            while j<len(list_word2):
                                for i in range 
                                if list_word1[i] == list_word2[j]:
                                    i+=1
                                    j+=1
                                else:
                                    replacement = list_word1("list_word1[i]", )

# lets now verify our result
        m=0
        while j<len(word1) and n<len(word2):
            j=i+1
            n=m+1
            if word1[i] == word2[m]:
                if word1[j] == word2[n]:
                    j+=1
                    n+=1
        return True
        
word1 = "cabbba"
word2 = "abbccc"
print (if_two_strings_are_close (word1, word2)) 
