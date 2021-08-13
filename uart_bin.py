#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  # We need sys so that we can pass argv to QApplication
import os
from datetime import datetime
# import numpy as np
import serial
import serial.tools.list_ports as prtlst
# import serial.tools.list_ports
import libscrc
from PyQt5 import QtWidgets, QtGui, QtCore, uic

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import time

#from ui.binwindow import Ui_MainWindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_0 = QtWidgets.QGridLayout()
        self.gridLayout_0.setObjectName("gridLayout_0")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_0.addItem(spacerItem, 4, 0, 1, 1)
        self.responseGBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responseGBox.sizePolicy().hasHeightForWidth())
        self.responseGBox.setSizePolicy(sizePolicy)
        self.responseGBox.setObjectName("responseGBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.responseGBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.responseGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.cleanButton = QtWidgets.QPushButton(self.responseGBox)
        self.cleanButton.setObjectName("cleanButton")
        self.verticalLayout.addWidget(self.cleanButton)
        self.gridLayout_0.addWidget(self.responseGBox, 0, 1, 5, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.photoLineEdit_1 = QtWidgets.QLineEdit(self.groupBox)
        self.photoLineEdit_1.setText("")
        self.photoLineEdit_1.setReadOnly(True)
        self.photoLineEdit_1.setObjectName("photoLineEdit_1")
        self.verticalLayout_2.addWidget(self.photoLineEdit_1)
        self.photoLineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.photoLineEdit_2.setReadOnly(True)
        self.photoLineEdit_2.setObjectName("photoLineEdit_2")
        self.verticalLayout_2.addWidget(self.photoLineEdit_2)
        self.photoButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.photoButton_1.setObjectName("photoButton_1")
        self.verticalLayout_2.addWidget(self.photoButton_1)
        self.photoButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.photoButton_2.setObjectName("photoButton_2")
        self.verticalLayout_2.addWidget(self.photoButton_2)
        self.gridLayout_0.addWidget(self.groupBox, 2, 0, 1, 1)
        self.requestGBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requestGBox.sizePolicy().hasHeightForWidth())
        self.requestGBox.setSizePolicy(sizePolicy)
        self.requestGBox.setObjectName("requestGBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.requestGBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sendButton = QtWidgets.QPushButton(self.requestGBox)
        self.sendButton.setObjectName("sendButton")
        self.gridLayout_2.addWidget(self.sendButton, 2, 1, 1, 2)
        self.cmdChBox = QtWidgets.QCheckBox(self.requestGBox)
        self.cmdChBox.setObjectName("cmdChBox")
        self.gridLayout_2.addWidget(self.cmdChBox, 1, 1, 1, 1)
        self.cmdSBox = QtWidgets.QSpinBox(self.requestGBox)
        self.cmdSBox.setEnabled(False)
        self.cmdSBox.setMinimum(10)
        self.cmdSBox.setMaximum(1000)
        self.cmdSBox.setSingleStep(10)
        self.cmdSBox.setProperty("value", 100)
        self.cmdSBox.setDisplayIntegerBase(10)
        self.cmdSBox.setObjectName("cmdSBox")
        self.gridLayout_2.addWidget(self.cmdSBox, 1, 2, 1, 1)
        self.readButton = QtWidgets.QPushButton(self.requestGBox)
        self.readButton.setObjectName("readButton")
        self.gridLayout_2.addWidget(self.readButton, 3, 1, 1, 2)
        self.cmdLineEdit = QtWidgets.QLineEdit(self.requestGBox)
        self.cmdLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cmdLineEdit.setMaxLength(12)
        self.cmdLineEdit.setObjectName("cmdLineEdit")
        self.gridLayout_2.addWidget(self.cmdLineEdit, 0, 1, 1, 2)
        self.gridLayout_0.addWidget(self.requestGBox, 1, 0, 1, 1)
        self.settingsGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.settingsGBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsGBox.sizePolicy().hasHeightForWidth())
        self.settingsGBox.setSizePolicy(sizePolicy)
        self.settingsGBox.setObjectName("settingsGBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.settingsGBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_1 = QtWidgets.QGridLayout()
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.portCBox = QtWidgets.QComboBox(self.settingsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portCBox.sizePolicy().hasHeightForWidth())
        self.portCBox.setSizePolicy(sizePolicy)
        self.portCBox.setMinimumSize(QtCore.QSize(140, 0))
        self.portCBox.setObjectName("portCBox")
        self.gridLayout_1.addWidget(self.portCBox, 2, 0, 1, 1)
        self.refButton = QtWidgets.QPushButton(self.settingsGBox)
        self.refButton.setObjectName("refButton")
        self.gridLayout_1.addWidget(self.refButton, 5, 0, 1, 1)
        self.speedLabel = QtWidgets.QLabel(self.settingsGBox)
        self.speedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout_1.addWidget(self.speedLabel, 3, 0, 1, 1)
        self.openButton = QtWidgets.QPushButton(self.settingsGBox)
        self.openButton.setObjectName("openButton")
        self.gridLayout_1.addWidget(self.openButton, 6, 0, 1, 1)
        self.portLabel = QtWidgets.QLabel(self.settingsGBox)
        self.portLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout_1.addWidget(self.portLabel, 1, 0, 1, 1)
        self.speedCBox = QtWidgets.QComboBox(self.settingsGBox)
        self.speedCBox.setObjectName("speedCBox")
        self.speedCBox.addItem("")
        self.speedCBox.addItem("")
        self.speedCBox.addItem("")
        self.speedCBox.addItem("")
        self.speedCBox.addItem("")
        self.gridLayout_1.addWidget(self.speedCBox, 4, 0, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.settingsGBox)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_1.addWidget(self.closeButton, 7, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_1, 1, 0, 1, 1)
        self.gridLayout_0.addWidget(self.settingsGBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.taxoLineEdit_0 = QtWidgets.QLineEdit(self.groupBox_2)
        self.taxoLineEdit_0.setObjectName("taxoLineEdit_0")
        self.horizontalLayout.addWidget(self.taxoLineEdit_0)
        self.taxoLineEdit_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.taxoLineEdit_1.setText("")
        self.taxoLineEdit_1.setObjectName("taxoLineEdit_1")
        self.horizontalLayout.addWidget(self.taxoLineEdit_1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.taxoLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.taxoLineEdit_2.setReadOnly(True)
        self.taxoLineEdit_2.setObjectName("taxoLineEdit_2")
        self.verticalLayout_4.addWidget(self.taxoLineEdit_2)
        self.taxoButton_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.taxoButton_1.setObjectName("taxoButton_1")
        self.verticalLayout_4.addWidget(self.taxoButton_1)
        self.taxoButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.taxoButton_2.setObjectName("taxoButton_2")
        self.verticalLayout_4.addWidget(self.taxoButton_2)
        self.gridLayout_0.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.speedLabel.setBuddy(self.speedCBox)
        self.portLabel.setBuddy(self.portCBox)

        self.retranslateUi(MainWindow)
        self.cmdChBox.clicked['bool'].connect(self.cmdSBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Физприбор 3.3.12а"))
        self.responseGBox.setTitle(_translate("MainWindow", "Ответ:"))
        self.cleanButton.setText(_translate("MainWindow", "Очистить"))
        self.groupBox.setTitle(_translate("MainWindow", "Опрос фотоприёмника"))
        self.photoLineEdit_2.setText(_translate("MainWindow", "200300010001"))
        self.photoButton_1.setText(_translate("MainWindow", "Старт"))
        self.photoButton_2.setText(_translate("MainWindow", "Стоп"))
        self.requestGBox.setTitle(_translate("MainWindow", "Команда:"))
        self.sendButton.setText(_translate("MainWindow", "Отправить"))
        self.cmdChBox.setText(_translate("MainWindow", "Через интервал (мс)"))
        self.readButton.setText(_translate("MainWindow", "Принять"))
        self.settingsGBox.setTitle(_translate("MainWindow", "Настройка COM порта:"))
        self.refButton.setText(_translate("MainWindow", "Обновить"))
        self.speedLabel.setText(_translate("MainWindow", "Скорость:"))
        self.openButton.setText(_translate("MainWindow", "Открыть"))
        self.portLabel.setText(_translate("MainWindow", "Номер:"))
        self.speedCBox.setItemText(0, _translate("MainWindow", "9600"))
        self.speedCBox.setItemText(1, _translate("MainWindow", "19200"))
        self.speedCBox.setItemText(2, _translate("MainWindow", "38400"))
        self.speedCBox.setItemText(3, _translate("MainWindow", "57600"))
        self.speedCBox.setItemText(4, _translate("MainWindow", "115200"))
        self.closeButton.setText(_translate("MainWindow", "Закрыть"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Опрос тахометра"))
        self.taxoLineEdit_2.setText(_translate("MainWindow", "100300010001"))
        self.taxoButton_1.setText(_translate("MainWindow", "Старт"))
        self.taxoButton_2.setText(_translate("MainWindow", "Стоп"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ''' Основное окно программы    '''
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.textEdit.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.cleanButton.clicked.connect( lambda : { self.textEdit.clear() })

    def set_devs(self, devs):
        self.portCBox.clear()
        for d in devs:
            self.portCBox.addItem(d)

    def get_bytes(self):
        cmd = self.cmdLineEdit.text()
        try:
            bl = bytes.fromhex(cmd)
            print('get_bytes:', bl.hex())
        except Exception as e:
            self.statusbar.showMessage(str(e), 3000)
        return bl

    def get_ph(self):
        cmd = self.photoLineEdit_2.text()
        try:
            bl = bytes.fromhex(cmd)
            print('get_ph:', bl)
        except Exception as e:
            self.statusbar.showMessage(str(e), 3000)
        return bl

    def get_taxo(self):
        cmd = self.taxoLineEdit_2.text()
        try:
            bl = bytes.fromhex(cmd)
            print('get_ph:', bl)
        except Exception as e:
            self.statusbar.showMessage(str(e), 3000)
        return bl

    def show_res(self, data : bytes):
        now = datetime.now() # current date and time
        self.statusbar.showMessage(data.hex(), 1000)
        self.textEdit.insertPlainText(data.hex() +" "+now.strftime("%H:%M:%S %f")+'\n')
        sb = self.textEdit.verticalScrollBar()
        sb.setValue(sb.maximum())
        print('show_res: ', data.hex())

    def show_ph(self, data : bytes):
        msg = str(int.from_bytes(data[3:7], byteorder='little', signed=False))
        print("show_ph():", msg, data[3:7].hex())
        self.photoLineEdit_1.setText(msg)
        # self.textEdit.insertPlainText(str(data)+" "+now.strftime("%H:%M:%S %f")+'\n');

    def show_taxo(self, data : bytes):
        t = int.from_bytes(data[3:7], byteorder='little', signed=False)
        msg1 = str(t)
        print("show_ph():", msg1, data[3:7].hex())
        self.taxoLineEdit_1.setText(msg1)
        if (t == 0):
            self.taxoLineEdit_0.setText("-")
        else: 
            msg0 = "%.3f" % (60000000/t)
            self.taxoLineEdit_0.setText(msg0)

class FixedSerial( serial.Serial ):
    '''To fix bug on Windows system'''
    def _reconfigure_port( self, *args, **kwargs ):
        try:
            super()._reconfigure_port( *args, **kwargs )
        except serial.SerialException:
            pass


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
        except Exception as e:
            print(e)
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
            devices.append('no device')

        return devices

    @_FileLogger
    def readbincode(self):
        r = UDevice._port.read(9)
        print("readbincode() ", r.hex())
        return r

    def writebincode(self, data : bytes):
        crc_data = _add_CRC16(data)
        UDevice._port.write(crc_data)
        return crc_data

def _add_CRC16(data: bytes):
    crc16 = libscrc.modbus(data)
    b78 = crc16.to_bytes(2, byteorder='little')
    print("b78: ", b78.hex(), "crc16: ", crc16)
    l = list(data)
    l.append(int(b78[0]))
    l.append(int(b78[1]))
    return bytes(l)

def _test_send():
    devl = UDevice.get_devs()
    device.open(devl[0], 9600, 3)

    code = b'\x01\x02\x03\x04\x05\x01'
    print('write: ', _add_CRC16(code))
    device.writebincode(_add_CRC16(code))
    print('read', device.readbincode())

    code = b'\x01\x02\x03\x04\x05\x02'
    print('write: ', _add_CRC16(code))
    device.writebincode(_add_CRC16(code))
    print('read', device.readbincode())

    code = b'\x01\x02\x03\x04\x05\x03'
    print('write: ', _add_CRC16(code))
    device.writebincode(_add_CRC16(code))
    print('read', device.readbincode())


    code = b'\x01\x02\x03\x04\x05\x04'
    print('write: ', _add_CRC16(code))
    device.writebincode(_add_CRC16(code))
    print('read', device.readbincode())
    # b1 = b'\x20\x03\x00\x01\x00\x01'
    # b2 = _add_CRC16(b1)
    # print('sum: ', b2)

def _test_window():

    timer1.timeout.connect( lambda: {
        device.writebincode(window.get_bytes()),
        window.show_res(device.readbincode())
        })

    timer2.timeout.connect( lambda: {
        device.writebincode(window.get_ph()),
        window.show_ph(device.readbincode())
    })

    timer3.timeout.connect( lambda: {
        device.writebincode(window.get_taxo()),
        window.show_taxo(device.readbincode())
    })

    window.openButton.clicked.connect( lambda : {
        window.statusbar.showMessage("Open("+window.portCBox.currentText()+")", 1000),
        device.open(window.portCBox.currentText(), int(window.speedCBox.currentText()), 0.1)
        })

    window.closeButton.clicked.connect( lambda :{
        window.statusbar.showMessage("Close()"),
        device.close()
        })

    window.refButton.clicked.connect( lambda : {
        window.statusbar.showMessage("Refresh()"),
        window.set_devs(UDevice.get_devs())
        })

    window.sendButton.clicked.connect( lambda : {
        _com(window, device, timer1)
        })

    window.readButton.clicked.connect( lambda : {
        window.show_res(device.readbincode())
        })

    window.photoButton_1.clicked.connect( lambda : {
        timer2.start(100)
        })

    window.photoButton_2.clicked.connect( lambda : {
        timer2.stop()
        })

    window.taxoButton_1.clicked.connect( lambda : {
        timer3.start(100)
        })

    window.taxoButton_2.clicked.connect( lambda : {
        timer3.stop()
        })

    window.show()

def _com(window, device, timer):
    if window.cmdChBox.isChecked() == True:
        print("interval: ", window.cmdSBox.value())
        timer.start(window.cmdSBox.value())
    else:
        timer.stop()
        device.writebincode(window.get_bytes())
        window.show_res(device.readbincode())

def _photo(window, device, timer):
    timer2.timeout.connect( lambda: {
        device.writebincode(window.get_ph()),
        window.show_ph(device.readbincode())
    })

def _taxo(window, device, timer):
    timer3.timeout.connect( lambda: {
        device.writebincode(window.get_taxo()),
        window.show_taxo(device.readbincode())
    })

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    device = UDevice()
    timer1=QtCore.QTimer()
    timer2=QtCore.QTimer()
    timer3=QtCore.QTimer()
    # _test_send()
    _test_window()
    sys.exit(app.exec_())
