class Error(Exception):
    pass
class menu:
    def __init__(self):
        self.d={}
    def show(self):
        print("\tMENU\n")
        for i in self.d:
            print(i," ",self.d[i])
    def add(self,st,p):
        self.d[st]=p
class order():
    def __init__(self,me):
        self.d1={}
        self.d=me.d
    def placeo(self,st1,qt):
        try:
            self.d[st1]
            self.d1[st1]=qt
        except:
            raise(Error(st1,'is not in the menu'))
    def disporder(self):
        tot=0
        print("Order\tQuantity\tPrice")
        for i in self.d1:
            print(i,"\t",self.d1[i],"\t\t",self.d1[i]*self.d[i])
            tot+=self.d1[i]*self.d[i]
        print("\nThe total cost is ",tot)
c=menu()
c.add("Idly",20)
for i in range(1000):
    st1=str(input("Enter food item:"))
    p1=int(input("Enter cost:"))
    c.add(st1,p1)
    ch=str(input("Do you wish to continue adding(y/n):"))
    if(ch=='n'):
        break
c.show()
o=order(c)
for i in range(100):
    s=str(input("Enter order from the menu:"))
    q=int(input("Enter quantity:"))
    o.placeo(s,q)
    c1=str(input("Do you wish to order more(y/n):"))
    if(c1=='n'):
        break
o.disporder()
