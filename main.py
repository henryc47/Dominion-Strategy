import game_manager
import strategies

import copy
if __name__ == "__main__":
    #new_game = game_manager.GameManager(game_manager.player_strategies)
    #victor = new_game.run_game()
    #print("VICTOR = ",victor)
    all_strategies = strategies.generate_strategies(strategies.treasure_cards_ranked,strategies.victory_cards_ranked,strategies.starting_max_cost)
    strategies.print_all_strategies(all_strategies)




    

    





