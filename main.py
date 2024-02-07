import deck
import card
import controller
import piles
import copy
if __name__ == "__main__":
    d = deck.Deck(deck.starting_cards)
    game_pile = piles.Piles(piles.card_quantities,piles.player_cards,7)
    c_cpu = controller.BuyPreferenceController(copy.deepcopy(d),"CPU1",game_pile,controller.prefer_money_strategy)
    c_player = controller.ManualController(copy.deepcopy(d),"PLAYER1",game_pile)
    game_pile.print_card_quantities()
    c_player.player.buy_power = 10
    c_player.player.implement_buy(card.estate)
    c_player.debug_display_discard_pile_cards()
    print(c_player.player.buy_power)
    game_pile.print_card_quantities()
    c_player.player.implement_buy(card.estate)
    c_player.debug_display_discard_pile_cards()
    print(c_player.player.buy_power)
    game_pile.print_card_quantities()
    c_player.player.implement_buy(card.estate)
    c_player.debug_display_discard_pile_cards()
    print(c_player.player.buy_power)
    game_pile.print_card_quantities()
    c_player.player.implement_buy(card.estate)
    c_player.debug_display_discard_pile_cards()
    print(c_player.player.buy_power)
    game_pile.print_card_quantities()
    c_player.player.implement_buy(card.estate)
    c_player.debug_display_discard_pile_cards()
    print(c_player.player.buy_power)
    game_pile.print_card_quantities()

    

    





