import deck
import card

if __name__ == "__main__":
    d = deck.Deck()
    d.add_external_card_to_discard_pile(card.copper)
    d.add_external_card_to_discard_pile(card.silver)
    d.add_external_card_to_discard_pile(card.estate)
    d.add_external_card_to_discard_pile(card.estate)
    d.add_external_card_to_hand(card.duchy)
    d.add_external_card_to_hand(card.estate)
    d.add_external_card_to_hand(card.silver)
    d.add_external_card_to_draw_pile(card.gold)
    d.add_external_card_to_draw_pile(card.estate)
    d.add_external_card_to_draw_pile(card.province)
    d.display_draw_pile_cards()
    print("deck draw pile vp = ",d.calculate_victory_points(d.draw_pile))
    d.display_hand_cards()
    print("deck hand vp = ",d.calculate_victory_points(d.hand))
    d.display_discard_pile_cards()
    print("deck discard pile vp = ",d.calculate_victory_points(d.discard_pile))
    print("total vp = ",d.calculate_all_victory_points())


