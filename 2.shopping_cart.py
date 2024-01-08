goods = []
prices = []

while True:
    good = input("請輸入商品:")
    if good.lower() == "q":
        break
    price = float(input("請輸入金額:"))
    goods.append(good)
    prices.append(price)

for index, good in enumerate(goods):
    print(f"第 {index+1} 個商品，商品名稱:{good}，價格:{prices[index]}")

total = sum(prices)
print(f"總價格:${total}")
