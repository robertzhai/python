# -*- coding: utf-8 -*-



ConfMysql = {

    'driver':'mysql+mysqlconnector',
    'db_user':'test',
    'db_password':'test',
    'host':'localhost',
    'port':'3306',
    'db':'python',
}

if __name__ == '__main__':
    print ConfMysql['driver'] + '://' + ConfMysql['db_user'] + ':' + ConfMysql['db_password'] + \
        '@' + ConfMysql['host'] + ':' + ConfMysql['port'] + '/' + ConfMysql['db']