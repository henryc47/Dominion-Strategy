import deck
import card

if __name__ == "__main__":
    d = deck.Deck(deck.starting_cards)
    d.display_draw_pile_cards()
    d.draw_single_card()
    d.draw_single_card()
    d.display_draw_pile_cards()
    d.display_hand_cards()



