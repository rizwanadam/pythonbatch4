def dict_to_str(d):
    st=''
    for i in d:
        st+=i+"="+d[i]+";"
    return st;
n=int(input("Enter the number of keys:"))
d={}
for i in range(n):
    i=input("Enter key:")
    d[i]=input("Enter value:")
stt=dict_to_str(d)
print(stt)

