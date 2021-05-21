#Freecell code by Geir Anderson
#!/usr/bin/python3
import deck
from card import Card
from cell import Cell, Home_Cell, Free_Cell, Cascade_Cell
import sys

#printer for cells
def print_blank():
    print("\033[0;30;48;5;15m"+("|  |"), end = '')

def print_card(card):
    if card.is_red() is True:
        print("\033[1;31;48;5;15m", end = '')
    else:
        print("\033[0;30;48;5;15m", end = '')
    print(card, end = '')

def print_list(card_list):
    if len(card_list) == 0:
        print_blank()

    else:
        for card in card_list:
            print_card(card)

def is_done(command):
    s = "".join(command)

    if s == "GOODBYE":
        return True

    return False

def win(homes):
    for home in homes:
        if len(home) != 16:
            return False
    return True

def to_card(chars):
    valid_rank = "ATJQK23456789"
    valid_suit = "CDHS"
    if (chars[0] not in valid_rank or chars[1] not in valid_suit):
        print("Invalid Input! Watch your inputs!")
        return None

    temp_rank = chars[0]
    temp_suit = chars[1]
    rank = 1
    suit = 0
    if temp_rank == 'A':
        rank = 1
    elif temp_rank == 'T':
        rank = 10
    elif temp_rank == 'J':
        rank = 11
    elif temp_rank == 'Q':
        rank = 12
    elif temp_rank == 'K':
        rank = 13
    else:
        rank = int(temp_rank)

    if temp_suit == 'C':
        suit = 0
    elif temp_suit == 'D':
        suit = 1
    elif temp_suit == 'H':
        suit = 2
    else:
        suit = 3

    ret_card = Card(rank, suit)

    return ret_card

#init cascades of cards
def init_cascade(shuffled):
    cascades = [[], [], [], [], [], [], [], []]
    ret_cascades = []
    i = 0
    j = 0
    c = 7
    t = 3
    for card in shuffled:
        if (j == 1 and c == 7):
            t = 7
            c -= 1
        if i < t:
            cascades[i].append(card)
            i = i + 1
        else:
            cascades[i].append(card)
            j = j + 1
            i = 0

    for cascade in cascades:
        ret_cascades.append(Cascade_Cell(cascade[:]))
    return ret_cascades

def init_home():
    homes = []
    i = 0
    while i < 4:
        homes.append(Home_Cell([]))
        i += 1
    return homes

def init_free():
    frees = []
    i = 0
    while i < 4:
        frees.append(Free_Cell([]))
        i += 1
    return frees

def display_full(homes = [], frees = [], cascades = []):
    i = 1
    j = 1
    k = 1
    for home in homes:
        print("\033[0;30;48;5;15m"+(f"H{i}:  "), end = '')
        print_list(home.cards)
        i += 1
        print("\n")
    for free in frees:
        print("\033[0;30;48;5;15m"+(f"F{j}:  "), end = '')
        print_list(free.cards)
        j += 1
        print("\n")
    for cascade in cascades:
        print("\033[0;30;48;5;15m"+(f"C{k}:  "), end = '')
        print_list(cascade.cards)
        k += 1
        print("\n")

    print("\033[0;32;48;5;15m")

def move(moving, to, homes, frees, cascades):
    if moving is None:
        print("Invalid move! Don't try to sneak cards out!")
        return -1
    elif to[0] == 'C':
        if cascades[int(to[1])-1].can_place(moving[0]):
             cascades[int(to[1])-1].place(moving)
        else:
            print("Invalid move! Same rank, suit, or color!")
            return -1
    elif to[0] == 'F':
        if len(moving) > 1:
            print("Invalid move! Too many cards!")
            return -1
        if (len(frees[int(to[1])-1]) == 0):
            frees[int(to[1])-1].place(moving)
        else:
            print("Invalid move! Full Freecell!")
            return -1
    elif to[0] == 'H':
        if len(moving) > 1:
            print("Invalid move! Too many cards!")
            return -1
        if (len(homes[int(to[1])-1].cards) == 0 and moving[0].num_rank != 1):
            print("Invalid move! Only Aces can be placed in empty Homecell")
            return -1
        elif homes[int(to[1])-1].can_place(moving[0]):
            homes[int(to[1])-1].place(moving)
        else:
            print("Invalid move! Can't place this card here!")
            return -1
    else:
        print("How did you get here?")
        return -1
    if win(homes):
        print("\033[0;34;48;5;15m!!!YOU WIN!!!")
        return 1

    return 0


