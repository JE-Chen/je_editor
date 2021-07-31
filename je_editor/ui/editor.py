# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.code_exec_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.code_exec_pushbutton.setObjectName("code_exec_pushbutton")
        self.horizontalLayout.addWidget(self.code_exec_pushbutton)
        self.shell_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.shell_pushbutton.setObjectName("shell_pushbutton")
        self.horizontalLayout.addWidget(self.shell_pushbutton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.code_edit_plaintext = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.code_edit_plaintext.setTabStopWidth(40)
        self.code_edit_plaintext.setObjectName("code_edit_plaintext")
        self.verticalLayout.addWidget(self.code_edit_plaintext)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.console_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.console_label.setObjectName("console_label")
        self.verticalLayout_2.addWidget(self.console_label)
        self.console_plaintext = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.console_plaintext.setReadOnly(True)
        self.console_plaintext.setTabStopWidth(40)
        self.console_plaintext.setObjectName("console_plaintext")
        self.verticalLayout_2.addWidget(self.console_plaintext)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open_file = QtWidgets.QAction(MainWindow)
        self.action_open_file.setObjectName("action_open_file")
        self.menuFile.addAction(self.action_open_file)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "je_editor"))
        self.code_exec_pushbutton.setText(_translate("MainWindow", "exec"))
        self.shell_pushbutton.setText(_translate("MainWindow", "run on shell"))
        self.console_label.setText(_translate("MainWindow", "console"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_open_file.setText(_translate("MainWindow", "Open"))
