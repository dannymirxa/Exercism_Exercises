def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    """
    21 - 16 = 5 < 11 return 1

    21 - 10 = 11 >= 11 return 11

    21 - (11 + 10) = 0
    """
    if 21 - (value_of_card(card_one) + value_of_card(card_two)) < 11:
        return 1
    else:
        return 11

card_one, card_two = '2', 'A'

print(value_of_card(card_one) + value_of_card(card_one))

print(21 - (value_of_card(card_one) + value_of_card(card_one)))

print(value_of_ace(card_one, card_two))