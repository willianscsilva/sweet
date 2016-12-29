#!/usr/bin/env python3
import sys, time, os
from vendor.internal.regex import Regex
from kernel.commands.MakeConsole import MakeConsole
from kernel.commands.Command import Command
from kernel.commands.UserCommand import UserCommand
from kernel.commands.ListCommands import ListCommands

class Artisan(MakeConsole, Command, UserCommand, ListCommands):
    internalCommands = ["make:console", "--command", "--list", "--help"]
    internalDescription = ["Create the class of a command.", "Create the command.", "List all commands created by user.", "Show all artisan arguments."]
    internalExample = [
                          "python3 artisan.py make:console [Folder name inside of controller]/[ClassName] --command=[command-name]",
                          "python3 artisan.py make:console [Folder name inside of controller]/[ClassName] --command=[command-name]",
                          "python3 artisan.py --list",
                          "python3 artisan.py --help"
                      ]
    makeConsoleId, commandId, listId, helpId = 0, 1, 2, 3
    flagMakeConsole, flagCommandId, flagList, flagHelp = False, False, False, False
    idInternalCommand, argumentToCommand, regex, argument = None, None, None, None
    directoryController, className, path = "app/src/Controller/", None, None

    def __init__(self):
        self.path = os.path.realpath(os.path.abspath(sys.argv[0]) + '/../')
        self.regex = Regex()
        self.readArguments()

    def readArguments(self):
        for index, eachArg in enumerate(sys.argv):
            countInternalCommands = self.handle(index, eachArg)
        self.executeCommands(countInternalCommands)

    def handle(self, identifier, argument):
        argumentToCommand = None
        iterInternalCommands = 0
        for index, eachCommand in enumerate(self.internalCommands):
            resultMatch = self.regex.pregMatch(eachCommand, argument)
            if resultMatch != None:
                self.setIdInternalCommand(index)
                if index == self.makeConsoleId:
                    self.flagMakeConsole = True
                    self.setArgumentIdentifier(identifier)
                    argumentToCommand = self.getArgumentToMakeCommand()
                elif index == self.commandId:
                    self.flagCommandId = True
                    self.setRawCommand(argument)
                elif index == self.listId:
                    self.flagList = True
                elif index == self.helpId:
                    self.flagHelp = True
                if argumentToCommand != None:
                    self.setArgumentToCommand(argumentToCommand)
                self.stackingCalls()
                iterInternalCommands = iterInternalCommands + 1
        return iterInternalCommands

    def stackingCalls(self):
        self.getArgumentToCommand()
        self.getDirectoryToSaveClass()
        self.getCommandValue()
        self.buildPathClass()
        self.buildCommandStruct()

    def executeCommands(self, internalCommands):
        if internalCommands > 0:
            self.apllyInternalCommands()
        else:
            self.executeUSerCommands()

    def apllyInternalCommands(self):
        if self.flagMakeConsole and self.flagCommandId:
            self.command2LessCommand()
            self.commandMakeConsole()
        elif self.flagList:
            self.listAllCommands()
        elif self.flagHelp:
            self.help()

    def help(self):
         print("Artisan arguments:\n")
         for i, ic in enumerate(self.internalCommands):
             print("\tArgument: " + "\t" + ic +
                   "\n\tDescription: " + "\t" + self.internalDescription[i] +
                   "\n\tExample: " + "\t" + self.internalExample[i] + "\n")

    def executeUSerCommands(self):
        exists = self.checkUserCommand()
        if exists == True:
            self.requireUserClass()

    def setIdInternalCommand(self, idInternalCommand):
        self.idInternalCommand = idInternalCommand

    def getIdInternalCommand(self):
        return self.idInternalCommand

    def setArgumentToCommand(self, argumentToCommand):
        self.argumentToCommand = argumentToCommand

    def getArgumentToCommand(self):
        return self.argumentToCommand

    def setArgumentIdentifier(self, argumentIdentifier):
        self.argumentIdentifier = argumentIdentifier

    def getArgumentIdentifier(self):
        return self.argumentIdentifier

if __name__ == '__main__':
    Art = Artisan()
