import card as card

#The deck class stores the cards the player owns
class Deck():
    #create the storage containers for the deck
    def __init__(self):
        self.draw_pile = [] #all cards in the players draw pile
        self.hand = [] #all cards in the players hand
        self.discard_pile = []#all cards in the players discard pile
    
    #adds a new external card to a players draw pile
    def add_external_card_to_draw_pile(self,new_card : card.Card):
        self.draw_pile.append(new_card)
    
    #adds a new external card to a players hand
    def add_external_card_to_hand(self,new_card : card.Card):
        self.hand.append(new_card)
    
    #adds a new external card to a players discard pile
    def add_external_card_to_discard_pile(self,new_card : card.Card):
        self.discard_pile.append(new_card)


        