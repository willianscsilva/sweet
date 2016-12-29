import os, imp, sys
from bootstrap import environment
from config.app import app
from config.database import database
from container.container import Container

class App(app, database, Container):
    #APP_ENV, envFile, dataConf, dbInstance, inputInstance, logInstance = None, None, None, None, None, None
    APP_ENV, envFile, dataConf, inputInstance, logInstance = None, None, None, None, None
    prePath, path = '', None
    DSF  = None
    def __init__(self):
        self.handleContainer()
        self.path = os.path.realpath(os.path.abspath(sys.argv[0]) + '/../')
        self.getEnv()
        self.getFileConf()
        self.getDataFileConf()

        self.logInstance = self.importLogFile()
        self.logInstance.path = self.path

        sys.exit(0)

        #self.dbInstance = self.importDbFile()
        #self.dbInstance.LOG = self.logInstance
        #self.getDBConnectionsData()

        self.inputInstance = self.importInputFile()


    def getEnv(self):
        if environment.APP_ENV != '':
            self.APP_ENV = environment.APP_ENV

    def getFileConf(self):
        if self.APP_ENV != None:
            self.envFile = self.APP_ENV + "env"
        else:
            print("Error: Configure variable environment 'APP_ENV'")
            exit(1)

    def getDataFileConf(self):
        envModule = self.importEnvFile(self.path + "/bootstrap/" + self.envFile, self.envFile)
        self.dataConf = envModule.configEnviron(envModule)

    def importEnvFile(self, fullPath, className):
        pathClass = imp.load_source(className, fullPath + '.py')
        return getattr(pathClass, className)

    """def importDbFile(self):
        className = 'DB'
        pathClass = imp.load_source(className, self.path + "/" +self.aliases()['DB'] + '.py')
        return getattr(pathClass, className)

    def getDBConnectionsData(self):
        if self.dbInstance != None:
            self.dbInstance.dbConf = self.dataConf
            self.dbInstance.dbConnection = self.connections()"""

    def importInputFile(self):
        className = "Input"
        pathClass = imp.load_source(className, self.path + "/" + self.aliases()['input'] + '.py')
        return getattr(pathClass, className)

    def importLogFile(self):
        className = "Log"
        pathClass = imp.load_source(className, self.path + "/" + self.aliases()['Log'] + '.py')
        return getattr(pathClass, className)
