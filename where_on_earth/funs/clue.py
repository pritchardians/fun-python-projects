import sys


def give_clue(clue_number, clues):
    clue_text = 'Do you want your '
    if clue_number == 0:
        clue_text += 'first '
    elif clue_number == 1:
        clue_text += 'second '
    else:
        clue_text += 'third '
    clue_text += 'clue? (y/n) \n'
    clue_wanted = input(clue_text).lower()
    if clue_wanted == 'y':
        print(clues[clue_number])
    else:
        print('Fair enough. Goodbye!')
        sys.exit(0)
