import deck
import card
import controller
import copy as copy

if __name__ == "__main__":
    d = deck.Deck(deck.starting_cards)
    c_cpu = controller.BuyPreferenceController(copy.deepcopy(d),"CPU1")
    c_player = controller.ManualController(copy.deepcopy(d),"PLAYER1")
    c_cpu.debug_display_draw_pile_cards()
    c_cpu.debug_display_hand_cards()
    c_cpu.debug_display_discard_pile_cards()
    c_player.debug_display_draw_pile_cards()
    c_player.debug_display_hand_cards()
    c_player.debug_display_discard_pile_cards()
    c_cpu.turn()
    c_player.turn()
    c_cpu.debug_display_draw_pile_cards()
    c_cpu.debug_display_hand_cards()
    c_cpu.debug_display_discard_pile_cards()
    c_player.debug_display_draw_pile_cards()
    c_player.debug_display_hand_cards()
    c_player.debug_display_discard_pile_cards()
    c_cpu.turn()
    c_player.turn()
    c_cpu.debug_display_draw_pile_cards()
    c_cpu.debug_display_hand_cards()
    c_cpu.debug_display_discard_pile_cards()
    c_player.debug_display_draw_pile_cards()
    c_player.debug_display_hand_cards()
    c_player.debug_display_discard_pile_cards()
    c_cpu.turn()
    c_player.turn()
    c_cpu.debug_display_draw_pile_cards()
    c_cpu.debug_display_hand_cards()
    c_cpu.debug_display_discard_pile_cards()
    c_player.debug_display_draw_pile_cards()
    c_player.debug_display_hand_cards()
    c_player.debug_display_discard_pile_cards()





