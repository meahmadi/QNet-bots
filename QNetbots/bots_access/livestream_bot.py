# -*- coding: utf-8 -*-

import os
os.path.dirname(os.path.abspath(__file__)+'/../../')

from QNetbots.core_bot_api.bot import Bot
from QNetbots.core_bot_api.mregex_handler import MRegexHandler
import random
import string
import subprocess
import pandas as pd
import time
class LiveStreamBot(Bot):
    greetings = {'dear': 'کاربر عزیز', 'not-recognized':'پیام شما مفهوم نبود، لطفا از الگوهای زیر استفاده کنید:',
                 'pattern':('@پخش#حذف#نام‌فایل '+'@پخش#ارسال#نام‌فایل '+'@پخش#نو#نام‌فایل ')}

    def __init__(self, username, password, server):
        super(LiveStreamBot, self).__init__(username, password, server)

        # Add arabic regex handler
        live_handler = MRegexHandler("@پخش", self.process_command)
        self.add_handler(live_handler)

    @staticmethod
    def get_password(length=10):
        # choose from all lowercase letter
        letters = string.ascii_lowercase + '0123456789' + string.ascii_uppercase
        password = ''.join(random.choice(letters) for i in range(length))
        return password

    def run(self):
        self.start_polling()

    def process_command(self, room, event):

        text = event['content']['body'].split('#')[-1].strip()
        command = event['content']['body'].split('#')[-2].strip()


        if command=='نو':
            password = LiveStreamBot.get_password()
            table = pd.DataFrame({'لینک':[F'https://quranic.network/{password}'], 'نام ضبط':[F'{text}'],'رمز':[F"{password}"]}).to_html(index=False)
            room.send_html(F"{event['sender']} {LiveStreamBot.greetings['dear']}: {table}")
            room.send_text(F"{event['sender']} لطفا ۷ ثانیه صبر کنید ")
            time.sleep(5)
            subprocess.call(['sudo', 'bash', '/stream/run.sh',password, text])

        elif command=='حذف':
            subprocess.call(['sudo', 'rm', '-r', F'/home/element/recordings/{text}*', text])
        else:
            room.send_text(F"{event['sender']} {LiveStreamBot.greetings['dear']}: {LiveStreamBot.greetings['not-recognized']}"
                   F"\n {LiveStreamBot.greetings['pattern']}")




