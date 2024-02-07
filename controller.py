import card as card
import deck as deck
import player as player

#Controller class is responsible for deciding which actions to take in the game, this is just a parent class to store common variables, implemention is in the child class
class Controller():
    def __init__(self,deck,name):
        self.player = player.Player(deck,self)
        self.name = name
    
    #take a turn
    def turn(self):
        self.player.turn()
    
    #display all the cards in the hand
    def debug_display_hand_cards(self):
        print(self.name," hand =",end=' ')
        self.player.deck.display_hand_cards()
    
    #display all cards in the draw pile
    def debug_display_draw_pile_cards(self):
        print(self.name," draw pile =",end=' ')
        self.player.deck.display_draw_pile_cards()
    
    #display all cards in the discard pile
    def debug_display_discard_pile_cards(self):
        print(self.name," discard pile =",end=' ')
        self.player.deck.display_discard_pile_cards()

    
    #decide on a buy to make, just a placeholder, implement in child class
    def decide_buy(self):
        print("decide_buy method not implemented in class ",type(self))
    
    #decide on an action to take, just a placeholder, implement in child class
    def decide_action(self):
        print("decide_action method not implemented in class ",type(self))

#control the game manually as a human using the command line
class ManualController(Controller):
    def __init__(self,deck,name):
        super().__init__(deck,name)
    
#play the game automatically by buying cards in response to a preference for buying particular cards
class BuyPreferenceController(Controller):
    def __init__(self,deck,name):
        super().__init__(deck,name)




