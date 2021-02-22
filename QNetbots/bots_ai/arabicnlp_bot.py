# -*- coding: utf-8 -*-

import os
os.path.dirname(os.path.abspath(__file__)+'/../../')

from QNetbots.core_bot_api.bot import Bot
from QNetbots.nlp.arabic_nlp import ArabicNLP
from QNetbots.core_bot_api.mregex_handler import MRegexHandler

class ArabicBot(Bot):
    greetings = {'dear': 'کاربر عزیز', 'not-recognized':'پیام شما مفهوم نبود، لطفا از الگوهای زیر استفاده کنید:',
                 'pattern':('@عربی#اعراب# جمله '+'@عربی#صرف# عبارت ')}

    def __init__(self, username, password, server):
        super(ArabicBot, self).__init__(username, password, server)
        self.arabic_nlp = ArabicNLP()

        # Add arabic regex handler
        arabic_handler = MRegexHandler("@عربی", self.process_command())
        self.add_handler(arabic_handler)

    def run(self):
        self.start_polling()

    def process_command(self, room, event):

        text = event['content']['body'].split('#')[-1].strip()
        command = event['content']['body'].split('#')[-2].strip()


        try:
            if self.arabic_nlp.get_normal_alef(command)==self.arabic_nlp.get_normal_alef('اعراب'):
                res = self.arabic_nlp.get_diacratics(text)
                room.send_text(F"{event['sender']} {ArabicBot.greetings['dear']}: {res}")

            elif command == 'صرف':
                res = self.arabic_nlp.get_properties(text)
                room.send_html(F"{event['sender']} {ArabicBot.greetings['dear']}: {res}")
            else:
                    room.send_text(F"{event['sender']} {ArabicBot.greetings['dear']}: {ArabicBot.greetings['not-recognized']}"
                           F"\n {ArabicBot.greetings['pattern']}")
        except:
            room.send_text(F"{event['sender']} {ArabicBot.greetings['dear']}: {ArabicBot.greetings['not-recognized']}"
                           F"\n {ArabicBot.greetings['pattern']}")




