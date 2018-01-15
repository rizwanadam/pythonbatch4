def fibo(max):
    a,b=0,1
    i=0
    while i<max:
        yield a
        a,b=b,a+b
        i+=1
    return a
n=int(input("Enter the number of terms to be displayed:"))
for i in fibo(n):
    print(i)
