class My_Class:
    def getString(self):
        self.my_object = input()
    def printString(self):
        print(self.my_object.upper())
p1 = My_Class()
p1.getString()
p1.printString()