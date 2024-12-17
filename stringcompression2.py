def stringCompression (givenCharList):
    currChar = ""
    charCount = 0
    newList = []
    #using a nested loop (conditionals inside a loop, before the loop ends, at line 18)
    for char in givenCharList:
        if char == currChar:
            charCount += 1
        else:
            if charCount > 1:
                #lets split the char count (eg 10) into each numbers: (1,0) using * syntax,
                #and we cannot split ints, we only split strings. so we use str.
                #we used extend in the first line below because append only takes one item,
                #so extend helps us add both eg(1,0) to the newlist
                newList.extend([* str(charCount)])
            newList.append(char)
            charCount = 1
        currChar = char
    newList.extend([* str(charCount)])
    return newList

print (stringCompression(["a","a","b","c","c","c"]))