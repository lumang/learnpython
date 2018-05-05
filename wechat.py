import itchat
import re
import io
from  os import  path
import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

import os
from matplotlib import pyplot as plt
def draw(datas):
    for key in datas.keys():
        plt.bar(key, datas[key])

    plt.legend()
    plt.xlabel('sex')
    plt.ylabel('rate')
    plt.title("Gender of lumang's friends")
    plt.show()

def parse_friedns():
    itchat.login()
    text = dict()
    friedns = itchat.get_friends(update=True)[0:]
    print(friedns)
    male = "male"
    female = "female"
    other = "other"
    for i in friedns[1:]:
        sex = i['Sex']
        if sex == 1:
            text[male] = text.get(male, 0) + 1
        elif sex == 2:
            text[female] = text.get(female, 0) + 1
        else:
            text[other] = text.get(other, 0) + 1
    total = len(friedns[1:])
    print("男性好友： %.2f%%" % (float(text[male]) / total * 100) + "\n" +
          "女性好友： %.2f%%" % (float(text[female]) / total * 100) + "\n" +

          "不明性别好友： %.2f%%" % (float(text[other]) / total * 100))
    draw(text)



if __name__ == '__main__':
    parse_friedns()
    
    
