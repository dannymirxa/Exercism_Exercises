
hand = [2, 3, 4, 8, 8]

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand)/ len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)

    return True if ((hand[0]+ hand[-1])/2) == average or (hand[int((len(hand)-1)/2)] == average) else False

# print(approx_average_is_average(hand))

hand = [1, 3, 5, 7, 9]

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    return True if sum(hand[::2])/len(hand[::2]) == sum(hand[1::2])/len(hand[1::2]) else False

# print(average_even_is_average_odd(hand))

hand = [5, 9, 11]

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    
    if hand[-1] == 11:
        hand[-1] = 11*2
    
    return hand

print(maybe_double_last(hand))