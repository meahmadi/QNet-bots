from QNetbots.bots_ai.arabicnlp_bot import ArabicBot

if __name__ == "__main__":
    arabbot = ArabicBot('arabibot','','')
    arabbot.run()
    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()
