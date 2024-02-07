import card as card

card_quantities = {card.copper : 60,card.silver : 40, card.gold : 30, card.estate : 24, card.duchy : 12, card.province : 12}
player_cards = {card.estate : 3, card.copper :7 }

#the piles class stores the piles of cards
class Piles:
    def __init__(self,card_quantities,player_cards = {},num_players=0):
        self.card_quantities = card_quantities
        if num_players>0:
            for key,value in player_cards.items():
                self.remove_cards(key,value*num_players)

    #remove n card from the piles, used during initialisation only
    def remove_cards(self,card,n):
        if card in self.card_quantities:
            card_quantities[card] -= n
            if card_quantities[card] <= 0:
                del card_quantities[card]

    #provide a card from the piles, return None if no such card, additional return value True is ran out on this check
    def provide_card(self,card):
        run_out = False
        if card in self.card_quantities:
            card_quantities[card] -= 1
            card_returned = card
            if card_quantities[card]==0:
                del card_quantities[card]
                run_out = True
        else:
            card_returned = None
        return card_returned,run_out

    #for debug, display the quantity still left in each pile
    def print_card_quantities(self):
        print("Unused Cards")
        for key,value in self.card_quantities.items():
            print(value," ",key.name)
        
    


        