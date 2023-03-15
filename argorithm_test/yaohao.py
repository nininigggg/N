""""摇号小程序
1、允许用户最多选3次
2、每次20个供用户选择
3、京【A-Z】-【XXXXX】，可以是数字和字母的组合
"""
import random
import string

count = 0
while count < 3:
    car_nums = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)  # 第一个字母大写
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        c_num = f"京{n1}-{n2}"
        car_nums.append(c_num)
        print(c_num)

    choice = input("输入你喜欢的号：").strip()
    if choice in car_nums:
        print(f"恭喜你选中了新车牌号：{choice}")
        exit("GOOD LUCK.")
    else:
        print("不合法的选择...")

    count += 1

"""
random模块用法：
1.random.choice('abced1224')
>>>'d'
2.s="ahefjfoi78789"
random.sample(s, 3)
>>>['a','i','9']
3.random.randint(1,100)
>>>79

string模块用法：
string.ascii_letters
>>>'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_uppercase
>>>'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase
>>>'abcdefghijklmnopqrstuvwxyz'
string.punctuation #特殊字符
>>>'~!@##$$%%^^&**()'
string.digits
>>>'0123456789'

"""
