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
class NumbersIterator:
    def __iter__(self):
        self.a = 1
        return self

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

class IDevice(metaclass=ABCMeta):
    @abstractmethod
    def open() -> None:
        ...
    @abstractmethod
    def close() -> None:
        ...
    @abstractmethod
    def get_devs() -> list:
        ...
    @abstractmethod
    def readline() -> str:
        ...

class UDevice(IDevice):
    _dev = None
    _port = None

    def __init__(self):
        ...
    def __del__(self):
        self.close()

    def open(self, dev: str, baudrate: int, timeout: int):
        try:
            if self._dev is None:
                UDevice._port = serial.Serial(port=dev, baudrate=baudrate, timeout=timeout)
                print('Open Port '+ dev)
                self._dev = dev
            else: print('The Port '+ dev + ' has been open')
        except Exception as e:
            print(e)
            exit()

    def close(self):
        if UDevice._port is not None:
            print('Closed Port '+ self._dev)
            UDevice._port.close()
            self._dev = None

    def get_devs(self):
        devices = list()
        pts= prtlst.comports()
        print(pts)
        for index, pt in enumerate(pts):
            #print(pt)
            if 'USB' or 'ACM'  in pt[1]:
                devices.append(pt[0])
                print('%d. %s %s'%(index, pt[0], pt[1]))

        if len(devices)==0:
            print('No USB device found.')
            devices.append('no device')

        return devices

    @_FileLogger
    def readline(self) ->str:
        data = UDevice._port.readline()
        if data == b'': 
            print('Device did not respond, timeout %.1fs'%timeout)
            exit()
        line = [ int(x) for x in data.decode('utf-8')[:-2].split(';') ]
        return line

class AboutForm(QtWidgets.QDialog, Ui_AboutForm):
    def __init__(self, *args, obj=None, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        self.setupUi(self)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    _num = 100

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.aboutForm = AboutForm()

        self._iter = iter(NumbersIterator())
        self._y1 = np.zeros(self._num)
        self._y2 = np.zeros(self._num)
        self._y3 = np.zeros(self._num)
        self._x = np.zeros(self._num, dtype=int)

        self.graphWidget1 = pg.PlotWidget()
        self.graphWidget2 = pg.PlotWidget()

        self.graphWidget1.setBackground((100,50,255,0))
        self.graphWidget2.setBackground((100,50,255,0))

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
        self.graphWidget1.setXRange(0, 10, padding=0)
        self.graphWidget2.setXRange(0, 10, padding=0)
        self.graphWidget1.setYRange(20, 55, padding=0)
        self.graphWidget2.setYRange(20, 55, padding=0)

        # plot data: x, y values
        pen = pg.mkPen(color=(0, 0, 0), width=2, style=QtCore.Qt.SolidLine)
        self.data_line1 = self.graphWidget1.plot(self._x, self._y1, name="Sensor1", symbolBrush='r', pen=pen)
        self.data_line2 = self.graphWidget2.plot(self._x, self._y2, name="Sensor3", symbolBrush='b', pen=pen)
        self.data_line3 = self.graphWidget2.plot(self._x, self._y3, name="Sensor4", symbolBrush='y', pen=pen)

        self.initUI()

    def initUI(self):
        # self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self._presed_ok)
        # self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(dev.set_dev)
        #self.open_pushButton.clicked.connect(lambda: self.statusbar.showMessage('open_pushButton'))
        self.close_pushButton.clicked.connect(lambda: self.statusbar.showMessage('close_pushButton'))
        self.actionAbout.triggered.connect(self.aboutForm.show)
        pass

    def _plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

    def _presed_ok(self):
        self.statusbar.showMessage("oK!")

    def set_dev(self, devs):
        for dev in devs:
            self.serial_comboBox.addItem(dev)

    def update_plot_data(self, data):
        data[2] = data[2]/16
        print(data)
        self._x = self._x[1:]  # Remove the first y element.
        self._x.append(self._x[-1] + 1)  # Add a new value 1 higher than the last.

        self._y1 = self._y1[1:]  # Remove the first 
        self._y1.append( data[0])  # Add a new value.

        self._y2 = self._y2[1:]  # Remove the first 
        self._y2.append( data[2])  # Add a new value.

        self._y3 = self._y3[1:]  # Remove the first 
        self._y3.append( data[3])  # Add a new value.

        self.data_line1.setData(self._x, self._y1)  # Update the data.
        self.data_line2.setData(self._x, self._y2)  # Update the data.
        self.data_line3.setData(self._x, self._y3)  # Update the data.

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    device = UDevice()
    window.set_dev(device.get_devs())

    window.open_pushButton.clicked.connect(
        lambda: { device.open(window.serial_comboBox.currentText(), int(window.baudrate_comboBox.currentText()), 3), print(device.readline()) } )
        # lambda: window.statusbar.showMessage(
        # window.baudrate_comboBox.currentText() + window.serial_comboBox.currentText()))
    window.close_pushButton.clicked.connect(lambda: device.close())

    print(device.get_devs())
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()