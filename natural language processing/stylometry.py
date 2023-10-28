fedaralist_by_author={}
with open("Hamilton.txt") as f:
    a=f.read()
    fedaralist_by_author['Hamilton']=a
with open("Madison.txt") as f1:
    b=f1.read()
    fedaralist_by_author['Madison']=b
with open("Jay.txt") as f2:
    c=f2.read()
    fedaralist_by_author['Jay']=c
with open("Hammad.txt") as f3:
    d=f3.read()
    fedaralist_by_author['Shared']=d
with open("Unknown.txt") as f4:
    z=f4.read()
    fedaralist_by_author['Unknown']=z
print(fedaralist_by_author)

