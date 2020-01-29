from .handler import SqlAchemyLogHandler

import logging

__version__ = '0.1'

def init_sql_alchemy_monitor(default_action, on_select=None, on_insert=None, on_update=None, on_not_recognized=None, logger_name='sqlalchemy.engine.base.Engine'):
    handler = SqlAchemyLogHandler(default_action, on_select, on_insert, on_update, on_not_recognized)
    sql_alchemy_log = logging.getLogger('sqlalchemy.engine.base.Engine')
    sql_alchemy_log.setLevel(logging.DEBUG)
    sql_alchemy_log.addHandler(handler)