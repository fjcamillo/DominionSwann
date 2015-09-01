__author__ = 'Jerhone Camillo'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import login_Ui
import homeGui_hr


name = " "
#Class for login page
class user_login(QDialog, login_Ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)




#Class for hr gui
class hr_user_interface(QMainWindow, homeGui_hr.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


app = QApplication(sys.argv)
dialog = user_login()
hr_user = hr_user_interface()
dialog.show()
app.exec_()