"""
Solution for task 4_1
"""
import os
import sys


def sumcard(cardidx):
    summ = 0
    for line in cards[cardidx]:
        summ += sum([item for item in line if item > -1])
    return summ

INPUT_FILE_NAME = 'task_4_input.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r") as input_file:
        INPUTS_RAW = input_file.readlines()

draw = []
cards = []
card = []
for line in INPUTS_RAW:
    if "," in line:
        numbers = [int(item) for item in line.strip().split(",")]
        draw = numbers
    elif len(line) > 1:
        numbers = [int(item) for item in line.strip().split()]
        card.append(numbers)
    elif len(card):
        cards.append(card)
        card = []

orig_cards = cards[:]
def next_winner():
    for drawn in draw:
        for (idxcard, card) in enumerate(cards):
            for line in card:
                if drawn in line:
                    idxrow = line.index(drawn)
                    line[idxrow] = -1
                    rowsum = sum([card[y][idxrow] for y in range(5)])
                    if sum(line) == -5 or rowsum == -5:
                        result = sumcard(idxcard) * drawn
                        return (orig_cards.index(card), idxcard, result)

while cards:
    (card_idx, idxcard, result) = next_winner()
    print("result: %d (%d)" % (result, card_idx))
    cards.pop(idxcard)
    
