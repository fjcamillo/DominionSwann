# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstGui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 661, 481))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox_4 = QtGui.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 130, 161, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_5 = QtGui.QComboBox(self.tab_2)
        self.comboBox_5.setGeometry(QtCore.QRect(190, 130, 221, 22))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_6 = QtGui.QComboBox(self.tab_2)
        self.comboBox_6.setGeometry(QtCore.QRect(420, 130, 171, 22))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 220, 631, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 229))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.checkBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 30, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 70, 70, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 90, 70, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_2 = QtGui.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.comboBox_7 = QtGui.QComboBox(self.tab_4)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 80, 181, 22))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_8 = QtGui.QComboBox(self.tab_4)
        self.comboBox_8.setGeometry(QtCore.QRect(240, 80, 181, 22))
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_9 = QtGui.QComboBox(self.tab_4)
        self.comboBox_9.setGeometry(QtCore.QRect(460, 80, 181, 22))
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_4)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 140, 631, 281))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 629, 279))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton = QtGui.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(470, 430, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 430, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_3)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 40, 631, 401))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.tabWidget_2.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.tabWidget_2.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.tabWidget_2.addTab(self.tab_9, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(680, 90, 111, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(678, 270, 111, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(680, 430, 111, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 661, 51))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Welcome, <insert name> !", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home", None))
        self.label_3.setText(_translate("MainWindow", "Application: Received CV", None))
        self.label_4.setText(_translate("MainWindow", "Search Database:", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Type Name", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Department", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Position", None))
        self.label_5.setText(_translate("MainWindow", "TextLabel", None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox", None))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Applications", None))
        self.label_2.setText(_translate("MainWindow", "Records:", None))
        self.label_6.setText(_translate("MainWindow", "Search Database:", None))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Keyword", None))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Department", None))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Type of Document", None))
        self.label_7.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton.setText(_translate("MainWindow", "Send", None))
        self.pushButton_2.setText(_translate("MainWindow", "delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Records", None))
        self.label_8.setText(_translate("MainWindow", "Account: Health Monitor", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Home", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Cardiovascular", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Blood Test", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "BMI", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Other", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Account", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "CV", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Interview", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Blank pa", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Blank pa", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Health Monitor", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Performance Shit", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "blank pa", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "blank pa", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "logout", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "HR", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "IT", None))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Sales", None))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "etc", None))

