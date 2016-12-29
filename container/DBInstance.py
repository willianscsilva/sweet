import os, imp, sys
from config.app import app
class DBInstance( object ):
    dbInstance, path = None, None

    def handle(self, className):
        self.path = os.path.realpath(os.path.abspath(sys.argv[0]) + '/../')
        self.dbInstance = self.importDbFile(className)
        return self.dbInstance

    def importDbFile(self, className):
        #className = 'DB'
        pathClass = imp.load_source(className, self.path + "/" +app.aliases(app)[className] + '.py')
        return getattr(pathClass, className)
