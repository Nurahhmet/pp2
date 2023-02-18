class Parent1:
    word1 = " "
    def __init__(self, color1, number1):
        self.color1 = color1
        self.number1 = number1
    def printinfo(self):
        print(self.color1)
        print(self.number1)
    def setword1(self, word1):
        self.word1 = word1
    def getword1(self):
        print(self.word1)

class Parent2:
    word2 = " "
    def __init__(self, color2, number2):
        self.color2 = color2
        self.number2 = number2
    def printinfo(self):
        print(self.color2)
        print(self.number2)
    def setword2(self, word2):
        self.word2 = word2
    def getword2(self):
        print(self.word2)

class BabyBoy(Parent1, Parent2):
    word3 = " "
    def __init__(self, color1, number1, color2, number2):
        super().__init__(color1, number1)
        super().__init__(color2, number2)
        self.color3 = color1 + color2
        self.number3 = number1 + number2
    def printinfo(self):
        print(self.color3)
        print(self.number3)
    def setword3(self):
        self.word3 = self.word1 + self.word2
    def getWord3(self):
        print(self.word3)


z = BabyBoy("blue", 7, "white", 7)
z.setword1("Toyota")
z.setword2("Camry")
z.setword3()
z.printinfo()
z.getWord3()