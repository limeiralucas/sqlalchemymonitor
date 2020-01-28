import logging

class SqlAchemyLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.setFormatter(logging.Formatter('SLH: %(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.setLevel(logging.INFO)

    def emit(self, record):
        message = record.msg
        splitted = message.split(' ', maxsplit=1)
        if len(splitted) == 1:
            # Single term operation
            return

        operation, tail = splitted

        try:
            if operation == 'SELECT':
                arguments = tail.split('FROM', maxsplit=1)
                if len(arguments) > 1:
                    table = arguments[1].strip().split(' ', maxsplit=1)[0]
                    print('%s: %s' % (operation, table))
            elif operation == 'INSERT':
                arguments = tail.split('INTO', maxsplit=1)
                if len(arguments) > 1:
                    table = arguments[1].strip().split(' ', maxsplit=1)[0]
                    print('%s: %s' % (operation, table))
            elif operation == 'UPDATE':
                arguments = tail.split(' ', maxsplit=1)
                if len(arguments) > 0:
                    table = arguments[0].strip()
                    print('%s: %s' % (operation, table))
            else:
                # Not recognized operation
                return
        except:
            # Not recognized operation
            return