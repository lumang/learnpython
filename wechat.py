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


def parse_signature():
    itchat.login()
    siglist=[]
    friends=itchat.get_friends(update=True)[1:]
    for i in friends:
        signature = i["signature"].strip().replace("span","").repalce("class","").replace("emoji","")
        rep =re.compile("1f\d+\W*|[<>/=]")
        signature = rep.sub("",signature)
        siglist.append(signature)
    text ="".join(siglist)
    with io.open('text.txt','a',encoding='utf-8') as f:
        wordlist=jieba.cut(text,cut_all=True)
        word_space_split=" ".join(wordlist)
        f.write(word_space_split)
        f.close()

def draw_signature():
    text = open(u'text.txt',encoding='utf-8').read()
    color

if __name__ == '__main__':
    parse_friedns()
    
    
