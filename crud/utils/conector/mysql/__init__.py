import os
from sqlalchemy import create_engine
from crud.utils.conector.conf import Config
from crud.utils.conector.sql import SQLDBContext


def mysql_engine(produto, pool_size=1, max_overflow=25):
    dbname = Config.get("produto", produto)
    con_str = Config.get("database", dbname)
    engine = create_engine("mysql+pymysql://{}/{}".format(con_str, produto),
                           pool_size=pool_size, max_overflow=max_overflow, pool_recycle=30 * 60)
    return engine

class CadastroDBContext(SQLDBContext):

    def __init__(self, engine):
        super().__init__(engine)
