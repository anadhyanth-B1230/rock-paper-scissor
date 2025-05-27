import random
ch=['rock','paper ','seissor']
comp=random.choice(ch)
player=int(input('1.rock 2.paper 3.seissors'))
def whowin(comp,player):
    if player==comp:
        return 'its a tie'
    elif (player==1 and comp=='seissors') or(player==2 and comp=='rock') or (player==3 and comp=='paper'):
        
        return 'you win!'
    else:
        return 'you lose!'
score=whowin(comp,player)
print('computer choice :',comp)
print(score)
    
