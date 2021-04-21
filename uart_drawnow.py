#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from datetime import datetime
import numpy as np
import serial
import serial.tools.list_ports as prtlst
from abc import ABCMeta, abstractmethod

from ui.MainWindow import Ui_MainWindow
from ui.AboutForm import Ui_AboutForm
# Create an Iterator for scale X on plot

class FixedSerial( serial.Serial ):
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
            if data == b'':
                line = ['timeout']
                print(line)
            else: line = [ int(x) for x in data.decode('utf-8')[:-2].split(';') ]
        except Exception as e:
            print(e)
            UDevice._dev = None
            line = ['error']
            line.append(str(e))
        return line

    def run(self):
        while True:
            # посылаем сигнал из второго потока в GUI поток
            if UDevice._dev is not None:
                data = self.readline()
                self.newData.emit(data)
                QtCore.QThread.msleep(100)
            else:
                QtCore.QThread.msleep(300)

class AboutForm(QtWidgets.QDialog, Ui_AboutForm):
    def __init__(self, *args, obj=None, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        self.setupUi(self)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    _num = 100

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self._index = iter(NumbersIterator())
        self.aboutForm = AboutForm()
        self.actionAbout.triggered.connect(self.aboutForm.show)

        self._y1 = list()
        self._y2 = list()
        self._y3 = list()
        self._x  = list()

        self.graphWidget1 = pg.PlotWidget()
        self.graphWidget2 = pg.PlotWidget()

        self.graphWidget1.setBackground((100,50,255,0))
        self.graphWidget2.setBackground((100,50,255,0))

        styles = {'color':'b', 'font-size':'14px'}
        self.graphWidget1.setLabel('left', 'RPM', **styles)
        self.graphWidget2.setLabel('left', 'ADC, T (C)', **styles)

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
        self._line1 = self.graphWidget1.plot(self._x, self._y1, name='RPM', symbolBrush=(0, 180, 0), symbolSize=6, pen=pen)
        pen = pg.mkPen(color='b', width=2, style=QtCore.Qt.SolidLine)
        self._line2 = self.graphWidget2.plot(self._x, self._y2, name='T(C)/16', symbolBrush='b', symbolSize=6, pen=pen)
        pen = pg.mkPen(color=(196, 160, 0), width=2, style=QtCore.Qt.SolidLine)
        self._line3 = self.graphWidget2.plot(self._x, self._y3, name='ADC', symbolBrush=(196, 160, 0), symbolSize=6, pen=pen)

    def set_dev(self, devs):
        self.serialCBox.clear()
        for dev in devs:
            self.serialCBox.addItem(dev)
            #self.statusbar.showMessage('device list updated')

    @staticmethod
    def set_num(i: int):
        MainWindow._num = i

    def update_plot_data(self, data=None):
        if data is None:
            self._line1.setData(self._x, self._y1)  # Update the data.
            self._line2.setData(self._x, self._y2)  # Update the data.
            self._line3.setData(self._x, self._y3)  # Update the data.
        elif data[0] == 'timeout':
            self.statusbar.showMessage('timeout')
        elif data[0] == 'error':
            self.statusbar.showMessage('error: '+ data[1])
        else:
            self.statusbar.showMessage('data: '+str(data))
            if len(self._x) >= self._num:
                cut = len(self._x) - self._num + 1
                self._x = self._x[cut:]       # Remove the first
                self._y1 = self._y1[cut:]     # Remove the first
                self._y2 = self._y2[cut:]     # Remove the first
                self._y3 = self._y3[cut:]     # Remove the first

            data[2] = data[2]/16
            self._x.append(next(self._index)) #self._x[-1] + 1)   # Add a new value 1 higher than the last.
            self._y1.append( data[0])   # Add a new value.
            self._y2.append( data[2])   # Add a new value.
            self._y3.append( data[3])   # Add a new value.

            self._line1.setData(self._x, self._y1)  # Update the data.
            self._line2.setData(self._x, self._y2)  # Update the data.
            self._line3.setData(self._x, self._y3)  # Update the data.

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    timer=QtCore.QTimer()
    timer.timeout.connect( lambda: window.set_dev(UDevice.get_devs()))
    timer.start(1000)

    # window.openButton.clicked.connect( lambda: { device.open(window.serial_comboBox.currentText(), int(window.baudrate_comboBox.currentText()), 3), print(device.readline()) } )
        # lambda: window.statusbar.showMessage(
        # window.baudrate_comboBox.currentText() + window.serial_comboBox.currentText()))
    # window.closeButton.clicked.connect(lambda: device.close())

    thread = UDevice()
    thread.newData.connect(window.update_plot_data)

    window.startButton.clicked.connect( lambda: {
        thread.open(window.serialCBox.currentText(), int(window.baudrateCBox.currentText()), 3)
        })
    window.stopButton.clicked.connect(lambda: {
        thread.close()
        })

    window.cleanButton.clicked.connect(lambda: {
        window._index.reset(),
        window._x.clear(),
        window._y1.clear(),
        window._y2.clear(),
        window._y3 .clear(),
        window.update_plot_data()
        })

    window.bufferSlider.valueChanged['int'].connect(lambda i: MainWindow.set_num(i))
    thread.start()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()