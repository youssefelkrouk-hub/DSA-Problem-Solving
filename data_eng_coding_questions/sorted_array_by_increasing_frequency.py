nums=[1,2,3,2]
counts={}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
print(counts)
# this is a dictionary of each number with his occurence : !!
print("Another way to count:","\n")
counts2={}
for num in nums:
    if num in counts2:
        counts2[num]+=1
    else:
        counts2[num]=1
print(counts2,"\n")
# en utilisant la bibliothéque collections ! :
from collections import Counter
counts3 = Counter(nums)
print(counts3)
print(sorted(nums,key=lambda n:-counts3[n] ))
# to return the frquence of each number in the counter dictionary !!: 
for num in nums:
    print(counts3[num])

print("\n")
# the problem is to sort this array by the frequence :  the first solution , we don't care about ties values 
# the first method is by using a Lambda function !! 
def sorting_increasing(nums):
    counts=Counter(nums) # this a hash og frequencies , we can implement  using the.get() method 
    return sorted(nums,key=lambda n : -counts[n]) # sorting by considering the descreasing frequencies !!

print(sorting_increasing([2,3,1,3,2]))

    


