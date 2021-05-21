class Card:
    def __init__(self, rank = 1, suit = 0):
        temp_rank = 'A'
        temp_suit = 'C'
        self.num_rank = rank
        self.num_suit = suit
        if rank == 10:
            temp_rank = 'T'
        elif rank == 11:
            temp_rank = 'J'
        elif rank == 12:
            temp_rank = 'Q'
        elif rank == 13:
            temp_rank = 'K'
        elif rank == 1:
            pass
        else:
            temp_rank = rank
        self.rank = temp_rank
        if suit == 0:
            pass
        elif suit == 1:
            temp_suit = 'D'
        elif suit == 2:
            temp_suit = 'H'
        else:
            temp_suit = 'S'
        self.suit = temp_suit

    def is_red(self):
        if (self.suit == 'D' or self.suit == 'H'):
            return True
        else:
            return False

    def can_tableau_on(self, other):
        if (self.is_red() != other.is_red() and self.rank == (other.rank - 1)):
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(other,str):
            if self.rank == other:
                return True
            elif self.suit == other:
                return True
            else:
                return False
        elif isinstance(other,int):
            if self.num_rank == other:
                return True
            elif self.num_suit == other:
                return True
            else:
                return False
        else:
            if self.rank == other.rank:
                if self.suit == other.suit:
                    return True
            else:
                return False

    def __str__(self):
        retstr = "|" + str(self.rank) + str(self.suit) + "|"
        return retstr

