class menu:
    d={}
    def show(self):
        print("\tMENU\n")
        for i in self.d:
            print(i," ",self.d[i])
    def add(self,st,p):
        self.d[st]=p
c=menu()
c.add("Idly",20)
for i in range(1000):
    st1=str(input("Enter food item:"))
    p1=int(input("Enter cost:"))
    c.add(st1,p1)
    ch=input("Do you wish to continue adding(y/n):")
    if(ch=='n'):
        break
c.show()
