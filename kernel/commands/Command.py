from vendor.internal.regex import Regex
import json, sys, os
from pathlib import Path

class Command(object):
    command, userCommand, userClass, regex, commandValue, commandStruct, existsCommand = None, None, None, None, None, None, None
    commandRegister = "command.register"
    def command2LessCommand(self):
        self.registerCommand()

    def getCommandValue(self):
        if self.command != None:
            resultMatch = self.regex.pregMatch('(.*?)=(.*)', self.command)
            if resultMatch != None:
                self.commandValue = resultMatch.group(2)
        elif self.userCommand != None:
            self.commandValue = self.userCommand

    def buildCommandStruct(self):
        if self.commandValue != None:
            self.commandStruct = json.JSONEncoder().encode({self.commandValue: self.commandToregister})

    def registerCommand(self):
        if self.commandStruct != None:
            self.existsCommand = self.checkCommandExists()
            if self.existsCommand == False:
                pathFile = self.path + "/" + self.commandRegister
                f = open(pathFile, 'a')
                f.write(self.commandStruct + '\n')
                f.close()

    def checkCommandExists(self):
        pathFile = self.path + "/" + self.commandRegister
        commandRegister = Path(pathFile)
        if commandRegister.is_file():
            with open(pathFile, 'r') as aFile:
                for aLine in aFile:
                    registeredCommand = json.loads(aLine.rstrip())
                    if self.commandValue in registeredCommand:
                        className = registeredCommand[self.commandValue]
                        if className:
                            if self.userCommand != None:
                                self.userClass = className
                            return True
        return False


    def setRawCommand(self, command):
        self.command = command

    def getRawCommand(self):
        return self.command
