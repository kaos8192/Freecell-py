from card import Card
class Cell:
    def __init__(self, items = []):
        self.cards = items

    def __len__(self):
        count = 0
        for it in self.cards:
            count += 1
        return count

    def is_empty(self):
        if self.cards == []:
            return True
        else:
            return False

    def can_place(self, card):
        if len(self.cards) == 0:
            return True
        if isinstance(card, list):
            cardit = card[0]
        else:
            cardit = card
        here = self.cards[len(self.cards)-1]
        if cardit.is_red() is not here.is_red():
            if cardit.num_rank == here.num_rank - 1:
                return True
        elif cardit.suit == here.suit:
            if cardit.num_rank == here.num_rank + 1:
                return True
        else:
            return False


    def can_pick(self, card):
        if card in self.cards:
            return True
        else:
            return False

    def place(self, card):
        if card is not None:
            for it in card:
                self.cards.append(it)
        else:
            pass

    def help_pick(self, card):
        count = self.cards.index(card)
        while count < (len(self.cards) - 1):
            if(self.cards[count+1].is_red() != self.cards[count].is_red() and self.cards[count+1].num_rank == self.cards[count].num_rank-1):
                count += 1
            else:
                return False
        return True

    def pick(self, card):
        if self.can_pick(card):
            take = []
            for item in self.cards:
                if(item == card):
                    take.append(item)
                    if(self.cards.index(item)+1 != len(self.cards)):
                        if(self.help_pick(card)):
                            nice = self.cards[self.cards.index(item)+1:len(self.cards)]
                            for it in nice:
                                take.append(it)

                            self.cards = self.cards[0:self.cards.index(item)]
                            return take
                        else:
                            return
                    else:
                        self.cards.pop()
                else:
                    pass
            return take
        else:
            pass



class Home_Cell(Cell):
    pass

class Free_Cell(Cell):
    pass

class Cascade_Cell(Cell):
    pass

