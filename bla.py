nums= [1,2,3,4,5]
i=0
hastriple=False
while i <len(nums)-2:
 if nums[i]<nums[i+1]<nums[i+1+1]:
  i+=1
  hastriple=True
 if hastriple==True:
  break
print(hastriple) 