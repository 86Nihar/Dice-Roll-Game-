import random 

rollcount = 0
while True:
    
    
    choice = input("Roll your Dies(y/n):").lower()
    

    if choice == 'y':
        dice1 = random.randint(1,6)
        print(dice1)
        rollcount += 1
        
    elif choice == 'n':
        print("thank for playing")
        break
    
    else:
        print("invalid input")
        
        

print("Dice rolled: ",rollcount,"times",)

    