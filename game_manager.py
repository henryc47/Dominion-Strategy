import deck
import card
import controller
import piles
import copy
import math as m

player_strategies = [controller.prefer_money_strategy,controller.prefer_land_strategy,controller.in_between_strategy]

class GameManager():
    def __init__(self,player_strategies):
        num_players = len(player_strategies)
        d = deck.Deck(deck.starting_cards)
        self.game_pile = piles.Piles(piles.card_quantities,piles.player_cards,num_players)
        self.players = []
        self.pile_removed = False
        self.needed_piles_removed = 3
        self.piles_removed = 0
        for i,strategy in enumerate(player_strategies):
            new_name = "CPU" + str(i+1)
            new_cpu = controller.BuyPreferenceController(copy.deepcopy(d),new_name,self.game_pile,self,strategy)
            self.players.append(new_cpu)
        
    def run_game(self):
        game_ended = False
        while game_ended==False:
            game_ended = self.turn()
        victory_id = self.determine_victory()
        return victory_id
    

    def turn(self):
        for player in self.players:
            player.turn()
            if self.pile_removed == True:
                game_ended = self.check_game_ended()
                if game_ended:
                    return True #game ended before all players had their turn
        
        return False
    
    def check_game_ended(self):
        self.piles_removed += 1
        if self.piles_removed >=3:
            return True
        elif card.province not in self.game_pile.card_quantities:
            return True
        else:
            return False

    #return the index of the player who won, ties are broken by order (will implement better tie handling later)
    def determine_victory(self):
        #The game has come to an end, determine the victor
        best_player_vp = -m.inf
        best_player_index = -1
        best_player_name = ""
        for i,controller in enumerate(self.players):
            player_vp = controller.player.deck.calculate_all_victory_points()
            print("Player ",controller.name," had ",player_vp," Victory Points") #debug
            if player_vp>best_player_vp:
                best_player_vp = player_vp
                best_player_index = i
                best_player_name = controller.name

        print("Player ",best_player_name," Won!") #debug
        return best_player_index
