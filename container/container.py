from container.DBInstance import DBInstance

class Container(object):
    def handleContainer(self):
        listClass = self.registerClass()
        for classes in listClass:
            print(classes)

    def registerClass(self):
        print(DBInstance().handle('DB'))
        return [ DBInstance().handle('DB'), ]
