#Sangeet Kumar Mishra
#16CE10052
#KOSS Membership Task
#Made by using PySide

from PySide.QtGui import *           #Import the PySide.QtGui module
from PySide.QtCore import *          #Import the PySide.QtGui module
import sys                           #Import the sys module
import calcUI                        #import the GUI file
from math import *                   #Import the math library of python


class mainwindow(QMainWindow,calcUI.Ui_MainWindow):     #Inherit from QMainWindow class and the class of calcUI file
    result=0                     #Initialising result as a global variable so that it can be used by all the functions
    def __init__(self,parent=None):
        super(mainwindow,self).__init__(parent)  #Initialise the Parent class
        self.setupUi(self)
        # signal and slot mechanism:
        #BY DEFAULT set the standard part of calculator as the main page
        self.stackedWidget.setCurrentWidget(self.std_page)
        #if 0 is clicked send a signal which will call displayScreen function
        self.PB_0.clicked.connect(lambda: self.displayScreen('0'))
        self.PB_1.clicked.connect(lambda: self.displayScreen('1'))
        self.PB_2.clicked.connect(lambda: self.displayScreen('2'))
        self.PB_3.clicked.connect(lambda: self.displayScreen('3'))
        self.PB_4.clicked.connect(lambda: self.displayScreen('4'))
        self.PB_5.clicked.connect(lambda: self.displayScreen('5'))
        self.PB_6.clicked.connect(lambda: self.displayScreen('6'))
        self.PB_7.clicked.connect(lambda: self.displayScreen('7'))
        self.PB_8.clicked.connect(lambda: self.displayScreen('8'))
        self.PB_9.clicked.connect(lambda: self.displayScreen('9'))
        self.PB_Addition.clicked.connect(lambda: self.displayScreen('+'))
        self.PB_Division.clicked.connect(lambda: self.displayScreen('/'))
        self.PB_Multiplication.clicked.connect(lambda: self.displayScreen('*'))
        self.PB_Subtraction.clicked.connect(lambda: self.displayScreen('-'))
        self.PB_DecimalPoint.clicked.connect(lambda: self.displayScreen('.'))
        self.PB_Backspace.clicked.connect(lambda: self.LineDisplay.backspace())
        self.PB_ClearAll.clicked.connect(lambda: self.LineDisplay.clear())
        #if Equal to button is pressed evaluate
        self.PB_EqualsTo.clicked.connect(lambda: self.evaluate())
        self.PB_EqualsTo_2.clicked.connect(lambda: self.evaluate())
        self.PB_ans.clicked.connect(lambda: self.displayAns())
        #If the  std or adv button is prssed set the corresponding page
        self.StdBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.std_page))
        self.AdvBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.adv_page))
        self.btn_sin.clicked.connect(lambda: self.displayScreen('sin('))
        self.btn_open_paranthesis.clicked.connect(lambda: self.displayScreen('('))
        self.btn_close_paranthesis.clicked.connect(lambda: self.displayScreen(')'))
        self.btn_open_paranthesis_2.clicked.connect(lambda: self.displayScreen('('))
        self.btn_close_paranthesis_2.clicked.connect(lambda: self.displayScreen(')'))
        self.btn_cos.clicked.connect(lambda: self.displayScreen('cos('))
        self.btn_tan.clicked.connect(lambda: self.displayScreen('tan('))
        self.btn_arccos.clicked.connect(lambda: self.displayScreen('acos('))
        self.btn_arcsin.clicked.connect(lambda: self.displayScreen('asin('))
        self.btn_arctan.clicked.connect(lambda: self.displayScreen('atan('))
        self.btn_sinh.clicked.connect(lambda: self.displayScreen('sinh('))
        self.btn_cosh.clicked.connect(lambda: self.displayScreen('cosh('))
        self.btn_tanh.clicked.connect(lambda: self.displayScreen('tanh('))
        self.btn_arcsinh.clicked.connect(lambda: self.displayScreen('asinh('))
        self.btn_arccosh.clicked.connect(lambda: self.displayScreen('acosh('))
        self.btn_arctanh.clicked.connect(lambda: self.displayScreen('atanh('))
        #Some Constants
        self.btn_e.clicked.connect(lambda: self.displayScreen('e'))
        self.btn_h.clicked.connect(lambda: self.displayScreen('6.26E-34'))
        self.btn_c.clicked.connect(lambda: self.displayScreen('3E8'))
        self.btn_pi.clicked.connect(lambda: self.displayScreen('pi'))
        self.btn_floor.clicked.connect(lambda: self.displayScreen('floor('))
        self.btn_remainder.clicked.connect(lambda: self.displayScreen('fmod('))
        self.btn_log10.clicked.connect(lambda: self.displayScreen('log10('))
        self.btn_ln.clicked.connect(lambda: self.displayScreen('log('))
        self.btn_abs.clicked.connect(lambda: self.displayScreen('fabs('))
        self.btn_ceil.clicked.connect(lambda: self.displayScreen('ceil('))
        self.btn_exp.clicked.connect(lambda: self.displayScreen('exp('))
        self.btn_sqroot.clicked.connect(lambda: self.displayScreen('sqrt('))
        self.btn_pow.clicked.connect(lambda: self.displayScreen('**'))
        self.btn_close_paranthesis_3.clicked.connect(lambda: self.displayScreen(','))
        #Move the cursor
        self.PB_cursorBackward.clicked.connect(lambda: self.LineDisplay.cursorBackward(False,1))
        self.PB_cursorForward.clicked.connect(lambda: self.LineDisplay.cursorForward(False,1))
        #if return is pressed evaluate
        self.LineDisplay.returnPressed.connect(lambda : self.evaluate())


    def displayScreen(self, value):
        self.LineDisplay.insert(value)

    def displayAns(self):
        self.LineDisplay.insert(str(self.result))
        self.LCDDisplay.display(self.result)

    def evaluate(self):
        #Python's Exception Handling Mechanism
        try:
            expression = self.LineDisplay.text()
            self.result = eval((expression))
            self.LineDisplay.clear()
            self.LCDDisplay.display(self.result)
        except:
            self.LineDisplay.setText("%s is Invalid" %expression)



#Creating an instance of The QApplication class which manages the GUI application's control flow and main settings.
app=QApplication(sys.argv)
form=mainwindow()
form.show()
#Execute the app
app.exec_()