import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
pname1=input("Player-1 Please Enter Your Name: ")
pname2=input("Player-2 Please Enter Your Name: ")
ps1='x'
ps2='o'
print(pname1," Symbol is ",ps1)
print(pname2," Symbol is ",ps2)

def check_rows(name,symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if(board[r][c]==symbol):
                count=count+1
        if(count==3):
            print(name," Won...!")
            return True
    return False

def check_col(name,symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if(board[r][c]==symbol):
                count=count+1
        if(count==3):
            print(name," Won...!")
            return True
    return False

def check_diagonals(name,symbol):
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol):
        print(name," Won...!")
        return True
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol):
        print(name," Won...!")
        return True
    else:
        return False
    

def won(name,symbol):
    return check_rows(name,symbol) or check_col(name,symbol) or check_diagonals(name,symbol)

def place(name,symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter Row Position(1 or 2 or 3): "))
        col=int(input("Enter Column Position(1 or 2 or 3): "))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            board[row-1][col-1]=symbol
            break
        else:
            print(name," ,It is Invalid Input...Please Enter Valid Row and Column...")

def play():
    c=0
    for i in range(9):
        if(i%2==0):
            print(pname1," Turn...")
            place(pname1,ps1)
            if won(pname1,ps1) and i>=4:
                print(numpy.matrix(board))
                c=1
                break
        if(i%2!=0):
            print(pname2," Turn...")
            place(pname2,ps2)
            if won(pname2,ps2) and i>=4:
                print(numpy.matrix(board))
                c=1
                break
    if(c==0):
        print("Match Drawn")

play()

    

    
            
        