#------> The code ascii of an array 

# -----> You are given a string s. 
# -----> The score of a string is 
# -----> defined as the sum of the absolute difference 
# -----> between the ASCII values of adjacent characters.

#---->  Return the score of s.
print("the code asci of the A is ",ord('A'))
# the zip function iterate trough tow list:
L=[1,2,3,4]
N=[3,4,6,8]
for s1,s2 in zip(N,L):
    print((s1,s2))

print("\n")

def string_score(s):
    output=0
    for i in range(len(s)-1):
        output+=abs(ord(s[i])-ord(s[i+1]))
    return output

s="hello"
print(string_score(s))

# on a one line of code using the zip function 

def string_score_2(s):
    return sum(abs(ord(s1)-ord(s2)) for s1,s2 in zip(s,s[1:]))


l="hello"
print(string_score_2(l))






