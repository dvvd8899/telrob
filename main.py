#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  @desc:
  @author: dvvd8899
  @contact: dvvd8899@gmail.com
"""

import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '''
    Hello, I am robot./大家好，我是机器人
    /start :查看此信息
    /help :查看IT服务内容
    /数字 座位号 :请求对应的服务
    ''')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    May I help you? 请问有什么可以帮您:
   =================================
   1. WIFI Connection/WIFI接入
   2. Software Problems/软件问题
   3. Printer Problems/打印机故障
   4. Network Problems/网络问题
   5. Monitor Problems/显示器故障
   6. No Sound/没有声音
   7. Slow Laptop/电脑很卡
   8. Request Mouse/申请鼠标
   9. Request Keyboard/申请键盘
   10. Request Headset/申请耳机
   11. Request Monitor/申请显示器
   12. Request Laptop/申请笔记本电脑
   ==================================
    Notice: Please attach your seat number.
    注意：请告知您的座位号!!!
    ''')

@bot.message_handler(commands=['1','2','3','4','5', '6', '7', '8', '9', '10', '11', '12'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='Copy it./收到，祝您工作愉快！@davidsq @JCManicia @RichardSoriao')

@bot.message_handler()
def echo(message):
    bot.reply_to(message, text='Invalid Input./无效的输入，请重新选择')

if __name__ == '__main__':
    bot.polling()

