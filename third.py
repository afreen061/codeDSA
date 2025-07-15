# range(1, 5) 5 not include [)
# random.randint(1, 5) []
# random.random()  # >= 0.0 and < 1.0 [)
# name[0:3] [)
import random 

random_number=random.randint(1,9)
print(random_number)

random_number2=random.random()
print(random_number2)

# random.shuffle(list)--> position change []
# random.sample(seq, k=n) ---> k item without repeat []
# random.choices(seq, k=n)--> k item with repeat []
# random.choice(seq)-----> seq []
# random.uniform(a, b)----> float btw []

game =["Stone","Paper","Scissor"]
player=int(input("your chance:"))
playerChance=game[player]
choose =random.randint(0,2)
computer=game[choose]
print(playerChance)
print(computer)
if playerChance == 'Stone' and computer=="paper":
    print("you lose")
elif playerChance == 'Stone' and computer=="Scissor":
    print("you win")
elif playerChance == 'paper' and computer=="Stone":
    print("you win")
elif playerChance == 'Scissor' and computer=="Stone":
    print("you lose")    
    ##
elif playerChance == 'Paper' and computer=="Scissor":
    print("you lose")
elif playerChance == 'Scissor' and computer=="Paper":
    print("you win") 
else:
    print("draw")
    
   















































































































































































