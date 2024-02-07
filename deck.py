#externala modules
import random


#project modules
import card as card


#starting hand
starting_cards = [card.copper]*7 + [card.estate] *3

#The deck class stores the cards the player owns
class Deck():
    #create the storage containers for the deck
    def __init__(self,starting_cards):
        self.draw_pile = [] #all cards in the players draw pile
        self.hand = [] #all cards in the players hand
        self.discard_pile = []#all cards in the players discard pile
        self.draw_size = 5 #how many cards drawn from the deck each turn
        self.add_starting_cards(starting_cards)
        self.shuffle_draw_pile()
    
    def add_starting_cards(self,starting_cards):
        for card in starting_cards:
            self.add_external_card_to_draw_pile(card)

    #adds a new external card to a players draw pile
    def add_external_card_to_draw_pile(self,new_card : card.Card):
        self.draw_pile.append(new_card)
    
    #adds a new external card to a players hand
    def add_external_card_to_hand(self,new_card : card.Card):
        self.hand.append(new_card)
    
    #adds a new external card to a players discard pile
    def add_external_card_to_discard_pile(self,new_card : card.Card):
        self.discard_pile.append(new_card)
    
    #shuffle the cards in the draw pile
    def shuffle_draw_pile(self):
        random.shuffle(self.draw_pile)
    
    #draw a single card from the draw_pile and place it into the players hand, additionally return False if there are no more cards in the deck
    def draw_single_card(self):
        if len(self.draw_pile)==0: #no more cards left to draw
            return None,False

        

    #calculate the victory points of all the players cards
    def calculate_all_victory_points(self):
        sum_vp = 0
        sum_vp += self.calculate_victory_points(self.draw_pile)
        sum_vp += self.calculate_victory_points(self.hand)
        sum_vp += self.calculate_victory_points(self.discard_pile)
        return sum_vp

    #calculate the victory points in a particular card list
    def calculate_victory_points(self,card_list):
        sum_vp = 0
        for card in card_list:
            sum_vp += card.vp
        return sum_vp

    #display all the card names in a particular card list
    def display_card_names(self,card_list):
        print_str = ""
        for card in card_list:
            print_str += card.name
            print_str += " , "
        print_str = print_str[:-3]
        print(print_str)
    
    #display all the card names in the players draw pile
    def display_draw_pile_cards(self):
        print("Cards in Draw Pile =",end=' ')
        self.display_card_names(self.draw_pile)
    
    #display all the card names in the players hand
    def display_hand_cards(self):
        print("Cards in Hand = ",end=' ')
        self.display_card_names(self.hand)
    
    #display all the card names in the players hand
    def display_discard_pile_cards(self):
        print("Cards in Discard Pile = ",end=' ')
        self.display_card_names(self.discard_pile)