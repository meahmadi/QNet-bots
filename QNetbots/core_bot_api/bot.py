from core_bot_api.matrix_bot_api import MatrixBotAPI
from core_bot_api.mregex_handler import MRegexHandler
from core_bot_api.mcommand_handler import MCommandHandler



class Bot(object):
    def __init__(self, config):
        self.bot = MatrixBotAPI(config['USERNAME'], config['PASSWORD'], config['SERVER'])

    def add_handlers(self, handlers):
        for handler in handlers:
            self.bot.add_handler(handler)

    @staticmethod
    def create_regex_base(regex, callback_f):
        return MRegexHandler(regex, callback_f)

    @staticmethod
    def create_command(command, callback_f):
        return MCommandHandler(command, callback_f)
