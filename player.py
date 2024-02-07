import card as card
import deck as deck
import controller as controller

#Player class is responsible for performing actions in the game
class Player():
    def __init__(self,deck,select_controller):
        self.deck = deck
        self.controller = select_controller
    
    #perform a players turn
    def turn(self):
        self.deck.draw_hand()
        self.current_hand = self.deck.provide_hand()
        self.buy_power = self.deck.get_hand_buy_power()
        self.num_buys = 1
        self.num_actions = 1
        while(self.num_actions>0):
            action = self.controller.decide_action()
            self.implement_action(action)
            self.num_actions -= 1
        while(self.num_buys>0):
            card_to_buy = self.controller.decide_buy()
            self.implement_buy(card_to_buy)
            self.num_buys -= 1
        self.deck.discard_hand()

    #perform the provided action
    def implement_action(self,action):
        if action==None:
            pass
        else:
            pass
    #buy the provided card
    def implement_buy(self,card_to_buy):
        if card_to_buy==None:
            pass
        else:
            pass
        
        

    

