def if_two_strings_are_close (word1, word2):
    word1 = "abc"
    word2 = "bca"
# 1) check if the length of list1 is = len list2. if not we cant carry on
    if len(word1) != len(word2):
        return False    
    else:
         return True
word1 = "abc"
word2 = "bca"
print (if_two_strings_are_close (word1, word2))