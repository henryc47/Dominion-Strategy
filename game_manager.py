import deck
import card
import controller
import piles
import copy
import math as m

player_strategies = [controller.prefer_money,controller.prefer_money_no_copper]

class GameManager():
    def __init__(self,player_strategies):
        num_players = len(player_strategies)
        d = deck.Deck(deck.starting_cards)
        self.game_pile = piles.Piles(piles.card_quantities,piles.player_cards,num_players)
        self.players = []
        self.pile_removed = False
        self.needed_piles_removed = 3
        self.piles_removed = 0
        self.max_turns = 1000 #if we reach 1000 turns and nobody has won, end the game now
        for i,strategy in enumerate(player_strategies):
            new_name = "CPU" + str(i+1)
            new_cpu = controller.BuyPreferenceController(copy.deepcopy(d),new_name,self.game_pile,self,strategy)
            self.players.append(new_cpu)
        
    def run_game(self):
        game_ended = False
        self.turns_taken = 0
        while (game_ended==False) and (self.turns_taken<self.max_turns):
            game_ended = self.turn()
            self.turns_taken += 1
        
        victory_ids = self.determine_victory()
        return victory_ids
    

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
        all_player_vps = self.calculate_all_player_vps()
        max_vp = max(all_player_vps)
        victor_indices = [i for i,x in enumerate(all_player_vps) if x==max_vp]
        return victor_indices

    #calculate the victory points of all the players
    def calculate_all_player_vps(self):
        all_victory_points = []
        for controller in self.players:
            all_victory_points.append(controller.player.deck.calculate_all_victory_points())
        
        return all_victory_points
