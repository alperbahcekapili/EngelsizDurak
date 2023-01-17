from datetime import datetime
import os


class Logger:

    def __init__(self):
        self.logfile = self.openNewLogger()

    def openNewLog(self,):
        newfile = os.path.join(os.getcwd(), "Logs", datetime.now().strftime("%m %d %Y, %H %M %S"))
        newfile = open(newfile, "w+", encoding="utf-8")
        return newfile


    def warning(self, text):
        now = datetime.now().strftime("%m %d %Y, %H %M %S")
        self.logfile.write(now + " WARNING: " + text + "\n")

    def information(self, text):
        now = datetime.now().strftime("%m %d %Y, %H %M %S")
        self.logfile.write(now + " INFORMATION: " + text + "\n")

    def error(self, text):
        now = datetime.now().strftime("%m %d %Y, %H %M %S")
        self.logfile.write(now + " ERROR: " + text + "\n")
