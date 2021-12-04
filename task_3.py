"""
Solution for task 3_1
"""

import os

INPUT_FILE_NAME = 'task_3_input.txt'
if os.path.exists(INPUT_FILE_NAME):
    with open(INPUT_FILE_NAME, "r") as input_file:
        INPUTS_RAW = input_file.readlines()

INPUT = [ line.strip() for line in INPUTS_RAW ]
LEN = len(INPUT[0])

ones = [0] * LEN
for line in INPUT:
    for idx, val in enumerate(line):
        if val == "1":
            ones[idx] += 1

gamma_rate = ["0"] * LEN
epsilon_rate = ["0"] * LEN

for idx, val in enumerate(ones):
    if val >= len(INPUT) // 2:
        gamma_rate[idx] = "1"
    else:
        epsilon_rate[idx] = "1"

gamma_rate_int = int("".join(gamma_rate), 2)
epsilon_rate_int = int("".join(epsilon_rate), 2)
print(f"Gamma rate: {gamma_rate} ({gamma_rate_int})")
print(f"epsilon rate: {epsilon_rate} ({epsilon_rate_int})")
print(f"Answer: {gamma_rate_int * epsilon_rate_int}")

"""  ------------------------------------ """
OXYGEN = INPUT[:]
CO2 = INPUT[:]
# find dominant first for every index
for idx in range(LEN):
    print("iteration %d" % idx)
    print("ox: %d" % len(OXYGEN))
    print("co2: %d" % len(CO2))
    # find dominant OXYGEN idx
    if len(OXYGEN) > 1:
        ones = 0
        for item in OXYGEN:
            if item[idx] == "1":
                ones += 1
        filter_by = "1" if ones >= len(OXYGEN) / 2 else "0"
        OXYGEN = [item for item in OXYGEN if item[idx] == filter_by]

    # find dominant CO2 idx
    if len(CO2) > 1:
        ones = 0
        for item in CO2:
            if item[idx] == "1":
                ones += 1
        filter_by = "0" if ones >= len(CO2) / 2 else "1"
        CO2 = [item for item in CO2 if item[idx] == filter_by]

ox_int = int("".join(OXYGEN[0]), 2)
co2_int = int("".join(CO2[0]), 2)
print("Oxygen: %s (%d)" % (OXYGEN, ox_int))
print("CO2: %s (%d)" % (CO2, co2_int))
print(f"Answer: {ox_int * co2_int}")
