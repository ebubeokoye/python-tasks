#define a function that takes two strings
def getcommonletters (str1, str2):
    # then create an empty string where the intersecting characters are put
    commonletters = ""
    
    for str in str1:
        if str in str2:
         return "".join(sorted(set(str1) & set(str2)))
        
str1 = "ABCTEF"
str2 = "ABC"
commonletters = getcommonletters (str1, str2)
print (commonletters)