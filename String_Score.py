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
print(string_score_2(l),"\n")
print(chr(65))  #it return A  : 
print(ord(' ')) # it return 32 : 
print(chr(36),"\n")  # $


char='Z'
print(chr(ord(char)+32))  # transform into the lower format !! 


s="YOOUSSEF"
print(s.lower(),"\n") 
print(s.lower()[::-1],"\n") # give the backwords of s
h="youssef"
print(h.upper(),"\n") # the opposite function of lower()
# Check if plandrome 
# a plandrome is a string that reads the same forwards and backwards !!


def is_plandrome(s):
    lowerd=s.lower() # lower create a new string  , that contain only the lower version of each charachter 
    return lowerd==lowerd[::-1]

s = "Racecar"
# s[0]="S" !! --> 'str' object does not support item assignment
print(is_plandrome(s)) # return True regadless of the format of characters in s , lower or upper
# for time complexity  


