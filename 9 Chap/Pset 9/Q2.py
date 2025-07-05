# game to save hiscore in file name hiscore
import random

def game():
    print("your playing a game")
    score = random.randint(1, 70)
    #fetch hiscore 
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"your score {score}")
    if(score>hiscore):
        # write hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()