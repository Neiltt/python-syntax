# 字典推導式
# ex1
cityes_in_f = {
    'LA': 120,
    'New York': 65,
    'Chicago': 50,
    'Miami': 150
}
cityes_in_c = {key: (value -32 ) * (5/9) for key,value in cityes_in_f.items()}
# print(cityes_in_f)
# print(cityes_in_c)

# ex2
weather = {
    '台北': '晴天',
    '台中': '雨天',
    '台南': '多雲',
    '桃園': '晴天',
    '宜蘭': '雨天',
}
summy_weather = {key: value for key,value in weather.items() if value == '晴天'}
# print(summy_weather)

# ex4 條件判斷+函式
cityes_in_f = {
    'LA': 120,
    'New York': 65,
    'Chicago': 50,
    'Miami': 150
}

def check_temp(value):
    if value>= 70:
        return '熱'
    elif value >= 40:
        return '溫暖'
    else:
        return '冷'

description_cities = {key: check_temp(value) for key,value in cityes_in_f.items() }
print(description_cities)