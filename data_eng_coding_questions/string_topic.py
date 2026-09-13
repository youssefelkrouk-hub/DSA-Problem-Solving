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

# for time complexity  : O(n)
# for space complexity : O(n)
# cont the number of Vowells  in a String !!


def count_vowelles(s):
    Vowells="aeiouAEIOU"
    return sum(1 for c in s if c in Vowells)

k='Hello World'
print(k.title()==k.strip())
print(count_vowelles(k),"\n") 


# .strip() method : Removes leading and trailing whitespace
# .title() method : capitalizes the first letter of each word, and lowercases the rest of each word.

# the None kayword mean  no value here , for that if you want to check 
# a value doesn't exit you compare it with None 



seq='CCA-TGC-GCAA-TA'
parts=seq.split('-') # .split() usually return a list ,by default seperate value is the space 
print(parts)  # return ['CCA', 'TGC', 'GCAA', 'TA']

parts_joins=''.join(parts)
print("to join all the word int the list we use .join method instead of looping and creating a new one:",parts_joins,"\n")
