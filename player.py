import card
import deck
import controller
import piles 

#Player class is responsible for performing actions in the game
class Player():
    def __init__(self,deck,select_controller,piles):
        self.deck = deck
        self.controller = select_controller
        self.piles = piles
    
    #perform a players turn
    def turn(self):
        self.deck.draw_hand()
        self.current_hand = self.deck.provide_hand()
        print("HAND =",end=' ') #debug
        self.deck.display_card_names(self.current_hand)
        self.buy_power = self.deck.get_hand_buy_power()
        self.num_buys = 1
        self.num_actions = 1
        while(self.num_actions>0):
            action = self.controller.decide_action()
            self.implement_action(action)
            self.num_actions -= 1
        while(self.num_buys>0):
            card_to_buy = self.controller.decide_buy()
            managed_to_buy = self.implement_buy(card_to_buy)
            self.num_buys -= 1
        self.deck.discard_hand()

    #perform the provided action
    def implement_action(self,action):
        if action==None:
            pass
        else:
            pass
    #buy the provided card, return True if successful
    def implement_buy(self,card_to_buy):
        if card_to_buy==None:
            pass
        else:
            card_returned,run_out = self.piles.provide_card_if_can_afford(card_to_buy,self.buy_power)
            if card_returned==None:
                return False
            else:
                self.deck.add_external_card_to_discard_pile(card_returned) #add the external straight card to the discard pile (the correct behaviour by default)
                self.buy_power -= card_returned.cost_to_buy
                if run_out: #once we have implemented the manager, this should directly contact the manager to return 
                    pass
                return True

            
        
        

    

