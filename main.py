from QNetbots.bots_ai.arabicnlp_bot import ArabicBot
from QNetbots.bots_access.livestream_bot import LiveStreamBot

if __name__ == "__main__":
    arabbot = ArabicBot('arabibot','','')
    arabbot.run()

    streambot = LiveStreamBot('streambot','','')
    streambot.run()
    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()
