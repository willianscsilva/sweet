from vendor.internal.checkProcess import CheckProcess
from bootstrap.app import App
class Test(object):
    app = None
    arguments = []
    def handle(self, app = App(), cp = CheckProcess()):
        self.app = app
        self.app.inputInstance.arguments = self.arguments