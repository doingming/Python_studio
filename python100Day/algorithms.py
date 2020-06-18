#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 数据结构和算法1





""" 穷举法例子：百钱百鸡和五人分鱼。 """

# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
for x in range(20):                                             # 最多买 二十只 公鸡
    for y in range(33):                                         # 最多买 三十三只 母鸡
        z = 100 - x - y                                         # 剩下的买 小鸡
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)




# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼  


fish = 6                                    # 鱼的数量必然大于 6 （5+1）
while True:
    total = fish
    enough = True
    for _ in range(5):                      # 循环五次
        if (total - 1) % 5 == 0:            # 每次仍一条鱼刚好分五份
            total = (total - 1) // 5 * 4
        else:                               # 否者说明鱼数量不够需加大
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5




""" 贪婪法例子 """

# 假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
# 很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。
# 名称	    价格（美元）	重量（kg）
# 电脑	    200	            20
# 收音机    20	            4
# 钟	    175	            10
# 花瓶	    50	            2
# 书	    10	            1
# 油画	    90	            9



