#  i wille use a DP aproach , i will create an array that will contain each value that  i will need to 
# calculate fib(n)=fibo(n-1)+fibo(n-2)

def fibonacci(n):
    #fibo(n)=fibo(n-1)+fibo(n-2)
    fibo=[0]*(n+1)
    fibo[0]=1
    fibo[1]=1
    for i in range(2,n+1):
        fibo[i]=fibo[i-2]+fibo[i-1]
    return fibo[n]

print(fibonacci(4))

# but time complexity is : O(n)
# space complexity is : O(n) i use an extra memory which is an array 

# more optimized solution without extra memory ::
print("\n")
print("more optimized solution without extra memory :")
def fibo(n):
    a,b=1,1
    for i in range(n-1):
        a,b=a,a+b
    return b 

print(fibo(5))
