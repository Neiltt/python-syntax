import random

player = None
computer = None

running = True
options = ("剪刀", "石頭", "布")
while running:
    player = input("請輸入剪刀石頭布:")
    while player not in options:
        player = input("輸入錯誤，請輸入剪刀石頭布:")
    computer = random.choice(options)
    print(f"玩家:{player}, 電腦:{computer}")

    if player == computer:
        print("平手")
    elif player == "剪刀" and computer == "布":
        print("玩家勝利")
    elif player == "石頭" and computer == "剪刀":
        print("玩家勝利")
    elif player == "布" and computer == "石頭":
        print("玩家勝利")
    else:
        print("電腦勝利")
    play_again = input("是否在一局y/n:")
    if not play_again == "y":
        running = False
print("謝謝來玩")

