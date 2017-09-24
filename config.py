# coding=utf-8

DB_config = {
     'db_type': 'mongodb',
    #'db_type': 'mysql',

    'mysql': {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'charset': 'utf8',
    },
    'redis': {
        'host': 'localhost',
        'port': 6379,
        'password': '123456',
        'db': 1,
    },
    'mongodb':{
        'host': '127.0.0.1',
        'port': 27017,

    }
}

database = 'ipproxy'
free_ipproxy_table = 'free_ipproxy'
httpbin_table = 'httpbin'
log_level = 'INFO'  # 0 10 20 30 40 for debug, info, warning, error, critical relatively
data_port = 8000
TestMode = False
