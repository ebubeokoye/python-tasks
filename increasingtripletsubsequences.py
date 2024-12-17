nums= [5,4,3,2,1]
i=0
hastriple=False
while i <len(nums)-2:
  if nums[i]<nums[i+1]<nums[i+1+1]:
    hastriple=True
  if hastriple==True:
    break
  i+=1
print(hastriple) 