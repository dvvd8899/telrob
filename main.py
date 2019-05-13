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
    /start ：查看此信息
    /help ：查看IT服务内容
    /数字 座位号 ：请求对应的服务
    如：/5 M-48 则表示M-48座位显示器故障
    ''')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    May I help you? 请问有什么可以帮您:
   ============
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
   ============
    Notice: Please attach seat number.
    注意:请告知您的座位号!!!
    ''')

@bot.message_handler(commands=['1'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    WIFI Connection
    ''')

@bot.message_handler(commands=['2'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Software Problems
    ''')

@bot.message_handler(commands=['3'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Printer Problems
    ''')

@bot.message_handler(commands=['4'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Network Problems
    ''')


@bot.message_handler(commands=['5'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Monitor Problems
    ''')

@bot.message_handler(commands=['6'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    No Sound
    ''')

@bot.message_handler(commands=['7'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Slow Laptop
    ''')

@bot.message_handler(commands=['8'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Request Mouse
    ''')

@bot.message_handler(commands=['9'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Request Keyboard
    ''')

@bot.message_handler(commands=['10'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Request Headset
    ''')

@bot.message_handler(commands=['11'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Request Monitor
    ''')

@bot.message_handler(commands=['12'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Copy it./收到，祝您工作愉快！
    @davidsq @JCManicia @robbiesarmiento @RichardSoriao
    Request Laptop
    ''')

@bot.message_handler(commands=['ithelpit'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    /runas  RunAs Administrator
    /isp    Show ISP IP list
    ''')

@bot.message_handler(commands=['runas'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    Sample: C:\Windows\System32\runas.exe /user:DESKTOP-FSQIAD6\Administrator /savecred "D:\FlyVPN\FlyVPN.exe"
    ''')

@bot.message_handler(commands=['isp'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='''
    SRASI1-WAN2
    61.238.96.242
    https://61.238.96.242:9509

    SRASI2-PORT2
    45.195.88.82
    https://45.195.88.82:9509

    SUNIWAY-PORT3
    203.85.84.114
    https://203.85.84.114:9509
    
    SUNIWAY_CN-PORT4
    14.152.48.162
    https://14.152.48.162:9509
    ''')


@bot.message_handler()
def echo(message):
    bot.reply_to(message, text='Invalid Input./无效的输入，请重新选择')

if __name__ == '__main__':
    bot.polling()

