#  i wille use a DP aproach , i will create an array that will contain each value that  i will need to 
# calculate fib(n)=fibo(n-1)+fibo(n-2)

def fibonacci(n):
    #fibo(n)=fibo(n-1)+fibo(n-2)
    
    if n==0:
        return 0
    if n==1:
        return 1
    fibo=[0]*(n+1)
    fibo[0]=1
    fibo[1]=1
    for i in range(2,n+1):
        fibo[i]=fibo[i-2]+fibo[i-1]
    return fibo[n]


print(fibonacci(4))