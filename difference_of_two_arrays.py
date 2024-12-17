nums1=[1,2,3]
nums2=[2,4,6]
ints_in_nums1_not_in_nums2=[]
# i is pointing at array nums1
i=0
# j is pointing at array nums2
j=0
# this is where we increment j to check ints in nums1 that are not in nums2
while i<len(nums1) and j<len(nums2):
    counter=0
    while j<len(nums1):
        if nums1[i] != nums2[j]:
            counter+=1
            j+=1
        elif nums1[i] == nums2[j]:
            i+=1
            j=0
            counter=0
    if counter == len(nums2):
        ints_in_nums1_not_in_nums2.append(nums1[i])
    i+=1
    j=0

ints_in_nums2_not_in_nums1=[]
# i is pointing at array nums1
j=0
# j is pointing at array nums2
i=0
# this is where we increment i to check ints in nums2 that are not in nums1
while i<len(nums1) and j<len(nums2):
    counter=0
    while i<len(nums1):
        if nums2[j] != nums1[i]:
            counter+=1
            i+=1
        elif nums2[j] == nums1[i]:
            j+=1
            i=0
            counter=0
    if counter == len(nums1):
        ints_in_nums2_not_in_nums1.append(nums2[j])
    j+=1
    i=0
result=(ints_in_nums1_not_in_nums2 , ints_in_nums2_not_in_nums1)
print (result)
