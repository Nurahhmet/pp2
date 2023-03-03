# 1
class with2meth:
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

UserInput = with2meth()
UserInput.getString()
UserInput.printString()