#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  # We need sys so that we can pass argv to QApplication
import os
from datetime import datetime
import numpy as np
import serial
import serial.tools.list_ports as prtlst
# import serial.tools.list_ports
import libscrc

from PyQt5 import QtWidgets, QtCore, uic

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import time

from ui.binwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ''' Основное окно программы    '''
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def set_devs(self, devs):
        self.portCBox.clear()
        for d in devs:
            self.portCBox.addItem(d)

    def get_bytes(self):
        cmd = self.cmdLineEdit.text()
        bl = bytes.fromhex(cmd)
        # self.statusbar.showMessage(str(_add_CRC16(bl)))
        print('get_bytes:', bl)
        return bl

    def show_res(self, data : bytes):
        self.statusbar.showMessage(str(data), 1000)
        self.textEdit.insertPlainText(str(data)+'\n');
        sb = self.textEdit.verticalScrollBar();
        sb.setValue(sb.maximum());
        print('show_res: ', data)

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
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect( lambda: print("time") )
        self.timer.start(1000)

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
        r = UDevice._port.read(8)
        return r

    def writebincode(self, data : bytes):
        crc_data = _add_CRC16(data)
        UDevice._port.write(crc_data)
        return crc_data

def _add_CRC16(data: bytes):
    crc16 = libscrc.modbus(data)
    b78 = crc16.to_bytes(2, byteorder='little')
    l = list(data)
    l.append(int(b78[0]))
    l.append(int(b78[1]))
    return bytes(l)

def _test_send():
    device = UDevice()
    devl = UDevice.get_devs()
    device.open(devl[0], 9600, 3)

    code = b'\x01\x02\x03\x04\x05\x01'
    print('write: ', _add_CRC16(code))
    device.writebincode(_add_CRC16(code))
    print('read', device.readbincode());

    code = b'\x01\x02\x03\x04\x05\x02'
    print('write: ', _add_CRC16(code))
    device.writebincode(_add_CRC16(code))
    print('read', device.readbincode());

    code = b'\x01\x02\x03\x04\x05\x03'
    print('write: ', _add_CRC16(code))
    device.writebincode(_add_CRC16(code))
    print('read', device.readbincode());


    code = b'\x01\x02\x03\x04\x05\x04'
    print('write: ', _add_CRC16(code))
    device.writebincode(_add_CRC16(code))
    print('read', device.readbincode());
    # b1 = b'\x20\x03\x00\x01\x00\x01'
    # b2 = _add_CRC16(b1)
    # print('sum: ', b2)

def _test_window():
    window = MainWindow()
    device = UDevice()

    window.openButton.clicked.connect( lambda : {
        device.open(window.portCBox.currentText(), int(window.speedCBox.currentText()), 0.1)
        })

    window.closeButton.clicked.connect( lambda :{
        device.close()
        })

    window.refButton.clicked.connect( lambda : {
        window.set_devs(UDevice.get_devs())
        })

    window.sendButton.clicked.connect( lambda : {
        device.writebincode(window.get_bytes()),
        time.sleep(0.1),
        window.show_res(device.readbincode())
        })

    window.readButton.clicked.connect( lambda : {
        window.show_res(device.readbincode())
        })

    window.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # _test_send()
    _test_window()
    sys.exit(app.exec_())
