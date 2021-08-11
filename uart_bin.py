#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys  # We need sys so that we can pass argv to QApplication
import os
from datetime import datetime
import numpy as np
import serial
import serial.tools.list_ports as prtlst

from PyQt5 import QtWidgets, QtCore, uic

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

class UDevice(QtCore.QThread):
    _dev = None
    _port = None
    newData = QtCore.pyqtSignal(list)

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
            self.newData.emit(['error', str(e)])

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
    def readline(self) ->str:
        line = None
        try:
            data = UDevice._port.readline()
            print(data)
            if data == b'':
                line = ['timeout']
                print(line)
            else:
                line = [ float(x) for x in data.decode('utf-8')[:-2].split(';') ]
        except Exception as e:
            print(e)
            UDevice._dev = None
            line = ['error']
            line.append(str(e))
        return line

    @_FileLogger
    def readbincode(self) -> str:
        return UDevice._port.read(8)

    def writebincode(self, data : bytearray):
        UDevice._port.write(data)

    def run(self):
        while True:
            # посылаем сигнал из второго потока в GUI поток
            if UDevice._dev is not None:
                data = self.readline()
                self.newData.emit(data)
                QtCore.QThread.msleep(100)
            else:
                QtCore.QThread.msleep(300)

if __name__ == '__main__':
    device_list = UDevice.get_devs();
    print(device_list)
    device_thread = UDevice()
    device_thread.open(device_list[0], 9600, 3)
    code = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    device_thread.writebincode(code)
    print('read', device_thread.readbincode());
