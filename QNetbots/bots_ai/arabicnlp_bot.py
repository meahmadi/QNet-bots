# -*- coding: utf-8 -*-
from QNetbots.core_bot_api.bot import Bot
from QNetbots.nlp.arabic_nlp import ArabicNLP

class ArabicBot(Bot):
    greetings = {'dear': 'عزیز', 'not-recoged':'پیام شما مفهوم نبود، لطفا از الگوهای زیر استفاده کنید:',
                 'pattern':('@arabi@erab@ جمله '+'@arabi@sarf@ عبارت ')}

    def __init__(self,USERNAME,PASSWORD,SERVER):
        super.__init__(USERNAME,PASSWORD,SERVER)
        self.arabic_nlp = ArabicNLP()

    def process_command(self, room, event):

        text = event['content']['body'].split('@')[-1].strip()
        command = event['content']['body'].split('@')[-2].strip()

        try:
            if command == 'erab':
                res = self.arabic_nlp.get_diacratics(text)
                room.send_text(F"{event['sender']} {ArabicBot.greetings['dear']}: {res}")

            elif command == 'sarf':
                res = self.arabic_nlp.get_properties(text)
                room.send_text(F"{event['sender']} {ArabicBot.greetings['dear']}: {res}")
            else:
                room.send_text(F"{event['sender']} {ArabicBot.greetings['dear']}: {event['not-recoged']}"
                           F"\n {ArabicBot.greetings['pattern']}")
        except:
            room.send_text(F"{event['sender']} {ArabicBot.greetings['dear']}: {event['not-recoged']}"
                           F"\n {ArabicBot.greetings['pattern']}")




