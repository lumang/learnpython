import requests
import os
import time
import json

#TODO json 解析
file = "D:/locked.csv"
file_line = open(file)
all_lines = file_line.readlines()
i=0
for num  in all_lines:
    # 判断是否是数字
    # 
    if((num!="\r\n")&num.isdigit()):
       print("开始解锁ID = "+num)
       i+=1
       url ="https://utc.365sale.com/wenzhou/consumer/rest/v11/promoters/"+num.strip()+"/unlock"
       print("发送请求 "+url)
       headers={'Content-Type':'application/json'}
       r = requests.put(url,headers=headers)
       print(r.text)
       print("id "+num.strip()+" 已解锁")
       print("请稍等。。。\n")
       time.sleep(3)# 等待3s ，否则服务器Dos
    else:
        pass

file_line.close()
print("解锁处理完成 "+str(i))#must be str not int



