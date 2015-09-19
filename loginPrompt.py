__author__ = 'Jerhone Camillo'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import login_Ui
import hr_user_ui
import clinic_user_ui
import head_user_ui
import normalemployee_user_ui
import secuirty_user_ui


name = " "
#Class for login page
class user_login(QDialog, login_Ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)




#Class for hr gui
class hr_user_interface(QMainWindow, hr_user_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

#Class for clinic gui
class clinic_user_interface(QMainWindow, clinic_user_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

#Class for Head Gui
class head_user_interface(QMainWindow, head_user_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

#Class for Normal Employee
class normalemployee_user_interface(QMainWindow, normalemployee_user_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

#Class ofr Security
class security_user_interface(QMainWindow, secuirty_user_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

app = QApplication(sys.argv)

#Prompt for login
dialog = user_login()

#Prompt for hr
hr_user = hr_user_interface()

#Prompt for clinic
clinic_user = clinic_user_interface()

#Prompt for head
head_user = head_user_interface()

#Prompot for Normal Employee
normal_user = normalemployee_user_interface()

#Prompt for Security
security_user = security_user_interface()

dialog.show()
app.exec_()