import deck
import card

if __name__ == "__main__":
    d = deck.Deck(deck.starting_cards)
    d.display_draw_pile_cards()
    d.draw_cards(5)
    d.display_draw_pile_cards()
    d.display_hand_cards()
    d.draw_cards(3)
    d.display_draw_pile_cards()
    d.display_hand_cards()
    d.draw_cards(3)
    d.display_draw_pile_cards()
    d.display_hand_cards()



