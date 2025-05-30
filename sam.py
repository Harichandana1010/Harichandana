import random

word_list=["msouse","juicie","Haia"]
c_w=random.choice(word_list)
print(c_w)
placeholder=""
for i in range(len(c_w)):
    placeholder += " _ "
print(placeholder)
game_over =False
correctword=[]
while not game_over:
    guess=input("Guess a letter: ").lower()
    display=""
    for l in c_w:
        if l == guess:
            display+= l
            correctword.append(guess)
        elif l in correctword:
            display+= l
        else:
            display +=" _ "
    print(display)
    if "_" not in display:
        game_over=True
        print("you win")   