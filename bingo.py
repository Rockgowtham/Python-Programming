import numpy
import random

def bingo_check(pn1,pn2,b1,b2):
    bc1=0
    bc2=0
    c1=0
    c2=0
    for r in range(5):
        for c in range(5):
            if(b1[r][c]=='x'):
                c1=c2+1
            if(b2[r][c]=='x'):
                 c2=c2+1
        if(c1==5):
            bc1=bc1+1
        if(c2==5):
            bc2=bc2+1
        c1=0
        c2=0
    for cc1 in range(5):
         for r1 in range(5):
             if(b1[r1][cc1]=='x'):
                 c1=c2+1
             if(b2[r1][cc1]=='x'):
                  c2=c2+1
         if(c1==5):
             bc1=bc1+1
         if(c2==5):
             bc2=bc2+1
         c1=0
         c2=0
    if(b1[0][0]==b1[1][1] and b1[1][1]==b1[2][2] and b1[2][2]==b1[3][3] and b1[3][3]==b1[4][4] and b1[2][2]=='x'):
         bc1=bc1+1
    if(b1[0][4]==b1[1][3] and b1[1][3]==b1[2][2] and b1[2][2]==b1[3][1] and b1[3][1]==b1[4][0] and b1[2][2]=='x'):
         bc1=bc1+1
    if(b2[0][0]==b2[1][1] and b2[1][1]==b2[2][2] and b2[2][2]==b2[3][3] and b2[3][3]==b2[4][4] and b2[2][2]=='x'):
         bc2=bc2+1
    if(b2[0][4]==b2[1][3] and b2[1][3]==b2[2][2] and b2[2][2]==b2[3][1] and b2[3][1]==b2[4][0] and b2[2][2]=='x'):
         bc2=bc2+1
    if(bc1>=5 and bc2>=5):
         print(pn1,"and",pn2,"...Win")
    if(bc1>=5):
         print(pn1,"...Won")
         return True
    if(bc2>=5):
         print(pn2,"...Won")
         return True
    return False
    
        
inpl=[]
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
pn1=input("Player-01 Please Enter Your Name: ")
pn2=input("Player-02 Please Enter Your Name: ")
board=numpy.array([['--','--','--','--','--'],['--','--','--','--','--'],['--','--','--','--','--'],['--','--','--','--','--'],['--','--','--','--','--']])
for r in range(0,5):
    for c in range(0,5):
        d=random.choice(l)
        board[r][c]=d
        l.remove(d)
board2=numpy.array([['--','--','--','--','--'],['--','--','--','--','--'],['--','--','--','--','--'],['--','--','--','--','--'],['--','--','--','--','--']])
for r in range(0,5):
    for c in range(0,5):
        e=random.choice(l1)
        board2[r][c]=e
        l1.remove(e)
print(pn1," Bingo Board:")
print(numpy.matrix(board))
print()
print(pn2," Bingo Board:")
print(numpy.matrix(board2))
for i in range(0,25):
    if(i%2==0):
        inp=input("Player 1 Please Enter Your Choice: ")
        
    else:
        inp=input("Player 2 Please Enter Your Choice: ")
        
    if inp not in inpl:
        inpl.append(inp)
        for r in range(5):
            for c in range(5):
                if(board[r][c]==inp):
                    board[r][c]='x';
                if(board2[r][c]==inp):
                    board2[r][c]='x';
        print(pn1," Bingo Board:")
        print(board)
        print(pn2," Bingo Board:")
        print(board2)
        if(bingo_check(pn1,pn2,board,board2)):
            break;
    else:
        print("Number already Exists")
    