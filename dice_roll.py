# dice roll

import random

dice_faces = {
    1: ("-----",
        "|   |",
        "| o |",
        "|   |",
        "-----"),

    2: ("-----",
        "|o  |",
        "|   |",
        "|  o|",
        "-----"),

    3: ("-----",
        "|o  |",
        "| o |",
        "|  o|",
        "-----"),

    4: ("-----",
        "|o o|",
        "|   |",
        "|o o|",
        "-----"),

    5: ("-----",
        "|o o|",
        "| o |",
        "|o o|",
        "-----"),

    6: ("-----",
        "|o o|",
        "|o o|",
        "|o o|",
        "-----"),
}

num_dice = []

def dice(dice_qty):
    total_val = 0

    if (dice_qty > 10):
        return print("Woah, too much, try less than 10.")

    for die in range(dice_qty):
        rand = random.randrange(1,6,1)
        total_val += rand
        num_dice.append(rand)

    for i in range(dice_qty):
        for line in dice_faces.get(num_dice[i]):
            print(line)

    print(f'Total value of dice rolls: {total_val}')

dice_qty = int(input("How many dice rolls do you want? "))

dice(dice_qty)