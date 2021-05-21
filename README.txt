Extended due date (4:00PM | 17, October 2019)

Full Freecell by Geir Anderson
Freecell accounts for all invalid moves
Invalid moves don't crash and don't alter the board
Has a quit command "goodbye" w/o quotes
Runs with any seed
Has a win condition, which displays a message and quits
Individual cards can be moved, if valid
Multiple cards can be moved at once, if valid
Displays the entire board and displays moves

To run:
python3 freecell.py 234897
python3 freecell.py
python3 freecell.py <replace with a string of digits>

To play:
    To quit:
    goodbye
    To move:
    RS O# P#
        R = rank of bottom most card being moved
        S = suit of bottom most card being moved
        O# = the letter and number of the cell where the card(s) is/are located
        P# = the letter and number of the destination cell

Goal:
Sort and place all of the cards into Homecells, each Homecell can contain only 1 suit.


Checkpoint for Freecell by Geir Anderson

Runs with the specified command from the handout and works regardless of seed and works with no seed
python3 freecell.py 234897

card.py and freecell.py contain functional code

Prints out all cards as [RS], where R is printed as the rank and S is printed as the suit. Outputs using ANSI colouring to colour code the red and black suits on a white background.
