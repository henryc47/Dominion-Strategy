import deck
import card

if __name__ == "__main__":
    d = deck.Deck(deck.starting_cards)
    d.display_draw_pile_cards()
    d.draw_hand()
    d.display_draw_pile_cards()
    d.display_hand_cards()
    d.display_card_names(d.provide_hand())
    d.draw_hand()
    d.display_draw_pile_cards()
    d.display_hand_cards()
    d.display_card_names(d.provide_hand())
    d.draw_hand()
    d.display_draw_pile_cards()
    d.display_hand_cards()
    d.display_card_names(d.provide_hand())



