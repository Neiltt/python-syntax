# 骰子遊戲
import random

dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐", # 0
        "│ ●   ● │", # 1
        "│ ●   ● │", # 2
        "│ ●   ● │", # 3
        "└───────┘", # 4
    ),
}
dice = []

num_dice = int(input("請輸入要擲幾次骰子:"))
for i in range(num_dice):
    dice_number = random.randint(1, 6)
    dice.append(dice_number)
print(dice)

# 圖像化
def get_dice_number(number):
    # number = 5
    dices = dice_art.get(6)
    for i in range(5):
        print(dice_art.get(number)[i])

for i in dice:
    get_dice_number(i)

print(sum(dice))