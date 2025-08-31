import art
import random
def giving_cards(who):
    if who== 'player':
        player.append(cards[random.randint(1,13)-1])
        score('player', player[-1])
    elif who== 'computer':
        computer.append(cards[random.randint(1, 13) - 1])
        score('computer',computer[-1])
def score(who,scre):
    global ply_score
    global com_score
    if who=='player':
        ply_score+=scre
        if ply_score>21:
            for scr in player:
                if scr==11:
                    ply_score-=10
                    player[player.index(11)]=1
                    break
    else:
        com_score += scre
        if com_score>21:
            for scr in computer:
                if scr==11:
                    com_score -= 10
                    computer[computer.index(11)] = 1
def compare():
    print(
        f"Your final hand {player}, final score {ply_score}\n"
        f"Computer final hand {computer}, final score {com_score}")
    if ply_score > com_score or com_score > 21:
        print("you win")
    elif ply_score==com_score:
        print("It's a draw")
    else:
        print("you lose")
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
x=input("do you want to play a game of blackjack? Type 'y' or 'n'").lower()
if x=='y':
    start=True
else :
    start=False
while start:
    player = []
    computer = []
    ply_score = 0
    com_score = 0
    fwd=True
    print(art.logo)
    giving_cards('player')
    giving_cards('player')
    giving_cards('computer')
    giving_cards('computer')
    print(f"Your cards : {player}, current score : {ply_score}")
    print(f"Computer's frst card : {computer[0]}")
    while True:
        if ply_score==21 and len(player)==2:
            if com_score==21:
                print("You lose since computer ter has a blackjack")
            else:
                print("It's a blackjack!!! You win ")
            fwd=False
            break
        x = input("Type 'y' to get another card, 'n' to pass: ").lower()
        if x=='n':
            break
        giving_cards('player')
        if ply_score>21:
            print(f"Your cards : {player}, current score : {ply_score}\nYou went over!!! you lose")
            fwd=False
            break
        print(f"Your cards : {player}, current score : {ply_score}")
    if fwd:
        while True:
            if com_score>17:
                break
            else :
                giving_cards('computer')

        compare()
    x = input("do you want to play a game of blackjack? Type 'y' or 'n'").lower()
    if x == 'y':
        print(20*"\n")
        start = True
    else:
        start = False

