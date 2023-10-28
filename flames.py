def count(n1,n2):
    for i in n1:
        for j in n2:
            if i==j:
                n1=n1.replace(i,'',1)
                n2=n2.replace(j,'',1)
                break;
    l=len(n1)+len(n2)
    print(l)
    return l
def predict(c):
    tar=c
    f="flames"
    len3=len(f)
    i=0
    index=0
    k=0
    while(i<=4):
        if(k>0):
            tar=tar-index
        k=tar%len3
        f=f.replace(f[k-1],'')
        index=len3-k
        len3=len3-1
        i=i+1
        tar=c
    return f
flames={'f':'Friendship','l':'Love','a':'Affection','m':'Marriage','e':'Enemy','s':'Sister'}
pn1=input("Enter Your Name: ")
pn2=input("Enter Your Partner Name: ")
pn1.replace(" ","")
pn2.replace(" ","")
pn11=pn1.upper()
pn22=pn2.upper()
c=count(pn11,pn22)
p=predict(c)
print("Hey...",pn11,"and",pn22,"...Your Relationship Prediction is",flames[p])