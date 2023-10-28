
import random

def choose():
    word_list = [
    "banana",
    "sunset",
    "eleven",
    "guitar",
    "octopus",
    "chicken",
    "butter",
    "computer",
    "kangaroo",
    "keyboard",
    "elephant",
    "blanket",
    "whisper",
    "diamond",
    "umbrella",
    "cucumber",
    "monster",
    "flamingo",
    "baseball",
    "rainbow",
    "chocolate",
    "peacock",
    "birthday",
    "treasure",
    "jupiter",
    "hamburger",
    "carousel",
    "pineapple",
    "suitcase",
    "raindrop",
    "dolphin",
    "crocodile",
    "waterfall",
    "fireworks",
    "campfire",
    "backpack",
    "penguin",
    "butterfly",
    "caterpillar",
    "sunflower",
    "umbrella",
    "sunrise",
    "sunshine",
    "vampire",
    "telephone",
    "whale",
    "rocket",
    "parrot",
    "cinnamon",
    "honeybee",
    "lighthouse",
    "jellyfish",
    "kitchen",
    "bicycle",
    "telephone",
    "strawberry",
    "chimpanzee",
    "watermelon",
    "accordion",
    "hurricane",
    "volcano",
    "mosquito",
    "astronaut",
    "crystal",
    "bouquet",
    "alligator",
    "marathon",
    "scorpion",
    "giraffe",
    "mermaid",
    "platypus",
    "spaceship",
    "triangle",
    "airplane",
    "lobster",
    "walrus",
    "mailbox",
    "painting",
    "quilt",
    "ocean",
    "mosquito",
    "coconut",
    "sunburn",
    "balloon",
    "dragonfly",
    "sweater",
    "mushroom",
    "carousel",
    "crayon",
    "ketchup",
    "zucchini",
    "xylophone",
    "waterfall"]
    
    main=random.choice(word_list)
    return main

def jumble(w):
    s="".join(random.sample(w,len(w)))
    return s

def thank(pn1,pn2,p1,p2):
    print(pn1," Your Score is ",p1)
    print(pn2," Your Score is ",p2)
    if(p1>p2):
        beat=p1-p2
        print(pn1," Beats ",pn2," by",beat," Points...")
    elif(p1<p2):
        beat=p2-p1
        print(pn2," Beats ",pn1," by",beat," Points...")
    elif(p1==p2):
        print("Match Drawn")
    print("Have A Nice Day...Game Ended")

def play():
    pname1=input("Player 1...Please Enter Your Name? ")
    pname2=input("Player 2...Please Enter Your Name? ")
    p1p=0
    p2p=0
    turn=0
    while(1):
       if turn%2==0:
           word=choose()
           finalword=jumble(word)
           print(pname1," Turn....")
           print(finalword)
           ans=input("Guess the Word? ")
           if(ans==word):
               p1p+=1
               print("Your Score is ",p1p)
           else:
               print("Better Luck Next Time...The Correct Word is ",word)
           c=int(input("Press 1 to Continue and 0 to Exit "))
           if c==0:
               thank(pname1,pname2,p1p,p2p)
               break
           
       else:
           word=choose()
           finalword=jumble(word)
           print(pname2," Turn....")
           print(finalword)
           ans=input("Guess the Word? ")
           if(ans==word):
               p2p+=1
               print("Your Score is ",p2p)
           else:
               print("Better Luck Next Time...The Correct Word is ",word)
           c=int(input("Press 1 to Continue and 0 to Exit "))
           if c==0:
               thank(pname1,pname2,p1p,p2p)
               break
       turn+=1
          
play()

