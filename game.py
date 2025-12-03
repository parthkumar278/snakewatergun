import random
def game(a,b):
    if a==b:
        return None;
    if a=='s' and b=='w':
        return True;
    elif a=='w'and b=='g':
        return False;
    elif a=='g' and b=='s':
        return True;
    elif b=='s'and a=='w':
        return False;
    elif b=='w' and a=='g':
         return True;
    elif b=='g' and a=='s':
        return False;

print("a turn :snake(s) water(w)or gun(g)?" )
randno=random.randint(1,3)
print(randno)
if randno==1:
    a='s'
elif randno==2:
    a='w'
else:
    a='g'
print("player 1 chose",a)  
    
b= input ("player 2 turn :snake(s) water(w)or gun(g)?" )
k=game(a,b)
if k==None:
    print("the game is a tie")
elif k==True:
    print("player 1 wins");
else:
    print("player 2 wins");