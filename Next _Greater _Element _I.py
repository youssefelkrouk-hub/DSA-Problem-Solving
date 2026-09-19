# let's implement the next greater element in a array , using a monotonic stack : 


def nge(nums):
    n = len(nums)
    res = [0] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]   # top of stack = next greater element
        else:
            res[i] = -1          # nothing greater found
        stack.append(nums[i])    # push current element for future comparisons
    return res

print(nge([4, 5, 2, 25]))


# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



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

# antoher brute force aproach using less more extra  memory : 
print("\n")
def nextgreatelt(nums1, nums2):
    result = [-1]*(len(nums1))
    for index,x in enumerate(nums1):
        pos = nums2.index(x)
        for k in range(pos + 1, len(nums2)):
            if nums2[k] > x:
                result[index]=nums2[k]
                break
    return result

nums1=[4,1,2]
nums2=[1,3,4,2]
print(nextgreatelt(nums1,nums2))

