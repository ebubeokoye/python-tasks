# starting altitude = 0 on point n = 0
# altitudes = [0,-5,-4,1,1,-6], so for altitude -5 point n = 1
# for altitude -4 point n = 2
#the points = n + 1 ie 0,1,2,3,4

#now lets calculate the different altitudes ie the 'gain'
#integer array gain = [-5,1,5,0,-7] of length n
# for gain = -5, net gain in altitude = altitude at point i - altitude at point i+1
#if gain = 2,3,4 altitude = 9,5,2,0 then we  reverse it to be 2,5,9 and insert the starting altitiude 0 at position0
# gain = [-4,-3,-2,-1,4,3,2] altitude = 0,-4,-7,-9,-10,-6,-3,-1

altitudes = []
gain = [-4,-3,-2,-1,4,3,2]   
i=len(gain)-1
while i > -1:
    x=i+1
    curr_gain = gain[0:x]
    sum_gain = sum(curr_gain)
    altitudes.append(sum_gain)
    i-=1
altitudes.reverse()
altitudes.insert(0,0)
#print (sum_list)
print (altitudes)