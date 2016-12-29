from threading import Thread
import sys, time, os

class cThread(object):
    assync = False
    def newThread(self, function, functionArgs):
        t=Thread(target=function, args=functionArgs)
        t.start()
        if self.assync == False:
            t.join()

    def numCpus(self):
        try:
            return int(os.sysconf('SC_NPROCESSORS_ONLN'))
        except Exception as e:
            print("Error: " + str(e))
