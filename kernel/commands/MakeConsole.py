import sys, json, os
from vendor.internal.regex import Regex

class MakeConsole(object):
    argumentIdentifier, regex, pathClass, commandToregister = None, None, None, None

    def getArgumentToMakeCommand(self):
        argumentIdentifier = self.getArgumentIdentifier()
        argumentToCommand = None
        if argumentIdentifier+1 < len(sys.argv):
            argumentToCommand = sys.argv[argumentIdentifier+1]
        return argumentToCommand

    def commandMakeConsole(self):
        if self.commandStruct != None:
            existsClass = self.checkClassExists()
            if existsClass == False and self.existsCommand == False:
                self.createClass()

    def checkClassExists(self):
        dictCommand = json.loads(self.commandStruct)
        fileName = dictCommand[self.commandValue] + ".py"
        return os.path.isfile(fileName)

    def createClass(self):
        self.writeClassFile()

    def writeClassFile(self):
       extension = ".py"
       if (self.pathClass != None) and (self.className != None):
           self.writeClass(self.pathClass + extension, self.className)

    def buildPathClass(self):
        if self.className != None and self.pathClass == None:
            directory = self.path + "/" + self.directoryController
            if not os.path.exists(directory):
                os.makedirs(directory)
            self.pathClass = self.path + "/" + self.directoryController + "/" + self.className
            self.commandToregister = self.directoryController + "/" + self.className

    def writeClass(self, path, className):
        space = " " * 4
        contentClass = "from vendor.internal.checkProcess import CheckProcess\n"
        contentClass = contentClass + "from bootstrap.app import App\n"
        contentClass = contentClass + "class " + className + "(object):\n" + space
        contentClass = contentClass + "app = None\n" + space
        contentClass = contentClass + "arguments = []\n" + space
        contentClass = contentClass + "def handle(self, app = App(), cp = CheckProcess()):\n" + space + space
        contentClass = contentClass + "self.app = app\n" + space + space
        contentClass = contentClass + "self.app.inputInstance.arguments = self.arguments"
        f = open(path, 'w')
        f.write(contentClass)
        f.close()

    def getDirectoryToSaveClass(self):
        if self.argumentToCommand != None:
            resultMatch = self.regex.pregMatch('/', self.argumentToCommand)
            if resultMatch != None:
                self.splitDirectoryNameClass()
            else:
                self.className = self.argumentToCommand

    def splitDirectoryNameClass(self):
       resultMatch = self.regex.pregMatch('(.*?)/(.*)', self.argumentToCommand)
       if resultMatch != None:
           self.directoryController = self.directoryController + resultMatch.group(1)
           self.className = resultMatch.group(2)
