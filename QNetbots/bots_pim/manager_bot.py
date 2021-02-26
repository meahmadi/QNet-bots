# -*- coding: utf-8 -*-

import os
os.path.dirname(os.path.abspath(__file__)+'/../../')

from matrix_client.api import  MatrixHttpApi,MatrixRequestError

from QNetbots.core_bot_api.bot import Bot
from QNetbots.core_bot_api.mregex_handler import MRegexHandler
import random
import string
import subprocess
import pandas as pd
import time
from tinydb import TinyDB, Query
import uuid

class ManagerBot(Bot):
    greetings = {'dear': 'کاربر عزیز', 'not-recognized':'پیام شما مفهوم نبود، لطفا از الگوهای زیر استفاده کنید:',
                 'pattern':('!مدیر:کار:نام کاربر اسم کار','!مدیر:لیست')}

    def __init__(self, username, password, server):
        super(ManagerBot, self).__init__(username, password, server)

        # Add arabic regex handler
        manager_handler = MRegexHandler("!مدیر", self.process_command)
        self.add_handler(manager_handler)

        self.api = MatrixHttpApi(server)
        self.db = TinyDB('manager.db.json')


    def run(self):
        self.start_polling()

    def process_command(self, room, event):

        commandParts = event['content']['body'].split(':')
        if len(commandParts)>1:
            command = commandParts[1].strip()
        else:
            comamnd = ''
        if len(commandParts)>2:
            text = ':'.join(commandParts[2:]).strip()
        else:
            text = ''


        if command=='کار':
            if len(commandParts)>3:#user specified
                user_text = commandParts[2].strip()
                user_ = None
                if len(user_text)==0:
                    user_ = event['sender']
                for u in room.get_joined_members():
                    if user_text.strip() == u.get_display_name().strip():
                        user_ = u
                if user_ is None:
                    room.send_html(F"{user_text} is not name of Any User")
                    return
            else: user_ = event['sender']
            
            if len(commandParts)>4:#time Specified
                time_text = commandParts[3].strip()
                time_ = None
                if len(time_text) == 0:
                    time_ = ''
                time_=time_text
            else: time_ = ''

            task_detail = commandParts[-1].strip()
            print(user_)
            print(dir(user_))
            self.db.insert({'guid':str(uuid.uuid1()),'user_id':user_.user_id,'user_name':user_.get_display_name(),'time':time_,'insert_time':'','task':task_detail})
            room.send_html(F"task for {user_.get_display_name()}:{task_detail} ")
        elif command=='لیست':
            print("list works")
            room.send_text(F"{event['sender']}")
        else:
            #room.send_text(F"{event['sender']} {LiveStreamBot.greetings['dear']}: {LiveStreamBot.greetings['not-recognized']}"
            #       F"\n {LiveStreamBot.greetings['pattern']}")
            pass




