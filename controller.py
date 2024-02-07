import card as card
import deck as deck
import player as player

prefer_money_strategy = [card.province,card.gold,card.silver,card.copper]
prefer_land_strategy = [card.province,card.duchy,card.estate,card.copper]
in_between_strategy = [card.province,card.duchy,card.silver,card.copper]

#Controller class is responsible for deciding which actions to take in the game, this is just a parent class to store common variables, implemention is in the child class
class Controller():
    def __init__(self,deck,name,piles,game_manager):
        self.player = player.Player(deck,self,piles,game_manager)
        self.name = name
    
    #take a turn
    def turn(self):
        print(self.name,"'s Turn")
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
        print("decide_buy method not implemented in ",type(self))
        return None
    
    #decide on an action to take, just a placeholder, implement in child class
    def decide_action(self):
        print("decide_action method not implemented in ",type(self))
        return None

#control the game manually as a human using the command line
class ManualController(Controller):
    def __init__(self,deck,name,piles,game_manager):
        super().__init__(deck,name,piles,game_manager)
    
#play the game automatically by buying cards in response to a preference for buying particular cards
class BuyPreferenceController(Controller):
    def __init__(self,deck,name,piles,game_manager,strategy):
        super().__init__(deck,name,piles,game_manager)
        self.strategy = strategy
    #decide on which option to buy
    def decide_buy(self):
        buy_power = self.player.buy_power
        print("our buy power is ",buy_power) #debug
        for card in self.strategy:
            bought_card = self.player.implement_buy(card)
            if bought_card==True:
                print("we bought a ",card.name) #debug
                break
        if bought_card==False:
            print("all cards we are interested in are too expensive") #debug










