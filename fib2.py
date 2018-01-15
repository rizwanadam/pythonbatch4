def fibo(n):
    ls=[0,1]
    i=1
    while i<n-1:
        i=i+1
        ls.append(ls[i-1]+ls[i-2])
    return ls;
n=int(input("Enter the number of terms:"))
for i in fibo(n):
    print(i)
    