#array of characters called "givencharlist" = ["a","a","b","c","c","c"]

#1st lets count each string and group them. the count wll be
#empty string is called groupedchars=""
#i = 0
#while 1 < len(givencharlist)
#eachchar = givencharlist[i]
#countofeach = givencharlist.count(i)
#if countofeach[i] = 1
#groupedchars.append(eachchar)
#else:
#groupedchars.append(eachchar, countofeach)
#i+=1
#print(groupedchars)
def stringcompression (givencharlist):
    givencharlist = ["a","a","b","c","c","c"]
    groupedchars=[]
    i = 0
    while i < len(givencharlist):
        eachchar = givencharlist[i]
        countofeach = givencharlist.count(eachchar)
        if countofeach == 1:
            groupedchars.append(eachchar)
        elif countofeach > 1:
            groupedchars.append(str(countofeach))
            groupedchars.append(eachchar)
        i+=1
    return(groupedchars)
print (stringcompression(["a","a","b","c","c","c"]))