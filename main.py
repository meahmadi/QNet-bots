from QNetbots.bots_ai.arabicnlp_bot import ArabicBot
from QNetbots.bots_access.livestream_bot import LiveStreamBot
from QNetbots.bots_pim.manager_bot import ManagerBot

import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    arabbot = ArabicBot('arabibot','dadashmeisam','https://quranic.network')
    arabbot.run()

    streambot = LiveStreamBot('streambot','DaDa$hMeiS@m','https://quranic.network')
    streambot.run()

    managerbot = ManagerBot('managerbot','mtnxoO6C','https://quranic.network')
    managerbot.run()
    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()
