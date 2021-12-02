"""
Solution for task 1_1
"""

import os

INPUT_FILE_NAME = 'task_2_input.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r") as input_file:
        INPUTS_RAW = input_file.readlines()

XPOS = 0
YPOS = 0

XXPOS = 0
YYPOS = 0
AIM = 0

for input_line in INPUTS_RAW:
    input_line.strip()
    cmd = input_line.split(" ")
    if cmd[0] == "up":
      YPOS -= int(cmd[1])
      AIM -= int(cmd[1])
    elif cmd[0] == "down":
      YPOS += int(cmd[1])
      AIM += int(cmd[1])
    elif cmd[0] == "forward":
      XPOS += int(cmd[1])
      XXPOS += int(cmd[1])
      YYPOS += AIM * int(cmd[1])
    else:
      print("WTF: %s" % cmd)

print(XPOS * YPOS)

print(XXPOS * YYPOS)
