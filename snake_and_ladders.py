import random
from PIL import Image
end=100
def show_board():
    img=Image.open("image.png")
    img.show()
  
def check_ladder(p):
    if p==8:
        print("Ladder")
        return 26
    if p==21:
        print("Ladder")
        return 82
    if p==43:
        print("Ladder")
        return 77
    if p==50:
        print("Ladder")
        return 91
    if p==54:
        print("Ladder")
        return 93
    if p==62:
        print("Ladder")
        return 96
    if p==66:
        print("Ladder")
        return 87
    if p==80:
        print("Ladder")
        return 100
    return p

def check_snake(p):
    if p==44:
        print("Snake")
        return 22
    if p==46:
        print("Snake")
        return 5
    if p==48:
        print("Snake")
        return 9
    if p==52:
        print("Snake")
        return 11
    if p==55:
        print("Snake")
        return 7
    if p==59:
        print("Snake")
        return 17
    if p==64:
        print("Snake")
        return 36
    if p==69:
        print("Snake")
        return 33
    if p==73:
        print("Snake")
        return 1
    if p==83:
        print("Snake")
        return 19
    if p==92:
        print("Snake")
        return 51
    if p==95:
        print("Snake")
        return 24
    if p==98:
        print("Snake")
        return 28
    return p

def reached_end(p):
    if(p==100):
        return True
    return False
    
def play():
    p1_name=input('Player-1...Please Enter Your Name: ')
    p2_name=input('Player-2...Please Enter Your Name: ')
    pp1=0
    pp2=0
    turn=0
    d1=0
    d2=0
    while(1):
        if(turn%2==0):
            print(p1_name,"...This is Your Turn!")
            print()
            c=int(input("Press 1 to Continue and 0 to Quit "))
            print()
            if c==0:
                print(p1_name," Scored ",pp1)
                print()
                print(p2_name," Scored ",pp2)
                print()
                print("Qutting the Game...Thanks for Playing...")
                break
            dice=random.randint(1,6)
            print("Dice Showed: ",dice)
            print()
            if(dice==6):
                d1=d1+1
            if(d1>0):
                pp1=pp1+dice
                pp1=check_ladder(pp1)
                pp1=check_snake(pp1)
                if(pp1>end):
                    pp1=pp1-dice
                print(p1_name," Your Score: ",pp1)
                print()
                if reached_end(pp1):
                    print(p1_name,"...Won")
                    break
            else:
                print("Roll 6 to Move From 0")
                print()
                print(p1_name," Your Score: ",pp1)
                print()
        else:
            print(p2_name,"...This is Your Turn!")
            print()
            c=int(input("Press 1 to Continue and 0 to Quit "))
            print()
            if c==0:
                print(p1_name," Scored ",pp1)
                print()
                print(p2_name," Scored ",pp2)
                print()
                print("Qutting the Game...Thanks for Playing...")
                print()
                break
            dice=random.randint(1,6)
            print("Dice Showed: ",dice)
            print()
            if(dice==6):
                d2=d2+1
            if(d2>0):
                pp2=pp2+dice
                pp2=check_ladder(pp2)
                pp2=check_snake(pp2)
                if(pp2>end):
                    pp2=pp2-dice
                print(p2_name," Your Score: ",pp2)
                print()
                if reached_end(pp2):
                    print(p2_name,"...Won")
                    break
            else:
                print("Roll 6 to Move From 0")
                print()
                print(p2_name," Your Score: ",pp2)
                print()
                
        turn=turn+1
show_board()
play()