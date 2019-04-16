print("welcome")
class employee:
    def __init__(self,hp,ak1,ak2):
      self.hp = hp
      self.ak1 = ak1
      self.ak2 = ak2
    def attacktake(self1,self2):
        if self1.hp<=0:
            print(b,"is already eliminated")
        elif self2.hp<=0:
            print(a,"is already eliminated")
        elif y==x:
            print("sorry dude,looks like u done a mistake")
        else:
         self1.hp=self1.hp-self2.ak1
         if self1.hp<=0:
            self1.hp=0
            print(a,"won by defeating",b)
gaurang = employee(300,65,80)
zaid = employee(300,60,75)
nihal = employee(300,55,70)
def change():
    x.ak1=x.ak2
def heal(x):
    if x.hp<=250:
        x.hp=x.hp+50
        print(a,"health is increased by 50 points")
        print(a,"health is",x.hp)      
    else:
        print("sorry,cannot us the heal right now")

for i in range(100):
    
    x=input("choose the attacking player from g,z and n")
    if x== 'g':
        x=gaurang
        a='gaurang'       
    elif x=='z':
        x=zaid
        a='zaid'        
    elif x=='n':
        x=nihal
        a='nihal'
    print(a,"is in attacking mode")            
    y=input("choose the player to be attacked or you know what else you can do")
    if y=="heal":
        heal(x)
    if y=='g':
     y=gaurang
     b='gaurang'
     if x==nihal:
         change()
    elif y=='z':
     y=zaid
     b='zaid'
     if x==gaurang:
         change()
    elif y=='n':
     y=nihal
     b='nihal'
     if x==zaid:
         change()
    if y!="heal":     
      employee.attacktake(y,x)
    if y!="heal":
     if y!=x:
      if y.hp!=0:
       print(b,"got attacked by",a)
       print("health remaining of",b,"is",y.hp)
   


































    
































    
