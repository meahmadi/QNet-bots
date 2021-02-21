from QNetbots.bots_ai.arabicnlp_bot import ArabicBot
from QNetbots.core_bot_api.mregex_handler import MRegexHandler

if __name__ == "__main__":
    bot = ArabicBot('arabibot','','')
    # Add arabic regex handler
    arabic_handler = MRegexHandler("@arabi", bot.process_command())
    bot.add_handler(arabic_handler)
    # Start polling
    bot.start_polling()
    # Infinitely read stdin to stall main thread while the bot runs in other threads
    while True:
        input()
