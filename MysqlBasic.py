# coding:utf-8 
import requests
import json
import pymysql
#配置数据库
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"",
    "database":"studio"
}
db = pymysql.connect(**config)

# 获取游标 cursor = db.cursor()
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

#执行查询
sql = "SELECT * FROM sedc_patient "
cursor.execute(sql)
#查询1个
resOne = cursor.fetchone()
#查所有
resAll = cursor.fetchall()
#查指定个数
resMany = cursor.fetchmany(10)
print("id:"+resOne['id'])

#转换为json字符串
jsonstr = json.dumps(resOne)
print(jsonstr)

#字符串转换为dict字典
dict = json.loads(jsonstr)

#关闭游标 关闭数据连接
cursor.close()
db.close()
