# coding:utf-8

"""
    @author  : linkin
    @email   : yooleak@outlook.com
    @date    : 2018-10-05
"""

#代理连接数据库
_DB_SETTINGS = {
    'backend'	:'mysql',		    #数据库类型选择 (MongoDB?MySQL?...)
    'host'		:'localhost',		#数据库主机
    'port'		:3306,				#数据库主机服务端口
    'user'		:'',		    #数据库用户
    'passwd'	:'',	#密码
    'database'  :'proxy'            #使用数据库名
}

#存储代理数据的数据表
_TABLE = {
    'standby'   :'standby',     #经过验证器验证后，存放有效代理的数据表
    'stable'    :'stable',      #经过检测器循环检测后，存放高分稳定代理的数据表
}

#创建数据库和数据表的sql文件路径
create_db_path      = 'sql/createDB'
create_table_path   = 'sql/createTable'