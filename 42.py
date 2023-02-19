# getString 获取键盘输入的字符串
# printString 输出字符串进过upper函数变大写的字母

class change:
    def __init__(self): #都得有
        pass
    def getString(self):
        self.string = str(input()) #键盘输入的字符串
    def printString(self):
        print(self.string.upper()) #变大写
example = change()
example.getString()
example.printString()