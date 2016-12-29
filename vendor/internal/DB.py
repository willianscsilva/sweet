import MySQLdb, sys, redis
class DB(object):
    dbConf, dbConnection, conn, cursor, driver, dbDriver = None, None, None, None, None, None
    server, user, passwd, db, port = None, None, None, None, None
    LOG, MYSQL_DRIVER, REDIS_DRIVER = None, "mysql", "redis"
    redisDb = None

    def connect(self):
        try:
            self.getDataConnection(self)

            if self.dbDriver == self.MYSQL_DRIVER:
                self.connMysql(self)
            elif self.dbDriver == self.REDIS_DRIVER:
                self.connRedis(self)
        except Exception as e:
            raise Exception("DB-Error: " + str(e) + " in method connect()")

    def connMysql(self):
        self.conn = MySQLdb.connect(self.server, self.user, self.passwd, self.db, port = self.port, charset = "utf8", use_unicode = True, local_infile = True, connect_timeout=9999 )
        self.conn.autocommit(False)
        self.cursor = self.conn.cursor()
        return self.conn

    def connRedis(self):
        self.conn = redis.StrictRedis(host=self.server, port=self.port, db=self.getRedisDataBase(self))

    def setRedisDataBase(self, dataBase):
        self.redisDb = dataBase

    def getRedisDataBase(self):
        return self.redisDb

    def getDataConnection(self):
        try:
            self.getDBDriver(self)

            self.server = self.dbConf[self.dbConnection[self.driver]['host']]
            self.user = self.dbConf[self.dbConnection[self.driver]['username']]
            self.passwd = self.dbConf[self.dbConnection[self.driver]['password']]
            self.db = self.dbConf[self.dbConnection[self.driver]['database']]
            self.port = int(self.dbConf[self.dbConnection[self.driver]['port']])
            self.dbDriver = self.dbConnection[self.driver]['driver']
        except Exception as e:
            raise Exception("DB-Error: " + str(e) + " in method getDataConnection()")

    def setDBDriver(self, driver):
        self.driver = driver

    def getDBDriver(self):
        return self.driver

    def redisSet(self, key, value):
        try:
            return self.conn.set(key, value)
        except Exception as e:
            raise Exception("DB-Error: " + str(e) + " in method redisSet()")

    def redisGet(self, key):
        try:
            return self.conn.get(key)
        except Exception as e:
            raise Exception("DB-Error: " + str(e) + " in method redisGet()")

    def select(self, query):
        try:
            arr = None
            if self.cursor.execute(query):
               arr = [ dict(line) for line in [zip([ column[0] for column in self.cursor.description], row) for row in self.cursor.fetchall()] ]
            return arr
        except Exception as e:
            raise Exception("DB-Error: " + str(e) + " in method select()")

    def count(self, query, field):
       try:
           if self.cursor.execute(query):
               arr = [ dict(line) for line in [zip([ column[0] for column in self.cursor.description], row) for row in self.cursor.fetchall()] ]
               return arr[0][field]
       except Exception as e:
           raise Exception("DB-Error: " + str(e) + " in method count()")

    def insert(self, query):
        try:
            if self.cursor.execute(query):
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            self.conn.rollback()
            raise Exception("DB-Error: " + str(e) + " in method insert()")

    def update(self, query):
        try:
            if self.cursor.execute(query):
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            self.conn.rollback()
            raise Exception("DB-Error: " + str(e) + " in method update()")

    def loadDataInFile(self, query):
        try:
            if self.cursor.execute(query):
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            self.conn.rollback()
            raise Exception("DB-Error: " + str(e) + " in method loadDataInFile()")

    def statement(self, query):
        try:
            if self.cursor.execute(query):
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            self.conn.rollback()
            raise Exception("DB-Error: " + str(e) + " in method statement()")

    def connClose(self):
        self.cursor.close()
        self.conn.close()
