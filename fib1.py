class fibo:
    def __init__(self,n=1000):
        self.i=0
        self.a,self.b = 0,1
        self.max = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i>self.max-1:
            raise StopIteration
        self.i+=1
        v = self.a
        self.a,self.b = self.b,self.a + self.b
        return v
n=int(input("Enter the number of terms to be displayed:"))
for i in fibo(n):
    print(i)
