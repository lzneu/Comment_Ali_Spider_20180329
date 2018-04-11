#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_sql.py
# @Author: 投笔从容
# @Date  : 2018/4/3
# @Desc  : 测试mysql

import pymysql
from Config.config import *

db = pymysql.connect(ALIYUN_MYSQL_HOST, ALIYUN_MYSQL_USERNAME, ALIYUN_MYSQL_PASSWORD, ALIYUN_MYSQL_DB, charset='utf8')
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM PRODUCTS \
WHERE (CATEGORY_TYPE = '%d' AND CATEGORY_ID = '%d' AND STORE_ID = '%d')" % (
1, 845024448691351552, 2)
# 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
count = len(results)

print(count)