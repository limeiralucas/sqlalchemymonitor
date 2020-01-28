from .handler import SqlAchemyLogHandler

import logging

__version__ = '0.1'

def init_sql_alchemy_monitor(handler, logger_name='sqlalchemy.engine.base.Engine'):
    sql_alchemy_log = logging.getLogger('sqlalchemy.engine.base.Engine')
    sql_alchemy_log.setLevel(logging.DEBUG)
    sql_alchemy_log.addHandler(handler)