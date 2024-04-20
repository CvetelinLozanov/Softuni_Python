def draw_cards(*args, **kwargs):
    cards = {}

    for arg in args:
        card_name = arg[0]
        card_type = arg[1]
        cards[card_name] = card_type

    cards.update(kwargs)
    monster_cards = [card_name for card_name, card_type in cards.items() if card_type == 'monster']
    spell_cards = [card_name for card_name, card_type in cards.items() if card_type == 'spell']
    sorted_monster_cards = sorted(monster_cards, reverse=True)
    sorted_spell_cards = sorted(spell_cards)

    result = []
    if monster_cards:
        result.append('Monster cards:')
        [result.append(f'  ***{monster_card}') for monster_card in sorted_monster_cards]
    if spell_cards:
        result.append('Spell cards:')
        [result.append(f'  $$${spell_card}') for spell_card in sorted_spell_cards]

    return '\n'.join(result)


print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))