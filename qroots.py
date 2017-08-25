import cmath
def quad(a,b,c,d):
	if(d==0):
		r1=(-b/(2*a))
		r2=(-b/(2*a))
		return r1,r2;
	else:
		r1=(-b-cmath.sqrt(d))/(2*a)
		r2=(-b+cmath.sqrt(d))/(2*a)
		return r1,r2;

print("ax^2+bx+c")	
a=float(input('Enter a:'))
b=float(input('Enter b:'))
c=float(input('Enter c:'))
if a==0:
    print ("The equation is linear")
else:
    d=b**2-4*a*c
    r1,r2=quad(a,b,c,d)
    print ("The roots are ",r1," and ",r2)
    

