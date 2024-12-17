# to use the append method create 2 pointers for the 2 words. 0 points at the first letter, i=1 then points at the second.etc
def getmergealternately (str1, str2):

    mergealternately= ""

    i = 0
    j = 0

    #then i'll write the while loop
    while i < len(str1) and j < len(str2):
        # appending the character in str1 and str2 to my empty mergealternately incrementally (+=) list and increment the pointers
        mergealternately+= str1[i] + str2[j]
        i += 1
        j += 1
        #then i'll just append the remaining characters in str1 and str2 ie "stuv"
    mergealternately += str1[i:] + str2[j:]

    return mergealternately 

str1 = "abc"
str2 = "pqrstuv"
#define mergealternately
mergealternately = getmergealternately(str1, str2)
print (mergealternately)