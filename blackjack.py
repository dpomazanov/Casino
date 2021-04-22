import random
import numpy as np

def get_deck(number_of_decks):
    J = 10
    Q = 10
    K = 10
    A = 1 or 11

    Cards = [2,3,4,5,6,7,8,9,10,J,Q,K,A]
    # Clubs = [2,3,4,5,6,7,8,9,10,J,Q,K,A]
    # Hearts = [2,3,4,5,6,7,8,9,10,J,Q,K,A]
    # Diamonds = [2,3,4,5,6,7,8,9,10,J,Q,K,A]

    Deck = [ele for ele in Cards for i in range(4)]
    Deck_full =  [ele for ele in Deck for i in range(number_of_decks)]

    random.shuffle(Deck_full)

    Deck_shuffled = Deck_full

    return  Deck_shuffled

number_of_decks = int(input("Enter number of decks:")) # request number ot decks to be used
Deck = get_deck(number_of_decks)

play = True

while play == True:
    # player hand
    player_hand = Deck[0] + Deck[2]
    print("player hand: ", player_hand)

    # dealer hand, only shoys first card drawn
    dealer_hand = Deck[1] + Deck[3]
    print("dealer hand: ", Deck[3])

    Deck[0:3] = [] #removes used card from deck
    # print(Deck)

    player_move = input("Enter 's' for stand or 'h' for hit:")

    # player moves
    # player moves
    # player moves

    while player_move == "h":
        player_hand = player_hand + Deck[0]
        Deck.pop(0)
        print(len(Deck))
        
        print("player hand: ", player_hand)
        
        if player_hand > 21:
            print("player loses")
            play = False
            break

        player_move = input("Enter 's' for stand or 'h' for hit:")

    # dealer moves
    # dealer moves
    # dealer moves
    if play == True:
        while dealer_hand < 17:
            dealer_hand = dealer_hand + Deck[0]
            Deck.pop(0)
            print(len(Deck))

                

        print("player hand: ", player_hand)
        print("dealer hand: ", dealer_hand)

        if dealer_hand > player_hand and dealer_hand <= 21:
            print("player loses")
            play = False
        elif dealer_hand == player_hand:
            print("push")
            play = False
        else :
            print("player wins")
            play = False
    else :
        print("dealer hand: ", dealer_hand)


    play = input("Would you like to play again? Y/N ")
    if play == 'Y' or play == 'y':
        play = True
        
    elif play == 'N' or play == 'n':
        play = False
        break

#TO DO
# ace not interpreted as 1 or 11
# what happens when deck ends
# fix invalid input