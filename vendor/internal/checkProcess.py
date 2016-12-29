import sys, os

class CheckProcess(object):
    pid = None
    def __init__(self):
        self.pid = os.getpid()
        psResult = self.getProcessInExecution()
        if psResult:
            print("Exists a instance of this process in execution...\nTerminating this.")
            sys.exit(0)

    def getProcessInExecution(self):
        command = ""
        for key, args in enumerate(sys.argv):
            if key != 0:
                command +=  args + " "
        command = command[0:len(command)-1]
        ps = "ps aux | grep -v '/bin/sh -c' | grep '%s' | grep -v 'grep' | grep -v '%s'" % (command, self.pid)
        result = os.system(ps)
        if result == 0:
            return True
