import time

my_time = int(input("請輸入秒數:"))
for x in range(my_time, 0, -1):
    # 02:00
    seconds = x % 60
    minutes = x // 60 % 60
    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)
print("時間到!")