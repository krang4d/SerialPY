#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Serial Port Reader by Pavel Golovkin, aka pgg.
# Feel free to use. No warranty
# Version 3.7.28a

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
        MainWindow.resize(1196, 1217)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_motor_setFreq = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_motor_setFreq.sizePolicy().hasHeightForWidth())
        self.groupBox_motor_setFreq.setSizePolicy(sizePolicy)
        self.groupBox_motor_setFreq.setObjectName("groupBox_motor_setFreq")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_motor_setFreq)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_motor_n = QtWidgets.QLabel(self.groupBox_motor_setFreq)
        self.label_motor_n.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_motor_n.setObjectName("label_motor_n")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_motor_n)
        self.spinBox_motor_n = QtWidgets.QSpinBox(self.groupBox_motor_setFreq)
        self.spinBox_motor_n.setMaximum(15)
        self.spinBox_motor_n.setObjectName("spinBox_motor_n")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_motor_n)
        self.label_motor_freq = QtWidgets.QLabel(self.groupBox_motor_setFreq)
        self.label_motor_freq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_motor_freq.setObjectName("label_motor_freq")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_motor_freq)
        self.spinBox_motor_freq = QtWidgets.QSpinBox(self.groupBox_motor_setFreq)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_motor_freq.sizePolicy().hasHeightForWidth())
        self.spinBox_motor_freq.setSizePolicy(sizePolicy)
        self.spinBox_motor_freq.setMaximum(65535)
        self.spinBox_motor_freq.setObjectName("spinBox_motor_freq")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_motor_freq)
        self.pushButton_motor_setFreq = QtWidgets.QPushButton(self.groupBox_motor_setFreq)
        self.pushButton_motor_setFreq.setObjectName("pushButton_motor_setFreq")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton_motor_setFreq)
        self.gridLayout.addWidget(self.groupBox_motor_setFreq, 4, 0, 1, 1)
        self.groupBox_taxo = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_taxo.sizePolicy().hasHeightForWidth())
        self.groupBox_taxo.setSizePolicy(sizePolicy)
        self.groupBox_taxo.setObjectName("groupBox_taxo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_taxo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self._4 = QtWidgets.QGridLayout()
        self._4.setObjectName("_4")
        self.taxoLineEdit_0 = QtWidgets.QLineEdit(self.groupBox_taxo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxoLineEdit_0.sizePolicy().hasHeightForWidth())
        self.taxoLineEdit_0.setSizePolicy(sizePolicy)
        self.taxoLineEdit_0.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(78, 154, 6);")
        self.taxoLineEdit_0.setReadOnly(True)
        self.taxoLineEdit_0.setObjectName("taxoLineEdit_0")
        self._4.addWidget(self.taxoLineEdit_0, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.groupBox_taxo)
        self.label_1.setObjectName("label_1")
        self._4.addWidget(self.label_1, 0, 0, 1, 1)
        self.taxoLineEdit_1 = QtWidgets.QLineEdit(self.groupBox_taxo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxoLineEdit_1.sizePolicy().hasHeightForWidth())
        self.taxoLineEdit_1.setSizePolicy(sizePolicy)
        self.taxoLineEdit_1.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(78, 154, 6);")
        self.taxoLineEdit_1.setReadOnly(True)
        self.taxoLineEdit_1.setObjectName("taxoLineEdit_1")
        self._4.addWidget(self.taxoLineEdit_1, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_taxo)
        self.label_2.setObjectName("label_2")
        self._4.addWidget(self.label_2, 0, 1, 1, 1)
        self.taxoLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_taxo)
        self.taxoLineEdit_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxoLineEdit_2.sizePolicy().hasHeightForWidth())
        self.taxoLineEdit_2.setSizePolicy(sizePolicy)
        self.taxoLineEdit_2.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.taxoLineEdit_2.setReadOnly(True)
        self.taxoLineEdit_2.setObjectName("taxoLineEdit_2")
        self._4.addWidget(self.taxoLineEdit_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_taxo)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self._4.addWidget(self.label_3, 2, 0, 1, 1)
        self.verticalLayout_4.addLayout(self._4)
        self.gridLayout.addWidget(self.groupBox_taxo, 6, 0, 1, 1)
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
        self.groupBox_vibro_status = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_vibro_status.sizePolicy().hasHeightForWidth())
        self.groupBox_vibro_status.setSizePolicy(sizePolicy)
        self.groupBox_vibro_status.setObjectName("groupBox_vibro_status")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_vibro_status)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self._5 = QtWidgets.QHBoxLayout()
        self._5.setContentsMargins(0, -1, -1, -1)
        self._5.setObjectName("_5")
        self.label_vibro_status_n = QtWidgets.QLabel(self.groupBox_vibro_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_vibro_status_n.sizePolicy().hasHeightForWidth())
        self.label_vibro_status_n.setSizePolicy(sizePolicy)
        self.label_vibro_status_n.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vibro_status_n.setObjectName("label_vibro_status_n")
        self._5.addWidget(self.label_vibro_status_n)
        self.spinBox_vibro_status_n = QtWidgets.QSpinBox(self.groupBox_vibro_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_vibro_status_n.sizePolicy().hasHeightForWidth())
        self.spinBox_vibro_status_n.setSizePolicy(sizePolicy)
        self.spinBox_vibro_status_n.setMaximum(15)
        self.spinBox_vibro_status_n.setObjectName("spinBox_vibro_status_n")
        self._5.addWidget(self.spinBox_vibro_status_n)
        self.lineEdit_vibro_status = QtWidgets.QLineEdit(self.groupBox_vibro_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_vibro_status.sizePolicy().hasHeightForWidth())
        self.lineEdit_vibro_status.setSizePolicy(sizePolicy)
        self.lineEdit_vibro_status.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.lineEdit_vibro_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_vibro_status.setObjectName("lineEdit_vibro_status")
        self._5.addWidget(self.lineEdit_vibro_status)
        self.verticalLayout_7.addLayout(self._5)
        self.pushButton_vibro_status = QtWidgets.QPushButton(self.groupBox_vibro_status)
        self.pushButton_vibro_status.setObjectName("pushButton_vibro_status")
        self.verticalLayout_7.addWidget(self.pushButton_vibro_status)
        self.gridLayout.addWidget(self.groupBox_vibro_status, 1, 0, 1, 1)
        self.groupBox_photo = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_photo.sizePolicy().hasHeightForWidth())
        self.groupBox_photo.setSizePolicy(sizePolicy)
        self.groupBox_photo.setObjectName("groupBox_photo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_photo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._3 = QtWidgets.QGridLayout()
        self._3.setObjectName("_3")
        self.label_temp = QtWidgets.QLabel(self.groupBox_photo)
        self.label_temp.setObjectName("label_temp")
        self._3.addWidget(self.label_temp, 0, 0, 1, 1)
        self.photoLineEdit_0 = QtWidgets.QLineEdit(self.groupBox_photo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoLineEdit_0.sizePolicy().hasHeightForWidth())
        self.photoLineEdit_0.setSizePolicy(sizePolicy)
        self.photoLineEdit_0.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(32, 74, 135);")
        self.photoLineEdit_0.setReadOnly(True)
        self.photoLineEdit_0.setObjectName("photoLineEdit_0")
        self._3.addWidget(self.photoLineEdit_0, 1, 0, 1, 1)
        self.label_ADC = QtWidgets.QLabel(self.groupBox_photo)
        self.label_ADC.setObjectName("label_ADC")
        self._3.addWidget(self.label_ADC, 0, 1, 1, 1)
        self.photoLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_photo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoLineEdit_2.sizePolicy().hasHeightForWidth())
        self.photoLineEdit_2.setSizePolicy(sizePolicy)
        self.photoLineEdit_2.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.photoLineEdit_2.setReadOnly(True)
        self.photoLineEdit_2.setObjectName("photoLineEdit_2")
        self._3.addWidget(self.photoLineEdit_2, 2, 1, 1, 1)
        self.label_cmd = QtWidgets.QLabel(self.groupBox_photo)
        self.label_cmd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cmd.setObjectName("label_cmd")
        self._3.addWidget(self.label_cmd, 2, 0, 1, 1)
        self.photoLineEdit_1 = QtWidgets.QLineEdit(self.groupBox_photo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoLineEdit_1.sizePolicy().hasHeightForWidth())
        self.photoLineEdit_1.setSizePolicy(sizePolicy)
        self.photoLineEdit_1.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(32, 74, 135);")
        self.photoLineEdit_1.setReadOnly(True)
        self.photoLineEdit_1.setObjectName("photoLineEdit_1")
        self._3.addWidget(self.photoLineEdit_1, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self._3)
        self._2 = QtWidgets.QFormLayout()
        self._2.setObjectName("_2")
        self.label_N1 = QtWidgets.QLabel(self.groupBox_photo)
        self.label_N1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_N1.setObjectName("label_N1")
        self._2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_N1)
        self.spinBox_N1 = BigIntSpinbox(self.groupBox_photo)
        # self.spinBox_N1.setMaximum(999999999)
        self.spinBox_N1.setObjectName("spinBox_N1")
        self._2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_N1)
        self.label_N2 = QtWidgets.QLabel(self.groupBox_photo)
        self.label_N2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_N2.setObjectName("label_N2")
        self._2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_N2)
        self.spinBox_N2 = BigIntSpinbox(self.groupBox_photo)
        # self.spinBox_N2.setMaximum(999999999)
        self.spinBox_N2.setObjectName("spinBox_N2")
        self._2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_N2)
        self.label_T1 = QtWidgets.QLabel(self.groupBox_photo)
        self.label_T1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_T1.setObjectName("label_T1")
        self._2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_T1)
        self.spinBox_T1 = QtWidgets.QSpinBox(self.groupBox_photo)
        self.spinBox_T1.setMinimum(-999999999)
        self.spinBox_T1.setMaximum(999999999)
        self.spinBox_T1.setObjectName("spinBox_T1")
        self._2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_T1)
        self.label_T2 = QtWidgets.QLabel(self.groupBox_photo)
        self.label_T2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_T2.setObjectName("label_T2")
        self._2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_T2)
        self.spinBox_T2 = QtWidgets.QSpinBox(self.groupBox_photo)
        self.spinBox_T2.setMinimum(-999999999)
        self.spinBox_T2.setMaximum(999999999)
        self.spinBox_T2.setObjectName("spinBox_T2")
        self._2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_T2)
        self.label_calibr = QtWidgets.QLabel(self.groupBox_photo)
        self.label_calibr.setObjectName("label_calibr")
        self._2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_calibr)
        self.verticalLayout_2.addLayout(self._2)
        self.gridLayout.addWidget(self.groupBox_photo, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.cleanButton = QtWidgets.QPushButton(self.centralwidget)
        self.cleanButton.setObjectName("cleanButton")
        self.horizontalLayout.addWidget(self.cleanButton)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 2)
        self.groupBox_motor_getFreq = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_motor_getFreq.sizePolicy().hasHeightForWidth())
        self.groupBox_motor_getFreq.setSizePolicy(sizePolicy)
        self.groupBox_motor_getFreq.setObjectName("groupBox_motor_getFreq")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_motor_getFreq)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self._1 = QtWidgets.QHBoxLayout()
        self._1.setObjectName("_1")
        self.label_moto_x = QtWidgets.QLabel(self.groupBox_motor_getFreq)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_moto_x.sizePolicy().hasHeightForWidth())
        self.label_moto_x.setSizePolicy(sizePolicy)
        self.label_moto_x.setObjectName("label_moto_x")
        self._1.addWidget(self.label_moto_x)
        self.spinBox_motor_x = QtWidgets.QSpinBox(self.groupBox_motor_getFreq)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_motor_x.sizePolicy().hasHeightForWidth())
        self.spinBox_motor_x.setSizePolicy(sizePolicy)
        self.spinBox_motor_x.setMaximum(15)
        self.spinBox_motor_x.setObjectName("spinBox_motor_x")
        self._1.addWidget(self.spinBox_motor_x)
        self.lineEdit_motor_freq_x = QtWidgets.QLineEdit(self.groupBox_motor_getFreq)
        self.lineEdit_motor_freq_x.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_motor_freq_x.sizePolicy().hasHeightForWidth())
        self.lineEdit_motor_freq_x.setSizePolicy(sizePolicy)
        self.lineEdit_motor_freq_x.setReadOnly(True)
        self.lineEdit_motor_freq_x.setObjectName("lineEdit_motor_freq_x")
        self._1.addWidget(self.lineEdit_motor_freq_x)
        self.verticalLayout_6.addLayout(self._1)
        self.pushButton_motor_getFreq = QtWidgets.QPushButton(self.groupBox_motor_getFreq)
        self.pushButton_motor_getFreq.setObjectName("pushButton_motor_getFreq")
        self.verticalLayout_6.addWidget(self.pushButton_motor_getFreq)
        self.gridLayout.addWidget(self.groupBox_motor_getFreq, 2, 0, 1, 1)
        self.groupBox_graphs = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_graphs.setObjectName("groupBox_graphs")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_graphs)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.groupBox_graphs)
        self.widget.setObjectName("widget")
        self.verticalLayout_5.addWidget(self.widget)
        self.gridLayout.addWidget(self.groupBox_graphs, 0, 1, 7, 1)
        self.groupBox_vibro_data = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_vibro_data.sizePolicy().hasHeightForWidth())
        self.groupBox_vibro_data.setSizePolicy(sizePolicy)
        self.groupBox_vibro_data.setObjectName("groupBox_vibro_data")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_vibro_data)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_vibro_n = QtWidgets.QLabel(self.groupBox_vibro_data)
        self.label_vibro_n.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_vibro_n.setObjectName("label_vibro_n")
        self.gridLayout_2.addWidget(self.label_vibro_n, 0, 0, 1, 1)
        self.spinBox_vibro_n = QtWidgets.QSpinBox(self.groupBox_vibro_data)
        self.spinBox_vibro_n.setMaximum(15)
        self.spinBox_vibro_n.setObjectName("spinBox_vibro_n")
        self.gridLayout_2.addWidget(self.spinBox_vibro_n, 0, 1, 1, 1)
        self.pushButton_vobro_data = QtWidgets.QPushButton(self.groupBox_vibro_data)
        self.pushButton_vobro_data.setObjectName("pushButton_vobro_data")
        self.gridLayout_2.addWidget(self.pushButton_vobro_data, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_vibro_data, 3, 0, 1, 1)
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
        self.gridLayout.addWidget(self.groupBox_messenger, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1196, 22))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Физприбор 3.7.28а"))
        self.groupBox_motor_setFreq.setTitle(_translate("MainWindow", "Установка частоты вращения вала двигателя"))
        self.label_motor_n.setText(_translate("MainWindow", "Номер:"))
        self.label_motor_freq.setText(_translate("MainWindow", "Частота:"))
        self.pushButton_motor_setFreq.setText(_translate("MainWindow", "Задать"))
        self.groupBox_taxo.setTitle(_translate("MainWindow", "Опрос тахометра"))
        self.label_1.setText(_translate("MainWindow", "Скорость  (oб/мин):"))
        self.label_2.setText(_translate("MainWindow", "ADC:"))
        self.taxoLineEdit_2.setText(_translate("MainWindow", "100300010001"))
        self.label_3.setText(_translate("MainWindow", "Команда:"))
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
        self.groupBox_vibro_status.setTitle(_translate("MainWindow", "Запрос состояния платы фотоприёмника виброметра"))
        self.label_vibro_status_n.setText(_translate("MainWindow", "X:"))
        self.pushButton_vibro_status.setText(_translate("MainWindow", "Запросить"))
        self.groupBox_photo.setTitle(_translate("MainWindow", "Опрос фотоприёмника"))
        self.label_temp.setText(_translate("MainWindow", "Температура °C:"))
        self.label_ADC.setText(_translate("MainWindow", "ADC:"))
        self.photoLineEdit_2.setText(_translate("MainWindow", "200300010001"))
        self.label_cmd.setText(_translate("MainWindow", "Команда:"))
        self.label_N1.setText(_translate("MainWindow", "N1"))
        self.label_N2.setText(_translate("MainWindow", "N2"))
        self.label_T1.setText(_translate("MainWindow", "T1"))
        self.label_T2.setText(_translate("MainWindow", "T2"))
        self.label_calibr.setText(_translate("MainWindow", "Параметры калибровки:"))
        self.startButton.setText(_translate("MainWindow", "Старт"))
        self.stopButton.setText(_translate("MainWindow", "Стоп"))
        self.cleanButton.setText(_translate("MainWindow", "Очистить"))
        self.groupBox_motor_getFreq.setTitle(_translate("MainWindow", "Запрос периода вращения вала двигателя:"))
        self.label_moto_x.setText(_translate("MainWindow", "X:"))
        self.pushButton_motor_getFreq.setText(_translate("MainWindow", "Запросить"))
        self.groupBox_graphs.setTitle(_translate("MainWindow", "Графики"))
        self.groupBox_vibro_data.setTitle(_translate("MainWindow", "Запрос данных с АЦП виброметра"))
        self.label_vibro_n.setText(_translate("MainWindow", "Номер фотоприёмника:"))
        self.pushButton_vobro_data.setText(_translate("MainWindow", "Запросить"))
        self.groupBox_messenger.setTitle(_translate("MainWindow", "Ответ:"))

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
        # self.spinBox_N1 = BigIntSpinbox(self.groupBox_photo)
        # self.spinBox_N2 = BigIntSpinbox(self.groupBox_photo)

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

    def setup_window(self):
        """
        Connect all signalls to slots, 
        """
        # self.timer1.timeout.connect( lambda: {
        #     device.writebincode(self.get_bytes()),
        #     self.show_res(device.readbincode())
        #     })
        self.device = UDevice()
        self.startButton.clicked.connect(self.start_slot)
        self.stopButton.clicked.connect(self.stop_slot)

        self.plots_timer.timeout.connect( lambda: {
            self.device.writebincode(self.get_ph()),
            self.show_ph(self.device.readbincode()),
            # time.sleep(0.02),
            self.device.writebincode(self.get_taxo()),
            self.show_taxo(self.device.readbincode())
        })

        self.openButton.clicked.connect( lambda : {
            self.statusbar.showMessage("Открытие порта "+self.portCBox.currentText()+".", 3000),
            self.device.open(self.portCBox.currentText(), int(self.speedCBox.currentText()), 0.1)
            })

        self.closeButton.clicked.connect( lambda :{
            self.statusbar.showMessage("Закрытие порта "+self.device.get_device_name()+".", 3000),
            self.device.close()
            })

        self.refButton.clicked.connect( lambda : {
            self.statusbar.showMessage("Обновление устройств.", 3000),
            self.set_devs(UDevice.get_devs())
            })

        self.pushButton_vobro_data.clicked.connect(self.vibro_data_slot)
        self.pushButton_vibro_status.clicked.connect(self.vibro_status_slot)
        self.pushButton_motor_getFreq.clicked.connect(self.motor_getFreq_slot)
        self.pushButton_motor_setFreq.clicked.connect(self.motor_setFreq_slot)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    def start_slot(self):
        self.plots_timer.start(100)
        self.start_flag = True

    def stop_slot(self):
        self.plots_timer.stop()
        # self.device.flush()
        self.start_flag = False

    def vibro_data_slot(self):
        """
        Запрос данных с АЦП виброметра: 3X 03 00 02 00 01 CS CS
        Ответ на запрос: 3X 03 01 BN ... B1 CS CS, где
        BN … B1 массив 16 разрядных отсчётов АЦП виброметра (N = 1024)
        """
        self.statusbar.showMessage("Запрос данных с АЦП виброметра.", 3000)
        self.plots_timer.stop()
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file', '.',"Text files (*.txt)")
        if fname[0] == '':
            return 0
        print(fname, os.path.isfile(fname[0]))

        code = list(b'\x30\x03\x00\x02\x00\x01') # 3X 03 00 02 00 01
        code[0] = code[0] + self.spinBox_vibro_status_n.value()
        self.device.writebincode(bytes(code))
        time.sleep(.1)
        if(self.start_flag):
            self.stop_slot()
            data = self.device.readbincode(1029)
            self.device.flush()
            self.start_slot()
        else:
            data = self.device.readbincode(1029)

        data_invert = [int.from_bytes(b, byteorder='big') for b in chunks(data[3:-2], 2)][::-1]
        print(data_invert)
        with open(fname[0], 'w') as f:
            for b in data_invert: f.write(str(b)+'\n')

    def vibro_status_slot(self):
        """
        Запрос состояния платы фотоприёмника виброметра: 3X 04 00 00 00 01 CS CS
        Ответ на запрос: 3X 04 01 NN CS CS, где
        NN- состояние платы: 00- исправна, 01- неисправна
        """
        self.statusbar.showMessage("Запрос состояния платы фотоприёмника виброметра.", 3000)
        self.plots_timer.stop()

        code = list(b'\x30\x04\x00\x01\x00\x01') # 3X 03 00 02 00 01
        code[0] = code[0] + self.spinBox_vibro_status_n.value()
        self.device.writebincode(bytes(code))
        time.sleep(.02)
        if(self.start_flag):
            self.stop_slot()
            data = self.device.readbincode(6)
            self.device.flush()
            self.start_slot()
        else:
            data = self.device.readbincode()

        if(list(data)[3] != 0x00):
            self.lineEdit_vibro_status.setText("Исправна")
            self.lineEdit_vibro_status.setStyleSheet("color: green; background-color: rgb(238, 238, 236);")
        else:
            self.lineEdit_vibro_status.setText("Неисправна")
            self.lineEdit_vibro_status.setStyleSheet("color: red; background-color: rgb(238, 238, 236);")

    def motor_setFreq_slot(self):
        """
        Задать частоту вращения вала двигателя: 3X 06 00 01 HH LL CS CS,
        где HH LL – целое 16-битное число, соответствующее частоте вращения вала двигателя, об/мин
        """
        self.statusbar.showMessage("Задать частоту вращения вала двигателя.", 3000)
        self.plots_timer.stop()
        code = list(b'\x30\x06\x00\x01\x00\x00')
        code[0] = code[0] + self.spinBox_motor_n.value()
        freq = self.spinBox_motor_freq.value().to_bytes(2, 'big')
        code[4]= freq[0]
        code[5]= freq[1]
        self.device.writebincode(bytes(code))
        time.sleep(.02)
        if(self.start_flag):
            self.stop_slot()
            data = self.device.readbincode()
            self.device.flush()
            self.start_slot()
        else:
            data = self.device.readbincode()

    def motor_getFreq_slot(self):
        """
        Запрос регистра данных периода вращения вала двигателя: 3X 03 00 01 00 01 CS CS,
        где Х- номер фотоприёмника виброметра (указывается или перемычками на плате, или программируется на объекте). По умолчанию 0
        Итоговая команда по-умолчанию: 30 03 00 01 00 01 D1 EB
        Ответ на запрос: 3X 03 00 01 HH LL CS CS
        """
        self.statusbar.showMessage("Запрос регистра данных периода вращения вала двигателя.", 3000)
        self.plots_timer.stop()
        code = list(b'\x30\x03\x00\x01\x00\x01')
        code[0] = code[0] + self.spinBox_motor_n.value()
        self.device.writebincode(bytes(code))
        time.sleep(.02)
        if(self.start_flag):
            self.stop_slot()
            data = self.device.readbincode()
            self.device.flush()
            self.start_slot()
        else:
            data = self.device.readbincode()
        self.plots_timer.stop()

    def normalOutputWritten(self, text):
        """
        Append text to the QTextEdit.
        """
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
        """
        Функция добавления новой точки на график фотоприемника
        """
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
        """
        Функция обновления всех значейний фотоприемника
        """
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
        """
        Функция добавления новой точки на график скрости тахометра
        """
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
        """
        Функция обновления в окне всех значейний тахометра
        """
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
    """
    To fix bug on Windows 10 system
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
    """
    Wrapper (decorator) for log incomming data from device
    """
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
            print("Error: Port "+ dev +" not found.")
            # self.newData.emit(['error', str(e)])

    def close(self):
        if UDevice._dev is not None:
            print('Close Port '+ UDevice._dev)
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
    def readbincode(self, n=9):
        r = UDevice._port.read(n)
        print("readbincode("+str(len(r))+"/"+str(n)+"): ", r.hex())
        return r

    def get_device_name(self):
        return UDevice._dev

    def writebincode(self, data : bytes, n=8) -> bytes:
        crc_data = self._add_CRC16(data)
        print("writebincode("+str(n)+"): ", crc_data.hex())
        UDevice._port.write(crc_data[:n])
        return crc_data

    def flush(self):
        UDevice._port.flush()
        UDevice._port.flushInput()
        UDevice._port.flushOutput()

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
    window.setup_window()
    window.show()
    sys.exit(app.exec_())
