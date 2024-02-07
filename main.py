import game_manager

import copy
if __name__ == "__main__":
    new_game = game_manager.GameManager(game_manager.player_strategies)
    victor = new_game.run_game()
    print("VICTOR = ",victor)



    

    





