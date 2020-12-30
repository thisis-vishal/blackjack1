def game():
    from art import logo
    import random
    print(logo)
    computer_turn=True 
    def deal_cards():
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        card=random.choice(cards)
        return card
    def score(cards):
        a=0
        for i in cards:
            a=a+i
        if a==21 and len(cards)==2:
            return 0   
        if 11 in cards and (a>21):
            cards.remove(11)
            cards.append(1)
            return a   
        else:
            return a       
    def compare(player,computer):
        if computer>21 and player<21:
            print(f"computer cards are {computer_cards} and score ={computer}")
            print("you win hurray!")
        elif player>computer:
            print(f"computer cards are {computer_cards} and score ={computer}")
            print("you win hurray!")
        elif computer>player:
            print(f"computer cards are {computer_cards} and score ={computer}")
            print("you loose!")
        elif computer_score==0 or computer_score==21:
            print(f"computer cards are{computer_cards} and computer score is 21 ")
            print("computer win by Blackjack")
        else:
            print(f"computer cards are {computer_cards} and score ={computer}")
            print("draw")

            
    
    computer_cards=[]
    player_cards=[]
    computer_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    player_cards.append(deal_cards())
    player_cards.append(deal_cards())
    computer_score=score(computer_cards)
    player_score=score(player_cards)
    print(f"    your cards are {player_cards} and your score is {player_score}")
    print(f"    computer first card is{computer_cards[0]}")
    if computer_score==0:
        print(f"computer cards are{computer_cards} and computer score is 21 ")
        print("computer win by Blackjack")
        play()
    if player_score==0:
        print("hurray! you win with blackjack") 
        play()
    player_turn=True    
    Turn=True
    while player_turn==True:
        action=input("if you want to add card press y else n")
        if action=='y':
            player_cards.append(deal_cards())
            player_score=score(player_cards)
            if player_score==0 or player_score==21:
                print(f"    your cards are {player_cards} and your score is {player_score}")
                print(f"computer cards are{computer_cards} and computer score is {computer_score}")
                print("hurray! you win with blackjack")
                player_turn=False 
                play()
            elif player_score>21:
                print(f"    your cards are {player_cards} and your score is {player_score}")    
                print(f"computer cards are{computer_cards} and computer score is {computer_score}")
                print("You loose")
                player_turn=False
                play()
            else:
                print(f"    your cards are {player_cards} and your score is {player_score}")
                print(f"computer one card is{computer_cards[0]}")    
        else:
            while Turn==True:
                if computer_score<17:
                    computer_cards.append(deal_cards())
                    computer_score=score(computer_cards)      
                else:
                    compare(player_score,computer_score)
                    Turn=False 
                    play()  
            player_turn=False    

def play():
    play=input("If you want to play blackjack press y else n")
    if play=="y":
        game()                        
    else:
        print("thanks for coming")    
play()        










        

    

   
 







