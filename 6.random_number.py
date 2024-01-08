# 猜數字遊戲
import  random

low = 1
high = 100
number = random.randint(low, high)
guesses = 0

while True:
    guess = int(input(f"猜一個介於{low}~{high}數字: "))
    guesses += 1
    if guess < number:
        print("你猜的數字太小了")
    elif guess > number:
        print("你猜的數字太大了")
    else:
        print(f"恭喜你猜對了，數字就是{number}")
        print(f"你總共猜了{guesses}")
        break