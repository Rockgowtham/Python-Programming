import random
import matplotlib.pyplot as plt
amount=0
x=[]
y=[]
for i in range(1,366):
    x.append(i)
    bit=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    if bit==lucky_draw:
        amount=amount+900-100
    else:
        amount=amount-100
    y.append(amount)
print("Amount Remaining in the Game Account: ",amount)
plt.plot(x,y)
plt.show()

  
