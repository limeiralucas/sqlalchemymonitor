import logging

class SqlAchemyLogHandler(logging.Handler):
    def __init__(self, default_action, on_select=None, on_insert=None, on_update=None, on_not_recognized=None):
        super().__init__()
        self.setFormatter(logging.Formatter('SLH: %(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.setLevel(logging.INFO)
        self.default_action = default_action
        self.on_select = on_select
        self.on_insert = on_insert
        self.on_update = on_update
        self.on_not_recognized = on_not_recognized

    def emit(self, record):
        message = record.msg
        splitted = message.split(' ', maxsplit=1)
        if len(splitted) == 1:
            return

        operation, tail = splitted

        try:
            if operation == 'SELECT':
                arguments = tail.split('FROM', maxsplit=1)
                if len(arguments) > 1:
                    table = arguments[1].strip().split(' ', maxsplit=1)[0]
                    (self.on_select or self.default_action)(operation, table)
            elif operation == 'INSERT':
                arguments = tail.split('INTO', maxsplit=1)
                if len(arguments) > 1:
                    table = arguments[1].strip().split(' ', maxsplit=1)[0]
                    (self.on_insert or self.default_action)(operation, table)
            elif operation == 'UPDATE':
                arguments = tail.split(' ', maxsplit=1)
                if len(arguments) > 0:
                    table = arguments[0].strip()
                    (self.on_update or self.default_action)(operation, table)
            else:
                if self.on_not_recognized:
                    self.on_not_recognized(message)
        except:
            if self.on_not_recognized:
                self.on_not_recognized(message)