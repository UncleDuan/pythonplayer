from wxpy import *
import requests
from datetime import datetime
import time

# from apscheduler.schedulers.blocking import BlockingScheduler#定时框架

bot = Bot(cache_path=True)
# tuling = Tuling(api_key=你的api )#机器人api

def send_weather(location):
    # 准备url地址
    path = "http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=? "
    url = path % location
    response = requests.get(url)
    result = response.json()
    # 如果城市错误就按照濮阳发送天气
    if result["error"] != 0:
        location = " 武汉 "
        url = path % location
        response = requests.get(url)
        result = response.json()
    str0 = ("早上好！这是今天的天气预报！……机器人：PyChatBot ")
    results = result["results"]
    # 取出数据字典
    data1 = results[0]
    # 取出城市
    city = data1["currentCity"]
    str1 = "你的城市: %s " % city
    # 取出pm2.5值
    pm25 = data1["pm25"]
    str2 = "Pm值    : %s " % pm25
    str3 = "污染指数: "
    result1 = results[0]
    weather_data = result1["weather_data"]
    data = weather_data[0]
    temperature_now = data["date"]
    str4 = "当前温度: %s" % temperature_now
    wind = data["wind"]
    str5 = "风向    : %s" % wind
    weather = data["weather"]
    str6 = " 天气    : %s" % weather
    str7 = "温度    : %s " % data["temperature"]
    message = data1["index"]
    str8 = "穿衣    : %s " % message[0]["des"]
    str9 = "我很: %s " % message[2]["des"]
    str10 = "运动    : %s " % message[3]["des"]
    str11 = "紫外线 : %s" % message[4]["des"]
    str = str0 + str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8 + str9 + str10 + str11
    return str
# 好友列表

# my_friends = []

# my_friends = bot.friends()

# my_friends.pop(0)

# 发送函数
def send_message():
    # 给全体好友发送
    friend = bot.friends().search("huhui1")[0]
    friend.send("Hello")
    # bot.file_helper.send('Hello from wxpy!')
    # 发送成功通知我
    bot.file_helper.send(send_weather("微信 "))
    bot.file_helper.send("发送完毕 ")
send_message()