"""!
* Project Name : Projekt IVS                                                
* File : calc.py                                                        
* Date : 13.04.2022                                                         
* Last change : 28.04.2022                                                  
* Author : Matěj Toul (xtoulm00)                                                                                                                     
* Description : Main script to launch the calculator and connect GUI with math library                                                                                 
"""

"""!
 @file calc.py                                                         
                                                                           
 @brief App entry point                                                       
 @author Matěj Toul (xtoulm00)
"""

import sys, ast, re
from PyQt5.QtWidgets import QApplication, QMainWindow
from calcUI import Ui_MainWindow
from calcMath import *

class CalcWindow(QMainWindow):
    """!
     @brief Main calculator window that inherits from PyQt QMainWindow class.
    """
    def __init__(self):
        super().__init__()
    
    def process(self, bool):
        processOperation()

class OperationsTransformer(ast.NodeTransformer):
    """!
     @brief Operation transformer used for parsing math operations into AST (builds upon Python AST module).
    """
    ops = {
        ast.Add: 'add(',
        ast.Sub: 'sub(',
        ast.Mult: 'mul(',
        ast.Div: 'div(',
        ast.LShift: 'root(',
        ast.RShift: 'power(',
        ast.Mod: 'mod('
    }

    unops = {
        ast.Not: 'factorial('
    }

    def visit_UnaryOp(self, node):
        """!
        @brief Parser for unary operations (factorial). Not to be called manually.
        @param node Node from AST module.
        """
        self.generic_visit(node)
        if isinstance(node.operand, ast.Constant) and isinstance(node.op, ast.Not):
            value = eval(f'{self.unops[type(node.op)]} {node.operand.value})')
            return ast.Num(n=value)
        return node

    def visit_BinOp(self, node):
        """!
        @brief Parser for binary operations. Not to be called manually.
        @param node Node from AST module.
        """
        self.generic_visit(node)
        if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
            value = eval(f'{self.ops[type(node.op)]} {node.left.n}, {node.right.n})')
            return ast.Num(n=value)
        return node

def processOperation():
    """!
    @brief Function that processes the input to AST module friendly format and launches the parser.
    """
    input = ui.lineEdit.text()
    input = input.replace("^", ">>")
    input = input.replace("√", "<<")

    if "!" in input:
        factInput = input.split("!")
        firstHalf = re.split("([^0-9])", factInput[0])
        newInput = firstHalf[-1]
        firstHalf.pop()
        input = ''.join(firstHalf) + "(not " + newInput + ")" + factInput[1]
    try:
        tree = ast.parse("result = " + input)
        ast.fix_missing_locations(OperationsTransformer().visit(tree))

        ldict = {}
        exec(compile(tree, filename="", mode="exec"), globals(), ldict)
        result = ldict['result']

        if(int(result) == result):
            result = int(result)

    except SyntaxError:
        result = "INVALID OPERATION SYNTAX"
    except ValueError:
        result = "NEGATIVE ROOT"
    except:
        result = "UNKNOWN ERROR"
    ui.lineEdit.setText(str(result))

def updateText(input):
    """!
    @brief Updates the text field based on input (key/button presses).
    @param input The inputed number or math function identificator.
    """
    if input == "":
        newText = ui.lineEdit.text()[:-1]
        ui.lineEdit.setText(newText)
        return

    if input == "," and "," in ui.lineEdit.text():
        return

    if ui.lineEdit.text() == "0" or "O" in ui.lineEdit.text():
        ui.lineEdit.setText(str(input))
    else:
        ui.lineEdit.setText(ui.lineEdit.text() + str(input))

def connectUI(uiWindow : Ui_MainWindow):
    """!
    @brief Connects GUI elements with the text field and ulimately the math library.
    @param uiWindow The calculator's main window instance.
    """
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
    uiWindow.buttonMod.clicked.connect(lambda: updateText("%"))
    uiWindow.buttonLPar.clicked.connect(lambda: updateText("("))
    uiWindow.buttonRPar.clicked.connect(lambda: updateText(")"))
    uiWindow.buttonBackspace.clicked.connect(lambda: updateText(""))

def setShortcuts(uiWindow : Ui_MainWindow):
    """!
    @brief Sets up all of the keyboard shortcuts.
    @param uiWindow The calculator's main window instance.
    """
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
    uiWindow.buttonMod.setShortcut("%")
    uiWindow.buttonLPar.setShortcut("(")
    uiWindow.buttonRPar.setShortcut(")")
    uiWindow.buttonBackspace.setShortcut("Backspace")

if __name__ == '__main__':
    """!
    @brief The application's entry point.
    """
    app = QApplication(sys.argv)
    window = CalcWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    connectUI(ui)
    setShortcuts(ui)

    ui.textBrowser.hide()
    ui.buttonBox.hide()

    window.show()
    sys.exit(app.exec_())