#where there are numbers in array indexes=[x,y,z] i want to return the value of: [y*z, x*z, x*y]
#i will give each number a position [0, 1, 2] and append to a new list called indexesofnumbers[]
#and simultaneously in the same loop append the numbers to a new list called indexednumbers[]
#indexesofnumbers[]
#indexednumbers
   #i=0
   # while i < len(indexes):
   #numbersinindex = indexes[i]
   #indexesofnumbers.append(i)
   #indexednumbers.append(numbersinindex)
   #i+=1
#now let me intrapolate the indexesofnumbers[0,1,2] and indexednumbers[x,y,z] lists using loop:
   #i=o
   #while i < len(indexednumbers):
   #positionsinindexednumbers = indexesofnumbers[i]
   #(next line below means: for one of the indexes x,y,z  its equal to position i=0 in indexesofnumbers)
   #indexes[positionsinindexednumbers] = indexednumbers[i]
   #i+=1
   #return''.join(indexes)

#now lets multiply accordingly: for indexes[x,y,z], products=[yz, xz, xy],
# and append to a new list called answer[]

   #i=0
   #while i < len(charinindexednumbers):
   #for char in charinindexednumbers:
   #if char = charinindexednumbers[i]:
   #productofchars = charinindexednumbers[i:] * charinindexednumbers[i:]
   #i+=1
#return
   #answer.append(sumofproduct)
   #print(" ".join(productofchars))
