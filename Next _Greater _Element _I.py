def nextGreaterElement(nums1, nums2):
    res=[-1]*(len(nums1))
    hash_map={}
    for index,elt in enumerate(nums1):
        hash_map[elt]=index

    for elt1 in hash_map:
        for jindex,elt2 in enumerate(nums2):
            if elt1==elt2:
                for d in range(jindex,len(nums2)):
                    if nums2[d]>elt1:
                        res[hash_map[elt1]]=nums2[d]
                        break #<-- stop at the FIRST greater element
                break # elt1 found in nums2, no need to keep scanning outer loop 
    return res

n1=[4,1,2]
n2=[1,3,4,2]
print(nextGreaterElement(n1,n2))

# this a brute force a  proach , where time complexity if O(n*msquare) and space complexity is O(n)