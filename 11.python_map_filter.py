# map (函式, 可迭代[列表])

store = [
    ('襯衫', 200),
    ('褲子', 300),
    ('夾克', 500),
    ('襪子', 200)
]

to_euros = lambda data: (data[0], data[1] * 0.82)
store_euros = list( map(to_euros, store) )
print(store_euros)

to_usd = lambda data: (data[0], data[1] / 30)
store_usd = list( map(to_usd, store) )
print(store_usd)

for item in store_usd:
    print(item)

# filter過濾可迭代資料結構
friends = [
    ('Mark', 20),
    ('John', 30),
    ('Jack', 14),
    ('Amy', 17)
]
age_filter = lambda data: data[1] >= 18
can_drink_friends = list( filter(age_filter, friends))
print(can_drink_friends)
for friend in can_drink_friends:
    print(friend[0],friend[1])