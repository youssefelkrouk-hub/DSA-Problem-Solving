# how to extract the digit of each number that we have in a input : !!
# some manipulation , after the goal problem


print(123%10) # this is 123 = 3 modulo[10] , the "%" return this result of this modulo 
print(123//10) # division with just  without the float part  , 123//10=12 not 12,3
print(123/10) # floating-point division
print("\n")

def get_digit(n):
    while n!=0:
        digit=n%10
        print(digit)
        n=n//10
print(get_digit(123))  
print("\n")

# define a helper function that will help me to solve the happy number problem : 

print("\n")

def sequare_digit(n):
    sequare_digit=0
    while n!=0:
        sequare_digit+=(n%10)**2
        n=n//10
    return sequare_digit
print(sequare_digit(12))  # this will return 2**2+1=5

# the first solution using a  hash set : 
# the intuition is to detect a  cycle , if a sequare  sum of dgit is already in the set and it's not equal to 1,then it's not a happy number

def happy_number(n):
    hash_set=set()
    if n==1:return True
    else:
        while n not in hash_set:
            hash_set.add(n)
            n=sequare_digit(n) 
        return False
print(happy_number(19))
