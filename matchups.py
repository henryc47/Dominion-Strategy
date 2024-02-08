import game_manager
import strategies
import tqdm
import copy

def run_pair_matchups(strategies,repeat):
    strategy_names = generate_strategy_names(strategies)
    num_strategies = len(strategies)
    print("Comparing ",num_strategies," unique strategies")
    num_victories = [0]*num_strategies #num victories + draws/2
    win_fraction_against = [{} for i in range(num_strategies)]
    for i in range(num_strategies-1):
        i_strategy = strategies[i]
        i_name = strategy_names[i]
        for j in range(i+1,num_strategies):
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
            #now store strategy data
            new_wins_i = num_i_victories + (num_draws/2)
            new_wins_j = num_j_victories + (num_draws/2)
            win_fraction_i_against_j = new_wins_i/repeat
            win_fraction_j_against_i = new_wins_j/repeat
            print(i," beats ",j," fraction = ",win_fraction_i_against_j) #debug
            print(j," beats ",i," fraction = ",win_fraction_j_against_i) #debug
            win_fraction_against[i][j] = win_fraction_i_against_j 
            win_fraction_against[j][i] = win_fraction_j_against_i 
            num_victories[i] += new_wins_i
            num_victories[j] += new_wins_j
    
    #now lets print the strategy data
    win_fractions = []
    for num_victory in num_victories:
        win_fractions.append(num_victory/(repeat*(num_strategies-1)))
    
    print("\n Results \n")
    for i in range(num_strategies):
        print("Strategy ",strategy_names[i])
        for j,win_fraction in win_fraction_against[i].items():
            print("Wins ",round(win_fraction*100,2),"'%' against ",strategy_names[j])
        print("overall win percentage = ",round(win_fractions[i]*100,2),"%")
        print(" ")

    print("Overall Best")
    max_win_fraction = max(win_fractions)
    win_index = win_fractions.index(max_win_fraction)
    print("Is ",strategy_names[win_index]," Overall Win Percentage = ",round(win_fractions[win_index]*100,2),"%")
    for j,win_fraction in win_fraction_against[win_index].items():
        print("Wins ",round(win_fraction*100,2),"'%' against ",strategy_names[j])

    

def generate_strategy_names(strategies_list):
    strategy_names = []
    for strategy in strategies_list:
        strategy_names.append(strategies.get_strategy_name(strategy))
    return strategy_names
