from functools import reduce
numbs = [1,2,3,4]
result=[]
i=0
while i < len(numbs):
       for number in numbs:
        product = reduce(lambda x,y: x*y, numbs)
        dividing = product/numbs[i]
        result.append(dividing)
        i+=1
print(result)