import json, sys, imp, os

class UserCommand(object):

    def checkUserCommand(self):
        if len(sys.argv) > 1:
            self.userCommand = sys.argv[1]
            if self.userCommand != None:
                self.getCommandValue()
                return self.checkCommandExists()
        return False

    def requireUserClass(self):
        className = self.getName(self.getClassName()).replace('/', '')
        pathClass = imp.load_source(className, self.getClassName() + '.py')
        classInstance = getattr(pathClass, className)
        classInstance.handle(classInstance)

    def getName(self, pathClass):
        resultMatch = self.regex.pregMatch('/[A-Za-z 0-9]+$', pathClass)
        return resultMatch.group()

    def getClassName(self):
        pathFile = self.path + "/" + self.userClass
        return pathFile
