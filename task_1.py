"""
Solution for task 1_1
"""

import os

INPUT_FILE_NAME = 'task_1_input.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r") as input_file:
        INPUTS_RAW = input_file.readlines()

INPUTS = []
for input_line in INPUTS_RAW:
    input_line.strip()
    INPUTS.append(int(input_line))

counter = 0
for idx in range (1, len(INPUTS)):
    if INPUTS[idx-1] < INPUTS[idx]:
        counter += 1

print("Increases: %d" % counter)

counter = 0
for idx in range (4, len(INPUTS)+1):
    if sum(INPUTS[idx-4:idx-1]) < sum(INPUTS[idx-3:idx]):
        counter += 1
print("Window increases: %d" % counter)

