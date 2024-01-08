menu = {
    "披薩": 200,
    "漢堡": 100,
    "薯條": 49,
    "可樂": 35
}
cart = []
total = 0
print("菜單")
print("-" * 30)
for item, price in menu.items():
    print(f"{item}:{price}")

while True:
    food = input("請輸入菜單項目:")
    if food == "q":
        break
    elif menu.get(food) is None:
        print("無此商品")
    else:
        cart.append(food)
        total += menu.get(food)
        print(food, end=" ")
print(f"總共: {total}元")
