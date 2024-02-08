import game_manager
import strategies
import tqdm
import copy

def run_pair_matchups(strategies,repeat):
    strategy_names = generate_strategy_names(strategies)
    num_strategies = len(strategies)
    print("Comparing ",num_strategies," unique strategies")
    #for i in range(num_strategies-1):
    for i in range(3,5):
        i_strategy = strategies[i]
        i_name = strategy_names[i]
        #for j in range(i+1,num_strategies):
        for j in range(i+1,i+3):
            j_strategy = strategies[j]
            j_name = strategy_names[j]
            num_i_victories = 0
            num_j_victories = 0
            num_draws = 0
            matchup_string = "Matchup = " + i_name + " VS " + j_name
            match_strategies = [i_strategy,j_strategy]
            for k in tqdm.tqdm(range(repeat),desc = matchup_string):
                new_game = game_manager.GameManager(match_strategies)
                victor = new_game.run_game()
                if len(victor)==2:
                    num_draws += 1
                elif victor[0]==0:
                    num_i_victories += 1
                elif victor[0]==1:
                    num_j_victories += 1
                else:
                    print("ERROR, raw victor = ",victor)
            print("Num Victories ",i_name," = ",num_i_victories, " ",j_name," = ",num_j_victories," "," Draws = ",num_draws)



    

def generate_strategy_names(strategies_list):
    strategy_names = []
    for strategy in strategies_list:
        strategy_names.append(strategies.get_strategy_name(strategy))
    return strategy_names
