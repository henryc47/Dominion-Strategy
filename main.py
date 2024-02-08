import game_manager
import strategies
import matchups

import copy
if __name__ == "__main__":
    #all_strategies = strategies.generate_strategies(strategies.treasure_cards_ranked,strategies.victory_cards_ranked,strategies.starting_max_cost)
    #matchups.run_pair_matchups(all_strategies,repeat)
    all_strategies = strategies.generate_strategies(strategies.treasure_cards_ranked,strategies.victory_cards_ranked,strategies.starting_max_cost)
    strategies.print_all_strategies(all_strategies)
    matchups.run_pair_matchups(all_strategies,10)



    

    





