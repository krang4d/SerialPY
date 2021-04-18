#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import serial
import serial.tools.list_ports as prtlst
from abc import ABCMeta, abstractmethod
from ui.MainWindow import Ui_MainWindow
from ui.AboutForm import Ui_AboutForm

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
    def open():
        ...
    @abstractmethod
    def get_devs():
        ...

class UDevice(IDevice):
    _port = None
    _name = None

    def __init__(self):
        ...

    def __del__(self):
        if UDevice._port is not None:
            print('Closed Port!')
            UDevice._port.close()

    def open(self, dev: str, baudrate: int, timeout: int):
        try:
            UDevice._port = serial.Serial(port=dev, baudrate=baudrate, timeout=timeout)
        except Exception as e:
           print(e.strerror)
           exit()


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
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.aboutForm = AboutForm()

        self.graphWidget1 = pg.PlotWidget()
        self.graphWidget2 = pg.PlotWidget()

        self.graphWidget1.setBackground((100,50,255,0))
        self.graphWidget2.setBackground((100,50,255,0))

        # Create a QHBoxLayout instance
        graphsLayout = QtWidgets.QVBoxLayout()
        graphsLayout.addWidget(self.graphWidget1)
        graphsLayout.addWidget(self.graphWidget2)

        self.widget.setLayout(graphsLayout)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature1 = [30,32,34,32,33,31,29,32,35,45]
        temperature2 = [30,32,34,32,33,31,29,32,35,45]
        temperature3 = [1,1,1,1,2,2,2,3,3,3]

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
        self.graphWidget1.plot(hour, temperature1, name="Sensor1", symbolBrush='r', pen=pen)
        self.graphWidget2.plot(hour, temperature2, name="Sensor3", symbolBrush='b', pen=pen)
        self.graphWidget2.plot(hour, temperature3, name="Sensor4", symbolBrush='y', pen=pen)

        self.initUI()

    def initUI(self):
        # self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self._presed_ok)
        # self.buttonBox.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(dev.set_dev)
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    device = UDevice()
    window.set_dev(device.get_devs())
    print(device.get_devs())
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()