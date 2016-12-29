import os, datetime

class Log(object):
    pathLog, path = "/storage/app/log/", None

    def createLogDir(self, folder=None):
        if os.path.isdir(self.path + self.pathLog) != True:
            os.mkdir(self.path + self.pathLog, mode=0o777)
        if folder != None:
            if os.path.isdir(self.path + self.pathLog + folder) != True:
                os.makedirs(self.path + self.pathLog + folder, mode=0o777)

    def writeLog(self, folderLog, fileLog, content):
        now = datetime.datetime.now()
        curFormateStrDate = now.strftime("%Y-%m-%d %H:%M:%S")

        self.createLogDir(self)
        self.createLogDir(self, folderLog)
        f = open(self.path + self.pathLog + folderLog + "/" + fileLog, 'a')
        f.write(curFormateStrDate + " --- " + content + '\n\n')
        f.close()
