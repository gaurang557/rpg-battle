print("welcome")
class player:
    def __init__(self,hp,ak1,ak2):
      self.hp = hp
      self.ak1 = ak1
      self.ak2 = ak2
    def attacktake(self1,self2):
        if self1==self2:
            print("sorry dude,looks like u have done a mistake")
        elif self1.hp==0:
            print(b,"is already eliminated")
        elif self2.hp==0:
            print(a,"is already eliminated")        
        else:
            self1.hp=self1.hp-self2.ak1
            if self1.hp<=0:
                self1.hp=0
                print(a,"won by defeating",b)
player1 = player(300,65,80)
player3 = player(300,60,75)
player2 = player(300,55,70)
def change(x):
    x.ak1=x.ak2
def heal(x):
    if x.hp<=250:
        x.hp=x.hp+50
        print(a,"health is increased by 50 points")
        print(a,"health is",x.hp)      
    else:
        print("sorry,cannot use the heal right now")

for i in range(100):    
    x=input("choose the attacking player from playe1,player2 and player3")
    if x== 'p1':
        x=player1
        a='player1'       
    elif x=='p2':
        x=player2
        a='player2'        
    elif x=='p3':
        x=player3
        a='player3'
    if x.hp!=0:
        print(a,"is in attacking mode")   
    else:
        print(a,"is already eliminated")
        continue
    y=input("choose the player to be attacked or use the heal function")
    if y=='p1':
        y=player1
        b='player1'
        if x==player2:
            change(x)
    elif y=='p3':
        y=player3
        b='player3'
        if x==player1:
            change(x)
    elif y=='p2':
        y=player2
        b='player2'
        if x==player3:
            change(x)
    elif y=="heal" or "Heal":
        heal(x)
        continue
    player.attacktake(y,x)
    if y!=x:
        if y.hp!=0:
            print(b,"got attacked by",a)
            print("health remaining of",b,"is",y.hp)