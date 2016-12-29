import sys, copy

class Input(object):
    arguments = []
    def getArgument(self, name=None):
        args = self.removeArtisanCommandInArguments(self)
        if name != None and self.arguments != [] and args != []:
            index = None
            for i, items in enumerate(self.arguments):
                if name == items:
                    index = i
            if index != None:
                if index < len(args):                    
                    return args[index]

    def removeArtisanCommandInArguments(self):
        args = copy.copy(sys.argv) #attribute in new memory
        args.remove(sys.argv[0])   #remove 'artisan.py' from the list
        args.remove(sys.argv[1])   #remove 'command'  from the list
        return args
