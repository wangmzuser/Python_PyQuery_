import MyModule
import sys,pprint
import copy
from copy import PyStringMap
from MyModule import ModuleDemo
import os
import time
import random
import fileinput

# ModuleDemo.test()
# ModuleDemo.hello()

ary_card = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
dct_card = {}
for i in range(1,16):
    if i<14:
        dct_card[i]=4
    else:
        dct_card[i]=1

def CheckCard(num):
    # print(dct_card)
    dct_card[num] -= 1
    if dct_card[num] == 0:
        ary_card.remove(num)
        dct_card.pop(num)
        # print(num)




if __name__ == '__main__':
    # pprint.pprint(MyModule.__path__)
    # a = [1,2,3,4]
    # b = copy.deepcopy(a)
    # a.append(5)
    # print(b)
    # # print(PyStringMap)
    # os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    # print('end')
    # str = time.localtime()
    # print(time.mktime(str))
    # struct_time = time.strptime("30 Nov 00", "%d %b %y")
    # print('struct_time :', struct_time)
    # print('time.mktime() :', time.mktime(struct_time))
    # print('time.strftime("%Y-%m-%d",struct_time)',time.strftime('%Y-%m-%d',struct_time))
    # print('time.asctime() :',time.asctime())
    # print('time.localtime() :',time.localtime())
    # print('time.mktime() :',time.mktime((2016,6,12,14,26,29,6,164,1)))
    # # print('time.sleep() :',time.sleep())
    # # print('time.strptime(string[.format]',time.strptime(str[.format])
    # print('time.time',time.time())

    ary_dct= dict()
    one_card_lst = []
    two_card_lst = []
    three_card_lst = []
    value_num = [None]*3
    number = 0
    # 选择你的位置
    while(True):
        try:
            number = input('please input you want postion : ')
            int(number)
        except  ValueError:
            print('input error')
        else:
            if int(number)<=3:
                break
            else:
                print('input error')
    # 确认地主(暂时随机)
    iBoss = int(random.uniform(1,4))

    # 发牌
    for i in range(1,18):
        for j in range(3):
            value_num[j]=random.sample(ary_card, 1)[0]
            CheckCard(value_num[j])
        # dct =dict(zip(value_name,value_num))
        # ary_dct[i] = dct
        one_card_lst.append(value_num[0])
        two_card_lst.append(value_num[1])
        three_card_lst.append(value_num[2])

    # 获取最后三张
    Boss_card = []
    for i in range(1,16):
        tmp = dct_card.get(i,0)
        if tmp!=0:
            for j in range(dct_card[i]):
                Boss_card.append(i)
    print('最后三张 :',Boss_card)

    # 整合最后三张牌，再整理牌组
    position_card = dict()
    position_card[1] = one_card_lst
    position_card[2] = two_card_lst
    position_card[3] = three_card_lst

    position_card[iBoss]+=Boss_card
    position_card[1].sort()
    position_card[2].sort()
    position_card[3].sort()

    print('%s : %s'% (number,position_card[int(number)]))


