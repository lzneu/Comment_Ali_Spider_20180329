# -*- coding: UTF-8 -*-
import pandas as pd
from Config.config import *
import pymysql


''''连接mysql, 返回connnection
'''''


def connect_mysql(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if isLocal:
        # 打开数据库连接
        conn = pymysql.connect(host, username, password, db)

    else:
        pass
        # conn = MongoClient([ALIYUN_MONGO_CONN_ADDR1, ALIYUN_MONGO_CONN_ADDR2], replicaSet=ALIYUN_MONGO_REPLICAT_SET)
        # if username and password:
        #     # 授权. 这里的user基于admin数据库授权
        #     conn.power.authenticate(username, password)

    return conn.cursor()

