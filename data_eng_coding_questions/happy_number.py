# how to extract the digit of each number that we have in a input : !!
# some manipulation , after the goal problem

def get_digit(n):
    while n>0:
        digit=n%10
        print(digit)
        n=n//10

#print(get_digit(123))
print(123%10)