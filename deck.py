import random

def shuffle_deck(Card, seed=None):
    '''generates a shuffled deck with the provided Card class

    Note that Card should have a constructor that takes two arguments
    in (rank, suit) order.  rank is in the range [1,13] and suit is [0,3]
    If seed is omitted, the generated shuffle will be different each
    time.'''
    deck = []
    for suit in range(4):
        for rank in range(1,14):
            deck.append(Card(rank, suit))
    random.seed(seed)
    random.shuffle(deck)
    for card in deck:
        yield card
