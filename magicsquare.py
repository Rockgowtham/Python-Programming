def magic_square(n):
    magicsquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicsquare.append(l)
        
    r=int(n/2)
    c=n-1
    num=n*n
    count=1
    while(count<=num):
        if(r==-1 and c==n):
            r=0
            c=n-2
        if(r==-1 or c==n):
            if(r==-1):
                r=n-1
            if(c==n):
                c=0
        if(magicsquare[r][c]!=0):
            r=r+1
            c=c-2
        
        magicsquare[r][c]=count
        r=r-1
        c=c+1
        count=count+1
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j], end=" ")
        print()
    
        

