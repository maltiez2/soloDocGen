def slprint(text):
    _SameLinePrinter().print(text)

def slclear():
    _SameLinePrinter().clear()

def slstop():
    _SameLinePrinter().stop()

class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class _SameLinePrinter(metaclass=_Singleton):
    def __init__(self, newLine = False):
        self._maxSize = 0
        self._stopped = True
        if newLine:
            self.newLine = '\n'
        else:
            self.newLine = '\r'

    def print(self, printString):
        printStringLength = len(printString)
        if (printStringLength > self._maxSize):
            self._maxSize = printStringLength
        for i in range(self._maxSize - printStringLength):
            printString += " "
        print(printString, end=self.newLine)
        self._stopped = False

    def clear(self):
        if not self._stopped:
            printingString = ""
            for i in range(self._maxSize):
                printingString += " "
            self._maxSize = 0
            print(printingString, end='\r')
            self._stopped = True

    def stop(self):
        if not self._stopped:
            self._maxSize = 0
            print("")
            self._stopped = True