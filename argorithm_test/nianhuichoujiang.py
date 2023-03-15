"""
年会抽奖
1、共抽3次，第一次抽三等奖30名；第二次抽2等奖6名；第三次抽根一等奖3名
2、每个员工只能中奖一次，不能重复
"""
import random

em_ids = list(range(300))  # 生成员工工号
winner_list = []  # 中奖清单
for i in range(3):
    if i == 1:
        # 三等奖
        t3 = random.sample(em_ids, 30)
        print(f"编号为", random.sample(em_ids, 30), "的员工获得了三等奖")
        winner_list.append(t3)

    elif i == 2:
        # 二等奖
        t2 = random.sample(em_ids, 6)
        if t2 not in winner_list:
            print(f"编号为", random.sample(em_ids, 6), "的员工获得了二等奖")
            winner_list.append(t2)

    else:
        # 一等奖
        t1 = random.sample(em_ids, 3)
        if t1 not in winner_list:
            print(f"编号为", random.sample(em_ids, 3), "的员工获得了一等奖")
            winner_list.append(t1)
            break
