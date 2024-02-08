import game_manager
import strategies

def run_pair_matchups(strategies,repeat):
    strategy_names = generate_strategy_names(strategies)
    num_strategies = len(strategies)
    print("Comparing ",num_strategies," unique strategies")
    

def generate_strategy_names(strategies):
    strategy_names = []
    for strategy in strategies:
        strategy_names.append(str(strategy))
    return strategy_names