def maybe_move(act, homes, frees, cascades):
    if (len(act) == 0 or len(act) == 2):
        print("Commands for moving cards should go \"RS O# P#\" or \"RS\" to send to a home if able")
        return

    valid_cell = "CFH"
    valid_num = "12345678"
    moving = []
    temp_card = to_card(list(act[0]))
    if temp_card is None:
        return
    else:
        if len(act) == 1:
            count = 0
            to_id = 1
            to = []
            while count < 4:
                if (homes[count].cards == [] or temp_card.suit == homes[count].cards[0].suit):
                    to = ['H', to_id]
                    break
                else:
                    to_id += 1
                    count += 1
            if(homes[count].cards == [] and temp_card.num_rank != 1):
                to = []

            elif not homes[count].can_place(temp_card):
                to = []

            else:
                count = 0

            if to != []:
                while count < 4:
                    if temp_card in frees[count].cards:
                        moving = frees[count].pick(temp_card)
                        success = move(moving, to, homes, frees, cascades)
                        if success == -1:
                            frees[count].place(moving)
                        else:
                            return success
                    else:
                        count += 1

            else:
                count = 0
                to_id = 1
                while count < 4:
                    if temp_card in frees[count].cards:
                        return
                    else:
                        if len(frees[count]) > 0:
                            count += 1
                            to_id += 1
                        else:
                            to = ['F', to_id]
                            break

            count = 0
            while count < 8:
                if temp_card in cascades[count].cards:
                    moving = cascades[count].pick(temp_card)
                    if (moving is None or to == []):
                        print("Invalid move!")
                        return
                    elif len(moving) == 1:
                        success = move(moving, to, homes, frees, cascades)
                    else:
                        success = -1
                    if success == -1:
                        cascades[count].place(moving)
                    else:
                        return success
                else:
                    count += 1


            print("Failed to move")
            return 0



        temp_from = list(act[1])
        temp_to = list(act[2])
        if (len(temp_from) != 2 or len(temp_to) != 2 or temp_from[0] not in valid_cell or temp_to[0] not in valid_cell or temp_from[1] not in valid_num or temp_to[1] not in valid_num):
            print("Invalid Input! Watch your inputs!")
            return 0
        if temp_from[0] == 'F':
            if int(temp_from[1]) > 4:
                print("There are only 4 Freecells! Try another number.")
                return 0
            else:
                from_free = (int(temp_from[1])-1)
                if frees[from_free].can_pick(temp_card):
                    moving = frees[from_free].pick(temp_card)
                    success = move(moving, temp_to, homes, frees, cascades)
                    if success == -1:
                        frees[from_free].place(moving)
                    return success
                else:
                    print("Invalid move! Can't take from an empty Freecell!")
                    return 0

        if (temp_to[0] == 'H' or temp_to[0] == 'F'):
            if int(temp_to[1]) > 4:
                print("There are only 4 Homecells and 4 Freecells! Try another number.")
                return 0
        if temp_from[0] == 'H':
            print("Invalid move! You can't take cards from the Homecells!")
            return 0

        if temp_from[0] == 'C':
            from_cas = (int(temp_from[1])-1)
            if cascades[from_cas].can_pick(temp_card):
                moving = cascades[from_cas].pick(temp_card)
                success = move(moving, temp_to, homes, frees, cascades)
                if success == -1:
                    cascades[from_cas].place(moving)
                return success
            else:
                print("Invalid move!")
                return 0




def command_to_list (command):
    passed_list = []
    temp_str = command.upper()
    passed_list = temp_str.split()
    return passed_list

def main():
    seed = 0

    if len(sys.argv) <= 1:
        seed = None
    else:
        seed = int(sys.argv[1])

    shuffled = [card for card in deck.shuffle_deck(Card, seed)]
    cascades = init_cascade(shuffled)
    frees = init_free()
    homes = init_home()
    win = 42

    print("\033[48;5;15m")

    display_full(homes, frees, cascades)

    for command in sys.stdin:
        parsed = command_to_list(command)
        if is_done(parsed):
            break
        else:
            win = maybe_move(parsed, homes, frees, cascades)
        display_full(homes, frees, cascades)
        if win == 1:
            return


main()
print("\033[0m")

