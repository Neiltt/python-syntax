# Lambda
# ex1
def double(x):
    return x * 2

double2 = lambda x: x * 2
# print(double(20))
# print(double2(30))

# ex2
multuply = lambda x, y: x * y
# print(multuply(30, 20))

# ex3 lambda 變數: T:結果1 T:條件 else 結果2
result = lambda x: f"{x}是偶數" if x % 2 == 0 else f"{x}是奇數"
# print(result(101))

# ex4
full_name = lambda first_name, last_name: f"{first_name} P{last_name}"
print(full_name("Neil", "Ch"))