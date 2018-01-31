from db.queries import get_rules


class UserCmd(object):
    '''
    This class represents the user commands
    '''

    def __init__(self, bot, metadata):
        self.bot = bot
        self.metadata = metadata
        super().__init__()

    def info(self):
        '''
        Show information about the user or group
        '''
        self.bot.sendMessage(chat_id=self.metadata['chat_id'], parse_mode='html',
                             text=('<b>ID INFO</b>\n'
                                   '==================\n'
                                   '<code>NOME</code> : {nome}\n'
                                   '<code>ID</code>   : {id}').format(
                                       nome=self.metadata['username'],
                                       id=self.metadata['user_id']),
                             reply_to_message_id=self.metadata['msg_id'])

    def help(self):
        help_msg = '''
Olá, sou o Tycot!
Segue minha lista de comandos:
    /info -> informações do grupo
    /link -> link do grupo
    /regras -> regras do grupo
    /leave -> sair do grupo
    /verifybook -> verifica o ultimo livro do packtpub
                          '''
        self.bot.sendMessage(self.metadata['user_id'], help_msg,
                             reply_to_message_id=self.metadata['msg_id'])

    def rules(self):
        rules = get_rules(self.metadata['chat_id'])
        if rules:
            self.bot.sendMessage(self.metadata['chat_id'], rules, parse_mode='Markdown',
                                 reply_to_message_id=self.metadata['msg_id'])
        else:
            self.bot.sendMessage(self.metadata['chat_id'], '*Sem regras!*', parse_mode='Markdown')
