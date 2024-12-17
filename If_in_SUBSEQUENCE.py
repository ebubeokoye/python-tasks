def subsequence (s, t):
    s= "abc"
    t= "ahbgdc"
    result=[]
    i = 0
    j = 0
    while i < len(s) and j < len (t):
        j+=1
        if s[i] == t[j]:
            result.append (i)
            i+=1
            break
        else:
            j+=1
        j=-1
    i=0
    while i < len(result):
        if result[i] < result[i]+1:
            i+=1
        return (True)
print (subsequence ("abc", "ahbgdc"))