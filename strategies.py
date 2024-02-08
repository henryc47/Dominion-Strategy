import card as card
import piles as pile
#generate unique strategies
#at the moment just do using treasure and victory cards
treasure_cards_ranked = [card.gold,card.silver,card.copper] #treasure cards in utility order, we will not use a combination where a lower utility card outranks a higher utility card of the same type
victory_cards_ranked = [card.province,card.duchy,card.estate] #victory cards in utility order
starting_max_cost = 5

def generate_strategies(treasure_cards_ranked,victory_cards_ranked,achievable_cost):
    num_treasures = len(treasure_cards_ranked)
    num_victorys = len(victory_cards_ranked)
    strategies = [[]]
    strategy_check_indices = [[0,0]] #first is treasure indice, second is victory indice
    all_strategies = []
    while len(strategies)>0:
        new_strategies = []
        new_strategy_check_indices = []
        for i,strategy in enumerate(strategies):
            treasure_indice = strategy_check_indices[i][0]
            victory_indice = strategy_check_indices[i][1]
            if treasure_indice<num_treasures:
                new_strategy = strategy.copy()
                new_strategy.append(treasure_cards_ranked[treasure_indice])
                new_strategies.append(new_strategy)
                new_strategy_check_indices.append([treasure_indice+1,victory_indice])
            if victory_indice<num_victorys:
                new_strategy = strategy.copy()
                new_strategy.append(victory_cards_ranked[victory_indice])
                new_strategies.append(new_strategy)
                new_strategy_check_indices.append([treasure_indice,victory_indice+1])


        all_strategies.extend(new_strategies)
        strategies = new_strategies
        strategy_check_indices = new_strategy_check_indices
    
    all_strategies = remove_redundant_strategies(all_strategies)
    all_strategies = remove_unachievable_strategies(all_strategies,achievable_cost)
    return all_strategies

#remove strategies where a lower preference has a higher cost to buy than a higher preference
def remove_redundant_strategies(strategies):
    return_strategies = []
    for strategy in strategies:
        strategy_rundant = check_strategy_redundant(strategy)
        if not  strategy_rundant:
            return_strategies.append(strategy)
    
    return return_strategies

#remove strategies which are too expensive for any possible starting hand
def remove_unachievable_strategies(strategies,achievable_cost):
    return_strategies = []
    for strategy in strategies:
        strategy_achievable = check_strategy_achievable(strategy,achievable_cost)
        if strategy_achievable:
            return_strategies.append(strategy)
    
    return return_strategies

#strategy is redundant if a lower preference has a higher cost to buy than a higher preferene
def check_strategy_redundant(strategy):
    lowest_card_cost = strategy[0].cost_to_buy
    for i in range(1,len(strategy)):
        card_cost = strategy[i].cost_to_buy
        if card_cost>=lowest_card_cost:
            return True
        else:
            lowest_card_cost = card_cost
    
    else:
        return False

#check strategy is unachievable if none of the cards in it have a cost achievable with the starting hand (5)
def check_strategy_achievable(strategy,achievable_cost):
    for card in strategy:
        if card.cost_to_buy<=achievable_cost:
            return True
        else:
            continue
    return False
            


def print_strategy(strategy):
    for card in strategy:
        print(card.name,end=" ")
    
    print("")

def print_all_strategies(all_strategies):
    print("Strategies")
    for strategy in all_strategies:
        print_strategy(strategy)
    