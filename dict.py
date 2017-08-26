def convert(string):
	d=dict(string.split('=') for string in string.split(';'))
	return d;
st=input("Enter string:")
d=convert(st)
print(d)
