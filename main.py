import deck
import card
import controller
import piles
import copy
if __name__ == "__main__":
    d = deck.Deck(deck.starting_cards)
    c_cpu = controller.BuyPreferenceController(copy.deepcopy(d),"CPU1",controller.prefer_money_strategy)
    c_player = controller.ManualController(copy.deepcopy(d),"PLAYER1")
    game_pile = piles.Piles(piles.card_quantities,piles.player_cards,8)
    game_pile.print_card_quantities()
    new_card,run_out = game_pile.provide_card(card.copper)
    print(new_card," ",run_out)
    new_card,run_out = game_pile.provide_card(card.copper)
    print(new_card," ",run_out)
    new_card,run_out = game_pile.provide_card(card.copper)
    print(new_card," ",run_out)
    new_card,run_out = game_pile.provide_card(card.copper)
    print(new_card," ",run_out)
    new_card,run_out = game_pile.provide_card(card.copper)
    print(new_card," ",run_out)
    new_card,run_out = game_pile.provide_card(card.copper)
    print(new_card," ",run_out)
    new_card,run_out = game_pile.provide_card(card.copper)
    print(new_card," ",run_out)
    new_card,run_out = game_pile.provide_card(card.gold)
    print(new_card," ",run_out)
    game_pile.print_card_quantities()

    

    





