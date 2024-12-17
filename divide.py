list1 = "ABCABC"
list2 = "ABC"

#converting them to sets to find the common words
common_words = set(list1).intersection (set(list2))
print(common_words)