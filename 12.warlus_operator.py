# 獠牙運算符

foods = []
# 1
# while True:
#     food = input("你喜歡的食物:")
#     if food == "q":
#         break
#     foods.append(food)
# print(foods)

# 2
# while food := input("你喜歡的食物:"):
#     if food == "q":
#         break
#     foods.append(food)
# print(foods)

# 3
while (food := input("你喜歡的食物:")) != 'q':
    foods.append(food)
print(foods)