---
layout: post
title:  "Telegram Bot-(1)"
date:   2019-03-25-kafka/2019-03-25
desc: "Quick test on writing code snippets in a blog post"
keywords: "Telegram, Bot"
categories: [Telegram]
tags: [JS,Jekyll]
icon: icon-html
---

## Telegram Bot Development Test


### 테스트 환경 준비

- 사용자의 기분에 기초해 이모지(emoji)로 반응하는 봇을 만드는 간단한 예제입니다.

- Telegram Bot 개발하기 위해서는 python-telegram-bot 라이브러리를 사용합니다.

- Module 설치
  
>pip install python-telegram-bot

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-15-57-04.png){: .wh50 .center}

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-15-57-17.png){: .wh45 .center}

- 또한 이모지 아이콘을 위한 emoji 라이브러리를 설치해 기분에 따라 적절한 표현을 사용자에게 반환 할 수 있다.

>pip install emoji

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-15-57-46.png){: .wh45 .center}

### 실행 방법

- 나만의 봇을 개발하기위해 먼저 Window에 **[Telegram](http://www.telegram.pe.kr/){:target="_blank"}**을 다운로드합니다. 그리고 계정을 휴대폰 번호를 이용하여 등록합니다.

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-16-01-34.png){: .wh50 .center}

- 봇을 등록하기 위해 BotFather 를 검색하고 클릭해 대화를 시작해서 토큰을 받아야합니다.

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-16-05-28.png){: .wh65 .center}

- BotFather 과 대화를 시작한 후 ***/newbot*** 혹은 ***/enable*** 같은 커맨드를 사용해 봇을 구성합니다.

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-16-06-38.png){: .wh65 .center}

- 생성할 봇 이름과 username을 설정해주어야 봇 생성이 가능합니다.

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-16-07-13.png){: .wh60 .center}

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-16-07-26.png){: .wh60 .center}

- 챗봇에 필요한 내용을 코딩합니다.

```
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import emoji
 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
 
def start(bot, update):
    keyboard = [
                [InlineKeyboardButton("Happy", callback_data='1'),
                 InlineKeyboardButton("Whatever", callback_data='2')],
                [InlineKeyboardButton("Sad", callback_data='3')]]
 
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text("Hey there! How do you feel today?", reply_markup=reply_markup)
    
def button(bot, update):
    query = update.callback_query
    if query.data == '1':
        em = emoji.emojize(':smile:', use_aliases=True)
        bot.editMessageText(text="Oh wow! %s" % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
 
    if query.data == '2':
        em = emoji.emojize(':expressionless:', use_aliases=True)
        bot.editMessageText(text="Does it matter? %s" % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
    
    if query.data == '3':
        em = emoji.emojize(':disappointed:', use_aliases=True)
        bot.editMessageText(text="Oh man!? %s" % em,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
 
def help(bot, update):
    update.message.reply_text('Use /start to test this bot.')
 
def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))
 
# Create the Updater and pass it your bot's token.
 
#updater = Updater('Token')
updater = Updater('602011398:AAGOUYgGqTWzoEi7JgwXZetG9Omy3SC9rJA')
 
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)
 
# Start the Bot
updater.start_polling()
 
# Run the bot untill the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
```

- 코딩 완료 후 파일을 실행합니다.

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-16-09-29.png){: .wh55 .center}

- 챗 봇에서 버튼 클릭을 하면 내용확인이 가능합니다.

![](/static/assets/img/blog/2019-03-26-telegram-bot/2019-03-26-16-10-06.png){: .wh70 .center}

To be continued...