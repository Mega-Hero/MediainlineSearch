import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Buttons & Msgs

DEVS_BTN = InlineKeyboardMarkup([[
                 InlineKeyboardButton('π Harshith', url='https://t.me/MutyalaHarshith'),
                 InlineKeyboardButton('π₯³ MHgcHat', url='https://t.me/MHgchat')
                 ],
                 [
                 InlineKeyboardButton('π Back', callback_data="back_Clbs")
                 ]]
                  )

DEVS_MG = "β¨ Hai Iam Mutyala Harshith π"

helps_msg = """
βΈππππ πΈπ MH π±πππ π·πππ πππππππ!
How to Use me 
Ex:- `Radhe Shyam`
πYes It Simple Normally Movie Search bot 

"""

HelpBack_Btn = InlineKeyboardMarkup([[
                InlineKeyboardButton('π BacK', callback_data="HELP_BACK")
            ]])

ENSTART_BTN = InlineKeyboardMarkup([[
                InlineKeyboardButton('π Help', callback_data="HELP_CLB")
            ],
            [
                InlineKeyboardButton('π Harshith', url='https://t.me/MutyalaHarshith'),
                InlineKeyboardButton('π€© Develovepers', callback_data="DevsCallback")
            ],
            [
                InlineKeyboardButton('π MHGcHaT', url='https://t.me/MHGcHaT')
            ],
            [
                InlineKeyboardButton('πSearch hereπ
', switch_inline_query_current_chat=''),
                InlineKeyboardButton('π‘ Go inline', switch_inline_query='')
            ],
            [ 
                InlineKeyboardButton('π Change Language', callback_data="TE_CHANGE")
            ]
        ])

ENSTART_MSG = "Hi Welcome to **Harshith Media Search Bot**π­ βClick Help To more Helpsβ‘"

STAT_STICKER = ["CAACAgUAAxkBAAIaoGLFAh4HC8weC0J4x1c3HAVnoxSsAAJLBQACk63ZVTl1b7fDo-OpHgQ",
                "CAACAgUAAxkBAAIapGLFAlREvYMW3VfKH7VwhIBeaafMAAIvBQACaXfYVQXRbSbmknymHgQ",
                "CAACAgUAAxkBAAIanWLFAhD1jogzet85akKM_JwwhWnkAAJyBwACJrrZVf2J1QcUBqdVHgQ",
                "CAACAgUAAxkBAAIammLFAfvd9RBuotbZunrvn1lIU8kLAAIhBgAC3ZD5V8DbuSeu9KvqHgQ",
                "CAACAgUAAxkBAAIal2LFAeiA5Hb6vW9dBlgQmx_UVpT0AAI9AwAClKrpVqYLvURyUjbVHgQ"              
         ]  

CLOSE_BUTTON = InlineKeyboardMarkup([[
                InlineKeyboardButton('cloce', callback_data="cloce")
            ]])
