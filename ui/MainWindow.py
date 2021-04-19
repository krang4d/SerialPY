# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setWindowTitle("Serial Port Reader")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.settingsGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.settingsGBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsGBox.sizePolicy().hasHeightForWidth())
        self.settingsGBox.setSizePolicy(sizePolicy)
        self.settingsGBox.setObjectName("settingsGBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.settingsGBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serialHLayout = QtWidgets.QHBoxLayout()
        self.serialHLayout.setObjectName("serialHLayout")
        self.serialLabel = QtWidgets.QLabel(self.settingsGBox)
        self.serialLabel.setObjectName("serialLabel")
        self.serialHLayout.addWidget(self.serialLabel)
        self.serialCBox = QtWidgets.QComboBox(self.settingsGBox)
        self.serialCBox.setObjectName("serialCBox")
        self.serialHLayout.addWidget(self.serialCBox)
        self.baudrateLabel = QtWidgets.QLabel(self.settingsGBox)
        self.baudrateLabel.setObjectName("baudrateLabel")
        self.serialHLayout.addWidget(self.baudrateLabel)
        self.baudrateCBox = QtWidgets.QComboBox(self.settingsGBox)
        self.baudrateCBox.setObjectName("baudrateCBox")
        self.baudrateCBox.addItem("")
        self.baudrateCBox.addItem("")
        self.baudrateCBox.addItem("")
        self.baudrateCBox.addItem("")
        self.baudrateCBox.addItem("")
        self.serialHLayout.addWidget(self.baudrateCBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.serialHLayout.addItem(spacerItem)
        self.updateButton = QtWidgets.QPushButton(self.settingsGBox)
        self.updateButton.setObjectName("updateButton")
        self.serialHLayout.addWidget(self.updateButton)
        self.openButton = QtWidgets.QPushButton(self.settingsGBox)
        self.openButton.setObjectName("openButton")
        self.serialHLayout.addWidget(self.openButton)
        self.closeButton = QtWidgets.QPushButton(self.settingsGBox)
        self.closeButton.setObjectName("closeButton")
        self.serialHLayout.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.serialHLayout)
        self.verticalLayout_2.addWidget(self.settingsGBox)
        self.sensorsGBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensorsGBox.sizePolicy().hasHeightForWidth())
        self.sensorsGBox.setSizePolicy(sizePolicy)
        self.sensorsGBox.setTitle("")
        self.sensorsGBox.setObjectName("sensorsGBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sensorsGBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.sensorsGBox)
        self.label_4.setStyleSheet("color: rgb(196, 160, 0);")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.sensorsGBox)
        self.label_5.setStyleSheet("color: brown;")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.sensorsGBox)
        self.label_1.setStyleSheet("color: green;")
        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.sensorsGBox)
        self.label_3.setStyleSheet("color: blue;")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.sensorsGBox)
        self.label_2.setStyleSheet("color: orange;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.sensorsGBox)
        self.label_6.setStyleSheet("color: violet;")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.sensorsGBox)
        self.graphsGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.graphsGBox.setEnabled(True)
        self.graphsGBox.setTitle("")
        self.graphsGBox.setObjectName("graphsGBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.graphsGBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.graphsGBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.graphsGBox)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setStyleSheet("color: red;")
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout_2.addWidget(self.exitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.serialLabel.setBuddy(self.serialCBox)
        self.baudrateLabel.setBuddy(self.baudrateCBox)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.serialLabel.setText(_translate("MainWindow", "Serial Port"))
        self.baudrateLabel.setText(_translate("MainWindow", "BaudRate (bps)"))
        self.baudrateCBox.setItemText(0, _translate("MainWindow", "9600"))
        self.baudrateCBox.setItemText(1, _translate("MainWindow", "19200"))
        self.baudrateCBox.setItemText(2, _translate("MainWindow", "38400"))
        self.baudrateCBox.setItemText(3, _translate("MainWindow", "57600"))
        self.baudrateCBox.setItemText(4, _translate("MainWindow", "115200"))
        self.updateButton.setText(_translate("MainWindow", "update"))
        self.openButton.setText(_translate("MainWindow", "Open"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.label_4.setText(_translate("MainWindow", "Sensor 4"))
        self.label_5.setText(_translate("MainWindow", "Sensor 5"))
        self.label_1.setText(_translate("MainWindow", "Sensor 1"))
        self.label_3.setText(_translate("MainWindow", "Sensor 3"))
        self.label_2.setText(_translate("MainWindow", "Sensor 2"))
        self.label_6.setText(_translate("MainWindow", "Sensor 6"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
