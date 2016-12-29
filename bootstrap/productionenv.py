class productionenv(object):
    def configEnviron(self):
        return {'APP_ENV':'local',
        'APP_DEBUG':'true',
        'DB_DRIVER':'mysql',
        'DB_HOST':'',
        'DB_PORT':'',
        'DB_DATABASE':'',
        'DB_USERNAME':'',
        'DB_PASSWORD':'',

        'DB_HOST_OTHER':'',
        'DB_PORT_OTHER':'',
        'DB_DATABASE_OTHER':'',
        'DB_USERNAME_OTHER':'',
        'DB_PASSWORD_OTHER':'',

        'REDIS_HOST':'redis',
        'REDIS_USERNAME':'',
        'REDIS_PASSWORD':'',
        'REDIS_PORT':'6379',
        'REDIS_DATABASE':''}
