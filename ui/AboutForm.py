# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.setWindowModality(QtCore.Qt.ApplicationModal)
        AboutForm.resize(479, 131)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutForm.sizePolicy().hasHeightForWidth())
        AboutForm.setSizePolicy(sizePolicy)
        self.main_verticalLayout = QtWidgets.QVBoxLayout(AboutForm)
        self.main_verticalLayout.setObjectName("main_verticalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(AboutForm)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(AboutForm)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.main_verticalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(AboutForm)
        self.pushButton.clicked.connect(AboutForm.close)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "About"))
        self.label.setText(_translate("AboutForm", "The Serial Port Reader program by Pavel Golovkin (jzi@inbox.ru).\n"
"Feel free to use. No warranty.\n"
"Version 3.7.30a"))
        self.pushButton.setText(_translate("AboutForm", "Ok"))
