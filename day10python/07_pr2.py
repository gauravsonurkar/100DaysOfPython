def game():
    return 78894

with open("highscore.txt",'r') as f:
    score = f.read()
    
hiscore = game()
if(str(hiscore) > str(score)):
    with open("highscore.txt",'w')as f:
        f.write(str(hiscore))