'''
@Author: YanQiaoYu
@Github: https://github.com/yanqiaoyu?tab=repositories
@Date: 2020-06-01 23:06:39
@LastEditors: YanQiaoYu
@LastEditTime: 2020-06-09 23:40:07
@FilePath: /Sleepway2work/sleepway2work.py
'''
from Alipay import Alipay
import uiautomator2 as u2
import os
#os.system("python3 -m weditor")

d = u2.connect()

a = Alipay(d)
#a.Sports()
#a.GoldTicket()
a.KickThiefChickenAndFeed()