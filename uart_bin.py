#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Serial Port Reader by Pavel Golovkin, aka pgg.
# Feel free to use. No warranty
# Version 3.6.25a

import sys  # We need sys so that we can pass argv to QApplication
import os
from datetime import datetime
# import numpy as np
import serial
import serial.tools.list_ports as prtlst
# import serial.tools.list_ports
import libscrc
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import time
import json

# from ui.binwindow import Ui_MainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1113, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_settings.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_settings.sizePolicy().hasHeightForWidth())
        self.groupBox_settings.setSizePolicy(sizePolicy)
        self.groupBox_settings.setObjectName("groupBox_settings")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_settings)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.portLabel = QtWidgets.QLabel(self.groupBox_settings)
        self.portLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.portLabel.setObjectName("portLabel")
        self.verticalLayout_3.addWidget(self.portLabel)
        self.portCBox = QtWidgets.QComboBox(self.groupBox_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portCBox.sizePolicy().hasHeightForWidth())
        self.portCBox.setSizePolicy(sizePolicy)
        self.portCBox.setMinimumSize(QtCore.QSize(140, 0))
        self.portCBox.setObjectName("portCBox")
        self.verticalLayout_3.addWidget(self.portCBox)
        self.speedLabel = QtWidgets.QLabel(self.groupBox_settings)
        self.speedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speedLabel.setObjectName("speedLabel")
        self.verticalLayout_3.addWidget(self.speedLabel)
        self.speedCBox = QtWidgets.QComboBox(self.groupBox_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speedCBox.sizePolicy().hasHeightForWidth())
        self.speedCBox.setSizePolicy(sizePolicy)
        self.speedCBox.setObjectName("speedCBox")
        self.speedCBox.addItem("")
        self.speedCBox.addItem("")
        self.speedCBox.addItem("")
        self.speedCBox.addItem("")
        self.speedCBox.addItem("")
        self.verticalLayout_3.addWidget(self.speedCBox)
        self.refButton = QtWidgets.QPushButton(self.groupBox_settings)
        self.refButton.setObjectName("refButton")
        self.verticalLayout_3.addWidget(self.refButton)
        self.openButton = QtWidgets.QPushButton(self.groupBox_settings)
        self.openButton.setObjectName("openButton")
        self.verticalLayout_3.addWidget(self.openButton)
        self.closeButton = QtWidgets.QPushButton(self.groupBox_settings)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_3.addWidget(self.closeButton)
        self.gridLayout.addWidget(self.groupBox_settings, 0, 0, 1, 1)
        self.groupBox_photo = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_photo.sizePolicy().hasHeightForWidth())
        self.groupBox_photo.setSizePolicy(sizePolicy)
        self.groupBox_photo.setObjectName("groupBox_photo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_photo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_photo_indicator = QtWidgets.QFormLayout()
        self.formLayout_photo_indicator.setObjectName("formLayout_photo_indicator")
        self.photoLineEdit_0 = QtWidgets.QLineEdit(self.groupBox_photo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoLineEdit_0.sizePolicy().hasHeightForWidth())
        self.photoLineEdit_0.setSizePolicy(sizePolicy)
        self.photoLineEdit_0.setObjectName("photoLineEdit_0")
        self.formLayout_photo_indicator.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.photoLineEdit_0)
        self.photoLineEdit_1 = QtWidgets.QLineEdit(self.groupBox_photo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoLineEdit_1.sizePolicy().hasHeightForWidth())
        self.photoLineEdit_1.setSizePolicy(sizePolicy)
        self.photoLineEdit_1.setText("")
        self.photoLineEdit_1.setReadOnly(True)
        self.photoLineEdit_1.setObjectName("photoLineEdit_1")
        self.formLayout_photo_indicator.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.photoLineEdit_1)
        self.label_temp = QtWidgets.QLabel(self.groupBox_photo)
        self.label_temp.setObjectName("label_temp")
        self.formLayout_photo_indicator.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_temp)
        self.label_ADC = QtWidgets.QLabel(self.groupBox_photo)
        self.label_ADC.setObjectName("label_ADC")
        self.formLayout_photo_indicator.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_ADC)
        self.verticalLayout_2.addLayout(self.formLayout_photo_indicator)
        self.label_cmd = QtWidgets.QLabel(self.groupBox_photo)
        self.label_cmd.setObjectName("label_cmd")
        self.verticalLayout_2.addWidget(self.label_cmd)
        self.photoLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_photo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoLineEdit_2.sizePolicy().hasHeightForWidth())
        self.photoLineEdit_2.setSizePolicy(sizePolicy)
        self.photoLineEdit_2.setReadOnly(True)
        self.photoLineEdit_2.setObjectName("photoLineEdit_2")
        self.verticalLayout_2.addWidget(self.photoLineEdit_2)
        self.formLayout_photo_calibr = QtWidgets.QFormLayout()
        self.formLayout_photo_calibr.setObjectName("formLayout_photo_calibr")
        self.label_N2 = QtWidgets.QLabel(self.groupBox_photo)
        self.label_N2.setObjectName("label_N2")
        self.formLayout_photo_calibr.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_N2)
        self.label_T1 = QtWidgets.QLabel(self.groupBox_photo)
        self.label_T1.setObjectName("label_T1")
        self.formLayout_photo_calibr.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_T1)
        self.label_T2 = QtWidgets.QLabel(self.groupBox_photo)
        self.label_T2.setObjectName("label_T2")
        self.formLayout_photo_calibr.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_T2)
        self.label_N1 = QtWidgets.QLabel(self.groupBox_photo)
        self.label_N1.setObjectName("label_N1")
        self.formLayout_photo_calibr.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_N1)
        self.label_calibr = QtWidgets.QLabel(self.groupBox_photo)
        self.label_calibr.setObjectName("label_calibr")
        self.formLayout_photo_calibr.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_calibr)
        self.spinBox_N1 = BigIntSpinbox(self.groupBox_photo)
        # self.spinBox_N1.setMaximum(999999999)
        self.spinBox_N1.setObjectName("spinBox_N1")
        self.formLayout_photo_calibr.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_N1)
        self.spinBox_N2 = BigIntSpinbox(self.groupBox_photo)
        # self.spinBox_N2.setMaximum(999999999)
        self.spinBox_N2.setObjectName("spinBox_N2")
        self.formLayout_photo_calibr.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_N2)
        self.spinBox_T1 = QtWidgets.QSpinBox(self.groupBox_photo)
        self.spinBox_T1.setMinimum(-999999999)
        self.spinBox_T1.setMaximum(999999999)
        self.spinBox_T1.setObjectName("spinBox_T1")
        self.formLayout_photo_calibr.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_T1)
        self.spinBox_T2 = QtWidgets.QSpinBox(self.groupBox_photo)
        self.spinBox_T2.setMinimum(-999999999)
        self.spinBox_T2.setMaximum(999999999)
        self.spinBox_T2.setObjectName("spinBox_T2")
        self.formLayout_photo_calibr.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_T2)
        self.verticalLayout_2.addLayout(self.formLayout_photo_calibr)
        self.gridLayout.addWidget(self.groupBox_photo, 5, 0, 1, 1)
        self.groupBox_messenger = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_messenger.sizePolicy().hasHeightForWidth())
        self.groupBox_messenger.setSizePolicy(sizePolicy)
        self.groupBox_messenger.setObjectName("groupBox_messenger")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_messenger)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_messenger)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout.addWidget(self.groupBox_messenger, 6, 1, 3, 1)
        self.groupBox_data_vibro = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_data_vibro.sizePolicy().hasHeightForWidth())
        self.groupBox_data_vibro.setSizePolicy(sizePolicy)
        self.groupBox_data_vibro.setObjectName("groupBox_data_vibro")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_data_vibro)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.NVButton = QtWidgets.QPushButton(self.groupBox_data_vibro)
        self.NVButton.setObjectName("NVButton")
        self.gridLayout_2.addWidget(self.NVButton, 2, 1, 1, 2)
        self.label_NV = QtWidgets.QLabel(self.groupBox_data_vibro)
        self.label_NV.setObjectName("label_NV")
        self.gridLayout_2.addWidget(self.label_NV, 0, 1, 1, 1)
        self.spinBox_NV = QtWidgets.QSpinBox(self.groupBox_data_vibro)
        self.spinBox_NV.setMaximum(15)
        self.spinBox_NV.setObjectName("spinBox_NV")
        self.gridLayout_2.addWidget(self.spinBox_NV, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_data_vibro, 2, 0, 1, 1)
        self.groupBox_taxo = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_taxo.sizePolicy().hasHeightForWidth())
        self.groupBox_taxo.setSizePolicy(sizePolicy)
        self.groupBox_taxo.setObjectName("groupBox_taxo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_taxo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_taxo = QtWidgets.QFormLayout()
        self.formLayout_taxo.setObjectName("formLayout_taxo")
        self.taxoLineEdit_0 = QtWidgets.QLineEdit(self.groupBox_taxo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxoLineEdit_0.sizePolicy().hasHeightForWidth())
        self.taxoLineEdit_0.setSizePolicy(sizePolicy)
        self.taxoLineEdit_0.setObjectName("taxoLineEdit_0")
        self.formLayout_taxo.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.taxoLineEdit_0)
        self.taxoLineEdit_1 = QtWidgets.QLineEdit(self.groupBox_taxo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxoLineEdit_1.sizePolicy().hasHeightForWidth())
        self.taxoLineEdit_1.setSizePolicy(sizePolicy)
        self.taxoLineEdit_1.setText("")
        self.taxoLineEdit_1.setObjectName("taxoLineEdit_1")
        self.formLayout_taxo.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.taxoLineEdit_1)
        self.label_1 = QtWidgets.QLabel(self.groupBox_taxo)
        self.label_1.setObjectName("label_1")
        self.formLayout_taxo.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_taxo)
        self.label_2.setObjectName("label_2")
        self.formLayout_taxo.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.verticalLayout_4.addLayout(self.formLayout_taxo)
        self.label_3 = QtWidgets.QLabel(self.groupBox_taxo)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.taxoLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_taxo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxoLineEdit_2.sizePolicy().hasHeightForWidth())
        self.taxoLineEdit_2.setSizePolicy(sizePolicy)
        self.taxoLineEdit_2.setReadOnly(True)
        self.taxoLineEdit_2.setObjectName("taxoLineEdit_2")
        self.verticalLayout_4.addWidget(self.taxoLineEdit_2)
        self.gridLayout.addWidget(self.groupBox_taxo, 6, 0, 1, 1)
        self.groupBox_graphs = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_graphs.setObjectName("groupBox_graphs")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_graphs)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.groupBox_graphs)
        self.widget.setObjectName("widget")
        self.verticalLayout_5.addWidget(self.widget)
        self.gridLayout.addWidget(self.groupBox_graphs, 0, 1, 6, 1)
        self.verticalLayout_main_buttons = QtWidgets.QVBoxLayout()
        self.verticalLayout_main_buttons.setObjectName("verticalLayout_main_buttons")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_main_buttons.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_main_buttons.addWidget(self.stopButton)
        self.cleanButton = QtWidgets.QPushButton(self.centralwidget)
        self.cleanButton.setObjectName("cleanButton")
        self.verticalLayout_main_buttons.addWidget(self.cleanButton)
        self.gridLayout.addLayout(self.verticalLayout_main_buttons, 7, 0, 1, 1)
        self.groupBox_setfreq_motor = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_setfreq_motor.sizePolicy().hasHeightForWidth())
        self.groupBox_setfreq_motor.setSizePolicy(sizePolicy)
        self.groupBox_setfreq_motor.setObjectName("groupBox_setfreq_motor")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_setfreq_motor)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox_freq_motor = QtWidgets.QSpinBox(self.groupBox_setfreq_motor)
        self.spinBox_freq_motor.setObjectName("spinBox_freq_motor")
        self.horizontalLayout.addWidget(self.spinBox_freq_motor)
        self.pushButton_setfreq_motor = QtWidgets.QPushButton(self.groupBox_setfreq_motor)
        self.pushButton_setfreq_motor.setObjectName("pushButton_setfreq_motor")
        self.horizontalLayout.addWidget(self.pushButton_setfreq_motor)
        self.gridLayout.addWidget(self.groupBox_setfreq_motor, 3, 0, 1, 1)
        self.groupBox_vibro_status = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_vibro_status.setObjectName("groupBox_vibro_status")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_vibro_status)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_vibro_status = QtWidgets.QLabel(self.groupBox_vibro_status)
        self.label_vibro_status.setObjectName("label_vibro_status")
        self.horizontalLayout_2.addWidget(self.label_vibro_status)
        self.pushButton_vibro_status = QtWidgets.QPushButton(self.groupBox_vibro_status)
        self.pushButton_vibro_status.setObjectName("pushButton_vibro_status")
        self.horizontalLayout_2.addWidget(self.pushButton_vibro_status)
        self.gridLayout.addWidget(self.groupBox_vibro_status, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.groupBox_getfreqmoto = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_getfreqmoto.sizePolicy().hasHeightForWidth())
        self.groupBox_getfreqmoto.setSizePolicy(sizePolicy)
        self.groupBox_getfreqmoto.setObjectName("groupBox_getfreqmoto")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_getfreqmoto)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_getfreqmoto = QtWidgets.QLineEdit(self.groupBox_getfreqmoto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_getfreqmoto.sizePolicy().hasHeightForWidth())
        self.lineEdit_getfreqmoto.setSizePolicy(sizePolicy)
        self.lineEdit_getfreqmoto.setObjectName("lineEdit_getfreqmoto")
        self.horizontalLayout_3.addWidget(self.lineEdit_getfreqmoto)
        self.pushButton_getfreqmoto = QtWidgets.QPushButton(self.groupBox_getfreqmoto)
        self.pushButton_getfreqmoto.setObjectName("pushButton_getfreqmoto")
        self.horizontalLayout_3.addWidget(self.pushButton_getfreqmoto)
        self.gridLayout.addWidget(self.groupBox_getfreqmoto, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.portLabel.setBuddy(self.portCBox)
        self.speedLabel.setBuddy(self.speedCBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Физприбор 3.7.25а"))
        self.groupBox_settings.setTitle(_translate("MainWindow", "Настройка соединения"))
        self.portLabel.setText(_translate("MainWindow", "Номер порта:"))
        self.speedLabel.setText(_translate("MainWindow", "Скорость соединения:"))
        self.speedCBox.setItemText(0, _translate("MainWindow", "9600"))
        self.speedCBox.setItemText(1, _translate("MainWindow", "19200"))
        self.speedCBox.setItemText(2, _translate("MainWindow", "38400"))
        self.speedCBox.setItemText(3, _translate("MainWindow", "57600"))
        self.speedCBox.setItemText(4, _translate("MainWindow", "115200"))
        self.refButton.setText(_translate("MainWindow", "Обновить"))
        self.openButton.setText(_translate("MainWindow", "Открыть"))
        self.closeButton.setText(_translate("MainWindow", "Закрыть"))
        self.groupBox_photo.setTitle(_translate("MainWindow", "Опрос фотоприёмника"))
        self.label_temp.setText(_translate("MainWindow", "Температура °C:"))
        self.label_ADC.setText(_translate("MainWindow", "ADC:"))
        self.label_cmd.setText(_translate("MainWindow", "Команда:"))
        self.photoLineEdit_2.setText(_translate("MainWindow", "200300010001"))
        self.label_N2.setText(_translate("MainWindow", "N2"))
        self.label_T1.setText(_translate("MainWindow", "T1"))
        self.label_T2.setText(_translate("MainWindow", "T2"))
        self.label_N1.setText(_translate("MainWindow", "N1"))
        self.label_calibr.setText(_translate("MainWindow", "Параметры калибровки:"))
        self.groupBox_messenger.setTitle(_translate("MainWindow", "Ответ:"))
        self.groupBox_data_vibro.setTitle(_translate("MainWindow", "Запрос данных с АЦП виброметра"))
        self.NVButton.setText(_translate("MainWindow", "Запросить"))
        self.label_NV.setText(_translate("MainWindow", "Номер фотоприёмника:"))
        self.groupBox_taxo.setTitle(_translate("MainWindow", "Опрос тахометра"))
        self.label_1.setText(_translate("MainWindow", "Скорость  (oб/мин):"))
        self.label_2.setText(_translate("MainWindow", "ADC:"))
        self.label_3.setText(_translate("MainWindow", "Команда:"))
        self.taxoLineEdit_2.setText(_translate("MainWindow", "100300010001"))
        self.groupBox_graphs.setTitle(_translate("MainWindow", "Графики"))
        self.startButton.setText(_translate("MainWindow", "Старт"))
        self.stopButton.setText(_translate("MainWindow", "Стоп"))
        self.cleanButton.setText(_translate("MainWindow", "Очистить"))
        self.groupBox_setfreq_motor.setTitle(_translate("MainWindow", "Установка частоты вращения вала двигателя"))
        self.pushButton_setfreq_motor.setText(_translate("MainWindow", "Задать"))
        self.groupBox_vibro_status.setTitle(_translate("MainWindow", "Запрос состояния платы фотоприёмника виброметра"))
        self.label_vibro_status.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_vibro_status.setText(_translate("MainWindow", "Запросить"))
        self.groupBox_getfreqmoto.setTitle(_translate("MainWindow", "Запрос периода вращения вала двигателя:"))
        self.pushButton_getfreqmoto.setText(_translate("MainWindow", "Запросить"))

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class BigIntSpinbox(QtWidgets.QAbstractSpinBox):

    def __init__(self, parent=None):
        super(BigIntSpinbox, self).__init__(parent)

        self._singleStep = 1
        self._minimum = 0 #-18446744073709551616
        self._maximum = 4294967295 #18446744073709551615

        self.lineEdit = QtWidgets.QLineEdit(self)

        rx = QtCore.QRegExp("[0-9]\\d{1,9}")
        validator = QtGui.QRegExpValidator(rx, self)

        self.lineEdit.setValidator(validator)
        self.setLineEdit(self.lineEdit)

    def value(self):
        try:
            return int(self.lineEdit.text())
        except:
            raise
            return 0

    def setValue(self, value):
        if self._valueInRange(value):
            self.lineEdit.setText(str(value))

    def stepBy(self, steps):
        self.setValue(self.value() + steps*self.singleStep())

    def stepEnabled(self):
        return self.StepUpEnabled | self.StepDownEnabled

    def setSingleStep(self, singleStep):
        assert isinstance(singleStep, int)
        # don't use negative values
        self._singleStep = abs(singleStep)

    def singleStep(self):
        return self._singleStep

    def minimum(self):
        return self._minimum

    def setMinimum(self, minimum):
        assert isinstance(minimum, int) or isinstance(minimum, long)
        self._minimum = minimum

    def maximum(self):
        return self._maximum

    def setMaximum(self, maximum):
        assert isinstance(maximum, int) or isinstance(maximum, long)
        self._maximum = maximum

    def _valueInRange(self, value):
        if value >= self.minimum() and value <= self.maximum():
            return True
        else:
            return False

class Inits:
    def __init__(self):
        self._settings_box = {
            "calibration" : {
                "N1": 0,
                "N2": 1,
                "T1": 0,
                "T2": 0
            }
        }
        if os.path.isfile("settings.json"):
            with open("settings.json", "r") as read_file:
                data = json.load(read_file)
            self.calibration = data.get("calibration")
        else:
            with open("settings.json", "w") as write_file:
                json.dump(self._settings_box, write_file)
            self.calibration = self._settings_box['calibration']

    def __del__(self):
        print('save_settings')
        self._settings_box['calibration'] = self.calibration
        with open("settings.json", "w") as write_file:
            json.dump(self._settings_box, write_file)


    def print_debug(self):
        print(self.calibration)
        self._settings_box['calibration'] = self.calibration
        if self.calibration is self._settings_box.get("calibration"):
            print("is equal")
        else:
            print(id(self.calibration), self.calibration)
            print(id(self._settings_box.get("calibration")), self._settings_box.get("calibration"))

    def get_N1(self):
        return self.calibration.get('N1', 0)

    def set_N1(self, value):
        self.calibration['N1'] = value

    def get_N2(self):
        return self.calibration.get('N2', 1)

    def set_N2(self, value):
        self.calibration['N2'] = value

    def get_T1(self):
        return self.calibration.get('T1', 0)

    def set_T1(self, value):
        self.calibration['T1'] = value

    def get_T2(self):
        return self.calibration.get('T2', 0)

    def set_T2(self, value):
        self.calibration['T2'] = value

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ''' Основное окно программы    '''
    _num = 100

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Install the custom output stream
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

        # self.timer1 = QtCore.QTimer()
        self.plots_timer = QtCore.QTimer()

        self.textEdit.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.cleanButton.clicked.connect( lambda : { self.clean() })

        self._index1 = iter(NumbersIterator())
        self._index2 = iter(NumbersIterator())
        # self._index3 = iter(NumbersIterator())

        self.flag_update_ph = True
        self.flag_update_taxo = True

        self._y1 = list()
        self._y2 = list()
        # self._y3 = list()
        self._x1  = list()
        self._x2  = list()
        # self._x3  = list()

        self.graphWidget1 = pg.PlotWidget()
        self.graphWidget2 = pg.PlotWidget()

        self.graphWidget1.setBackground((100,50,255,0))
        self.graphWidget2.setBackground((100,50,255,0))

        styles = {'color':'b', 'font-size':'14px'}
        self.graphWidget1.setLabel('left', 'RPM', **styles)
        self.graphWidget2.setLabel('left', 'T (°C)', **styles)

        # Create a QHBoxLayout instance
        graphsLayout = QtWidgets.QVBoxLayout()
        graphsLayout.addWidget(self.graphWidget1)
        graphsLayout.addWidget(self.graphWidget2)

        self.widget.setLayout(graphsLayout)

        #Add legend
        self.graphWidget1.addLegend()
        self.graphWidget2.addLegend()

        #Add grid
        self.graphWidget1.showGrid(x=True, y=True)
        self.graphWidget2.showGrid(x=True, y=True)

        #Set Range
        # self.graphWidget1.setXRange(0, 10, padding=0)
        # self.graphWidget2.setXRange(0, 10, padding=0)
        # self.graphWidget1.setYRange(20, 55, padding=0)
        # self.graphWidget2.setYRange(20, 55, padding=0)

        #Plot data: x, y values
        pen = pg.mkPen(color=(0, 180, 0), width=2, style=QtCore.Qt.SolidLine)
        self._line1 = self.graphWidget1.plot(self._x1, self._y1, name='RPM', symbolBrush=(0, 180, 0), symbolSize=6, pen=pen)
        pen = pg.mkPen(color='b', width=2, style=QtCore.Qt.SolidLine)
        self._line2 = self.graphWidget2.plot(self._x2, self._y2, name='T(°C)', symbolBrush='b', symbolSize=6, pen=pen)
        # pen = pg.mkPen(color=(196, 160, 0), width=2, style=QtCore.Qt.SolidLine)
        # self._line3 = self.graphWidget2.plot(self._x3, self._y3, name='ADC', symbolBrush=(196, 160, 0), symbolSize=6, pen=pen)

        self.init = Inits()
        # self.init.print_debug()
        self.spinBox_N1.setValue(self.init.get_N1())
        self.spinBox_N2.setValue(self.init.get_N2())
        self.spinBox_T1.setValue(self.init.get_T1())
        self.spinBox_T2.setValue(self.init.get_T2())

        self.start_flag = False

    def setup_window(self, device):
        # self.timer1.timeout.connect( lambda: {
        #     device.writebincode(self.get_bytes()),
        #     self.show_res(device.readbincode())
        #     })
        self.device = device
        self.startButton.clicked.connect(self.start_slot)
        self.stopButton.clicked.connect(self.stop_slot)

        self.plots_timer.timeout.connect( lambda: {
            device.writebincode(self.get_ph()),
            self.show_ph(device.readbincode()),
            time.sleep(0.02),
            device.writebincode(self.get_taxo()),
            self.show_taxo(device.readbincode())
        })

        self.openButton.clicked.connect( lambda : {
            self.statusbar.showMessage("Open("+self.portCBox.currentText()+")", 1000),
            device.open(self.portCBox.currentText(), int(self.speedCBox.currentText()), 0.1)
            })

        self.closeButton.clicked.connect( lambda :{
            self.statusbar.showMessage("Close()"),
            device.close()
            })

        self.refButton.clicked.connect( lambda : {
            self.statusbar.showMessage("Refresh()"),
            self.set_devs(UDevice.get_devs())
            })

        self.NVButton.clicked.connect(self.vibromotor_slot)
        self.pushButton_vibro_status.clicked.connect(self.vibrostatus_slot)
        self.pushButton_getfreqmoto.clicked.connect(self.getfreqmotor_slot)
        self.pushButton_setfreq_motor.clicked.connect(self.setfreqmotor_slot)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    def start_slot(self):
        self.plots_timer.start(100)
        self.start_flag = True

    def stop_slot(self):
        self.plots_timer.stop()
        self.device.flush()
        self.start_flag = False

    def vibromotor_slot(self):
        """
        Запрос данных с АЦП виброметра: 3X 03 00 02 00 01 CS CS
        Ответ на запрос: 3X 03 01 BN ... B1 CS CS, где
        BN … B1 массив 16 разрядных отсчётов АЦП виброметра (N = 1024)
        """
        self.statusbar.showMessage("Req_V()")
        self.plots_timer.stop()
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file', '.',"Text files (*.txt)")
        if fname[0] == '':
            return 0
        print(fname, os.path.isfile(fname[0]))
        # TODO set true command
        x = self.spinBox_NV.value();
        code = b'\x30\x03\x00\x02\x00\x01' # 3X 03 00 02 00 01
        code_l = list(code)
        code_l[0] = code_l[0] + x
        code = bytes(code_l)
        device.writebincode(code)
        time.sleep(1)
        if(self.start_flag):
            self.stop_slot()
            data = device.readbincode(1029)
            self.device.flush()
            self.start_slot()
        else:
            data = device.readbincode(1029)

        # data_invert = list(chunks(data[3:-2], 2))[::-1]
        data_invert = [int.from_bytes(b, byteorder='big') for b in chunks(data[3:-2], 2)][::-1]
        print(data_invert)
        with open(fname[0], 'w') as f:
            for b in data_invert: f.write(str(b)+'\n')

    def vibrostatus_slot(self):
        """
        запрос состояния платы фотоприёмника виброметра: 3X 04 00 00 00 01 CS CS
        Ответ на запрос: 3X 04 01 NN CS CS, где
        NN- состояние платы: 00- исправна, 01- неисправна
        """
        self.statusbar.showMessage("vibrostatus_slot()")
        self.plots_timer.stop()
        if(True):
            self.label_vibro_status.setText("Исправна")
        else:
            self.label_vibro_status.setText("Неисправна")

    def setfreqmotor_slot(self):
        """
        Задать частоту вращения вала двигателя: 3X 06 00 01 HH LL CS CS,
        где HH LL – целое 16-битное число, соответствующее частоте вращения вала двигателя, об/мин
        """
        self.statusbar.showMessage("setfreqmotor_slot()")
        self.plots_timer.stop()
        pass

    def getfreqmotor_slot(self):
        """
        запрос регистра данных периода вращения вала двигателя: 3X 03 00 01 00 01 CS CS,
        где Х- номер фотоприёмника виброметра (указывается или перемычками на плате, или программируется на объекте). По умолчанию 0
        Итоговая команда по-умолчанию: 30 03 00 01 00 01 D1 EB
        """
        self.statusbar.showMessage("getfreqmotor_slot()")
        self.plots_timer.stop()
        pass

    def normalOutputWritten(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def closeEvent(self, event):
        self.init.set_N1(self.spinBox_N1.value())
        self.init.set_N2(self.spinBox_N2.value())
        self.init.set_T1(self.spinBox_T1.value())
        self.init.set_T2(self.spinBox_T2.value())
        del self.init
        # event.accept()

    def set_devs(self, devs):
        self.portCBox.clear()
        for d in devs:
            self.portCBox.addItem(d)

    @staticmethod
    def set_num(i: int):
        MainWindow._num = i

    # def get_bytes(self):
    #     cmd = self.cmdLineEdit.text()
    #     try:
    #         bl = bytes.fromhex(cmd)
    #         print('get_bytes():', bl.hex())
    #     except Exception as e:
    #         self.statusbar.showMessage(str(e), 3000)
    #     return bl

    # def show_res(self, data : bytes):
    #     now = datetime.now() # current date and time
    #     self.statusbar.showMessage(data.hex(), 1000)
    #     self.textEdit.insertPlainText("res:"+data.hex() +" "+now.strftime("%H:%M:%S %f")+'\n')
    #     sb = self.textEdit.verticalScrollBar()
    #     sb.setValue(sb.maximum())
    #     # print('show_res(): ', data.hex())

    def get_ph(self):
        cmd = self.photoLineEdit_2.text()
        try:
            bl = bytes.fromhex(cmd)
            # print('get_ph():', bl)
        except Exception as e:
            self.statusbar.showMessage(str(e), 3000)
        return bl

    def get_taxo(self):
        cmd = self.taxoLineEdit_2.text()
        try:
            bl = bytes.fromhex(cmd)
            # print('get_taxo():', bl)
        except Exception as e:
            self.statusbar.showMessage(str(e), 3000)
        return bl

    def _update_ph(self, data):
        '''Функция добавления новой точки на график фотоприемника'''
        if len(self._x2) >= self._num:
            cut = len(self._x2) - self._num + 1
            self._x2 = self._x2[cut:]     # Remove the first
            self._y2 = self._y2[cut:]     # Remove the first

        self._x2.append(next(self._index2)) #self._x[-1] + 1)   # Add a new value 1 higher than the last.
        self._y2.append(data) # Add a new value.
        self._line2.setData(self._x2, self._y2)  # Update the data.

        axY = self.graphWidget2.getAxis('left')

        if data > axY.range[1] or data < axY.range[0] or self.flag_update_ph:
            # avg = sum(self._y2) / len(self._y2)
            ymin = min(self._y2)
            ymax = max(self._y2)
            self.graphWidget2.setRange(yRange=[ymax+0.25, ymin-0.25])
            self.flag_update_ph = False;

    def show_ph(self, data : bytes):
        """Функция обновления всех значейний фотоприемника"""
        N = int.from_bytes(data[3:7], byteorder='little', signed=False)
        str_code = str(N)
        # print("show_ph():", str_code, data[3:7].hex())
        self.photoLineEdit_1.setText(str_code)

        N1 = self.spinBox_N1.value()
        N2 = self.spinBox_N2.value()
        T1 = self.spinBox_T1.value()
        T2 = self.spinBox_T2.value()
        try: 
            T = (N-N1)*(T2-T1)/(N2-N1)+T1
            self.photoLineEdit_0.setText( "%.1f" % (T) )
            self._update_ph(T)
        except ZeroDivisionError:
            self.photoLineEdit_0.setText( "-" )
            self.statusbar.showMessage("ZeroDivisionError", 3000)

        # self.textEdit.insertPlainText(str(data)+" "+now.strftime("%H:%M:%S %f")+'\n');

    def _update_taxo(self, data):
        """Функция добавления новой точки на график скрости тахометра"""
        if len(self._x1) >= self._num:
            cut = len(self._x1) - self._num + 1
            self._x1 = self._x1[cut:]     # Remove the first
            self._y1 = self._y1[cut:]     # Remove the first

        self._x1.append(next(self._index1)) #self._x[-1] + 1)   # Add a new value 1 higher than the last.
        self._y1.append(data) # Add a new value.
        self._line1.setData(self._x1, self._y1)  # Update the data.

        axY = self.graphWidget1.getAxis('left')
        # print("axis bottom", axX.range, "axis left", axY.range[0], axY.range[1])
        if data > axY.range[1] or data < axY.range[0] or self.flag_update_taxo:
            avg = sum(self._y1) / len(self._y1)
            ymin = min(self._y1)
            ymax = max(self._y1)
            limit = 0.005 * avg
            self.graphWidget1.setRange(yRange=[ ymax+limit, ymin-limit])
            self.flag_update_taxo = False

    def show_taxo(self, data : bytes):
        """Функция обновления всех значейний тахометра"""
        t = int.from_bytes(data[3:7], byteorder='little', signed=False)
        msg1 = str(t)
        # print("show_taxo():", msg1, data[3:7].hex())
        self.taxoLineEdit_1.setText(msg1)
        if (t == 0):
            self.taxoLineEdit_0.setText("-")
        else:
            y = 60000000/t
            msg0 = "%.1f" % (60000000/t)
            self.taxoLineEdit_0.setText(msg0)
            self._update_taxo(y)

    def clean(self):
        self.textEdit.clear()
        self._x1.clear()
        self._x2.clear()
        self._y1.clear()
        self._y2.clear()
        self._index1.reset()
        self._index2.reset()
        self._line1.setData(self._x1, self._y1)
        self._line2.setData(self._x2, self._y2)

class FixedSerial( serial.Serial ):
    """To fix bug on Windows 10 system
        https://github.com/pyserial/pyserial/issues/258
        https://github.com/pyserial/pyserial/issues/362
    """
    def _reconfigure_port( self, *args, **kwargs ):
        try:
            super()._reconfigure_port( *args, **kwargs )
        except serial.SerialException:
            pass

class NumbersIterator:
    def __iter__(self):
        self.a = 1
        return self

    def reset(self):
        self.a = 1

    def __next__(self):
        x = self.a
        self.a += 1
        return x

def _FileLogger(func):
    '''Wrapper (decorator) for log incomming data from device'''
    _file_name = "uart.log" # имя лог файла
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        with open(_file_name, 'a') as f:
            f.write('%s;%s\n'%(datetime.now(), ';'.join(map(str,data))))
        return data
    return wrapper

class UDevice(QtWidgets.QWidget):
    _dev = None
    _port = None
    # newData = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.close()

    def open(self, dev: str, baudrate: int, timeout: int):
        try:
            #if UDevice._dev is None:
            UDevice._port = FixedSerial(port=dev, baudrate=baudrate, timeout=timeout)
            print('Open Port '+ dev)
            self.timeout = timeout
            UDevice._dev = dev
            #else: print('The Port '+ dev + ' has been open')
        except serial.serialutil.SerialException as e:
            print("PortNotFoundError")
            # self.newData.emit(['error', str(e)])

    def close(self):
        if UDevice._dev is not None:
            print('Closed Port '+ UDevice._dev)
            UDevice._dev = None
            UDevice._port.close()

    @staticmethod
    def get_devs():
        devices = list()
        pts= prtlst.comports()
        for index, pt in enumerate(pts):
            #print(pt)
            if 'USB' or 'ACM'  in pt[1]:
                devices.append(pt[0])
                #print('%d. %s %s'%(index, pt[0], pt[1]))

        if len(devices)==0:
            #print('No USB device found.')
            devices.append('не найдено')

        return devices

    # @_FileLogger
    def readbincode(self, len=9):
        r = UDevice._port.read(len)
        print("readbincode("+str(len)+"): ", r.hex())
        return r

    def writebincode(self, data : bytes, len=8) -> bytes:
        crc_data = self._add_CRC16(data)
        print("writebincode("+str(len)+"): ", crc_data.hex())
        UDevice._port.write(crc_data[:len])
        return crc_data

    def flush(self):
        UDevice._port.flush()

    def _add_CRC16(self, data: bytes) -> bytes:
        crc16 = libscrc.modbus(data)
        b78 = crc16.to_bytes(2, byteorder='little')
        # print("_add_CRC16(): b78: ", b78.hex(), "crc16: ", crc16)
        l = list(data)
        l.append(int(b78[0]))
        l.append(int(b78[1]))
        return bytes(l)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # print(sys.getsizeof(2 ** 63))
    # print(type(2 ** 63))
    device = UDevice()

    window.setup_window(device)
    window.show()
    sys.exit(app.exec_())
