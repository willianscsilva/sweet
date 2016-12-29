import json, sys, os
from pathlib import Path

class ListCommands(object):
    commandRegisterFile = "command.register"
    def listAllCommands(self):
        pathFile = self.path + "/" + self.commandRegisterFile
        allCommands = []
        commandRegister = Path(pathFile)
        if commandRegister.is_file():
            with open(pathFile, 'r') as aFile:
                for aLine in aFile:
                    allCommands.append(json.loads(aLine.rstrip()))
            self.formatCommands(allCommands)

    def formatCommands(self, commands):
        formatOut = "Commands:\n\n"
        for cmd in commands:
            for keys in cmd:
                formatOut +=  "\tCommand: " + keys + "\n" + "\tClass Path: " + cmd[keys] + "\n\n"
        print(formatOut)
