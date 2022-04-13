import sys, re, ast
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from calcUI import Ui_MainWindow
from calcMath import *

class CalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def process(self, bool):
        processOperation()

class OperationsTransformer(ast.NodeTransformer):
    ops = {
        ast.Add: 'add(',
        ast.Sub: 'sub(',
        ast.Mult: 'mul(',
        ast.Div: 'div(',
        ast.LShift: 'root(',
        ast.RShift: 'power('
    }

    def visit_BinOp(self, node):
        self.generic_visit(node)
        if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
            value = eval(f'{self.ops[type(node.op)]} {node.left.n}, {node.right.n})')
            return ast.Num(n=value)
        return node

def processOperation():
    input = ui.lineEdit.text()
    input = input.replace("^", ">>")
    input = input.replace("√", "<<")
    try:
        tree = ast.parse("result = " + input)
        ast.fix_missing_locations(OperationsTransformer().visit(tree))

        ldict = {}
        exec(compile(tree, filename="", mode="exec"), globals(), ldict)
        result = ldict['result']
    except SyntaxError:
        result = "INVALID OPERATION SYNTAX"

    if(int(result) == result):
        result = int(result)
    ui.lineEdit.setText(str(result))

def updateText(input):
    if input == "," and "," in ui.lineEdit.text():
        return

    if ui.lineEdit.text() == "0" or "O" in ui.lineEdit.text():
        ui.lineEdit.setText(str(input))
    else:
        ui.lineEdit.setText(ui.lineEdit.text() + str(input))

def connectUI(uiWindow):
    uiWindow.button0.clicked.connect(lambda: updateText(0))
    uiWindow.button1.clicked.connect(lambda: updateText(1))
    uiWindow.button2.clicked.connect(lambda: updateText(2))
    uiWindow.button3.clicked.connect(lambda: updateText(3))
    uiWindow.button4.clicked.connect(lambda: updateText(4))
    uiWindow.button5.clicked.connect(lambda: updateText(5))
    uiWindow.button6.clicked.connect(lambda: updateText(6))
    uiWindow.button7.clicked.connect(lambda: updateText(7))
    uiWindow.button8.clicked.connect(lambda: updateText(8))
    uiWindow.button9.clicked.connect(lambda: updateText(9))
    uiWindow.buttonDecimal.clicked.connect(lambda: updateText("."))
    uiWindow.buttonPlus.clicked.connect(lambda: updateText("+"))
    uiWindow.buttonMinus.clicked.connect(lambda: updateText("-"))
    uiWindow.buttonMul.clicked.connect(lambda: updateText("*"))
    uiWindow.buttonDiv.clicked.connect(lambda: updateText("/"))
    uiWindow.buttonFact.clicked.connect(lambda: updateText("!"))
    uiWindow.buttonPower.clicked.connect(lambda: updateText("^"))
    uiWindow.buttonRoot.clicked.connect(lambda: updateText("√"))

def setShortcuts(uiWindow : Ui_MainWindow):
    uiWindow.button0.setShortcut("0")
    uiWindow.button1.setShortcut("1")
    uiWindow.button2.setShortcut("2")
    uiWindow.button3.setShortcut("3")
    uiWindow.button4.setShortcut("4")
    uiWindow.button5.setShortcut("5")
    uiWindow.button6.setShortcut("6")
    uiWindow.button7.setShortcut("7")
    uiWindow.button8.setShortcut("8")
    uiWindow.button9.setShortcut("9")
    uiWindow.buttonDecimal.setShortcut(",")
    uiWindow.buttonPlus.setShortcut("+")
    uiWindow.buttonMinus.setShortcut("-")
    uiWindow.buttonMul.setShortcut("*")
    uiWindow.buttonDiv.setShortcut("/")
    uiWindow.buttonEquals.setShortcut("Return")
    uiWindow.buttonEquals_2.setShortcut("Enter")
    uiWindow.buttonFact.setShortcut("!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalcWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    ui.lineEdit.setText(str("(2+5)*2"))

    connectUI(ui)
    setShortcuts(ui)

    window.show()
    sys.exit(app.exec_())