# 列表推導式

# before
def square(x):
    return x * x
list = []
for i in range(1, 11):
    list.append(square(i))
print(list)

# after
squares = [i*i for i in range(1,11)]
print(f"列表推導式: {squares}")

grades = [1, 4, 49, 64, 81, 100, 9, 16, 25, 36, 44]
passed_grades = [g for g in grades if g >= 60]
print(f"及格分數: {passed_grades}")