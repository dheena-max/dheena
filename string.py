n=input()
a=[]
b=[]
for i in n:
    if i not in a:
        a.append(i)
    elif(i in a):
        b.append(len(a))
        a=[]
b.append(len(a))
print(max(b))
