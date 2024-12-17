from functools import reduce
numbs = [1,2,3,4]
result=[]
i=0
while i < len(numbs):
        result.append(reduce(lambda x,y: x*y, numbs)/numbs[i])
        i+=1
print(result)


