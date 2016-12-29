class database(object):
    def connections(self):
        return {'mysql':
                    {
                    'driver':'mysql',
                    'host':'DB_HOST',
                    'database':'DB_DATABASE',
                    'username':'DB_USERNAME',
                    'password':'DB_PASSWORD',
                    'port':'DB_PORT',
                    'charset':'utf8',
                    'collation':'utf8_unicode_ci'
                    },
                'mysqlother':
                    {
                    'driver':'mysql',
                    'host':'DB_HOST_OTHER',
                    'database':'DB_DATABASE_OTHER',
                    'username':'DB_USERNAME_OTHER',
                    'password':'DB_PASSWORD_OTHER',
                    'port':'DB_PORT_OTHER',
                    'charset':'utf8',
                    'collation':'utf8_unicode_ci'
                    },
                'redis':
                    {
                    'driver':'redis',
                    'host':'REDIS_HOST',
                    'username':'REDIS_USERNAME',
                    'password':'REDIS_PASSWORD',
                    'port':'REDIS_PORT',
                    'database':'REDIS_DATABASE'
                    }
                }
