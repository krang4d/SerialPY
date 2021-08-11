#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Serial Port Reader with Qt interface by Pavel Golovkin, aka pgg (14.04.2021).
# Feel free to use. No warranty
# Version 1.0.3
'''
Установка и запуск
------------------

1. Установите Python3 (https://www.python.org/downloads/)
2. Далее установите небходимые пакеты командой:
    python -m pip install pyserial PyQt5
3. Запустите программу командой: python uart_over_usb.py
'''

import sys, os
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import pyqtgraph
import serial
import serial.tools.list_ports

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
"Version 1.1.10"))
        self.pushButton.setText(_translate("AboutForm", "Ok"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 854)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settingsGBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.baudrateLabel = QtWidgets.QLabel(self.settingsGBox)
        self.baudrateLabel.setObjectName("baudrateLabel")
        self.gridLayout.addWidget(self.baudrateLabel, 0, 2, 1, 1)
        self.serialLabel = QtWidgets.QLabel(self.settingsGBox)
        self.serialLabel.setObjectName("serialLabel")
        self.gridLayout.addWidget(self.serialLabel, 0, 0, 1, 1)
        self.serialCBox = QtWidgets.QComboBox(self.settingsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialCBox.sizePolicy().hasHeightForWidth())
        self.serialCBox.setSizePolicy(sizePolicy)
        self.serialCBox.setMinimumSize(QtCore.QSize(140, 0))
        self.serialCBox.setObjectName("serialCBox")
        self.gridLayout.addWidget(self.serialCBox, 0, 1, 1, 1)
        self.baudrateCBox = QtWidgets.QComboBox(self.settingsGBox)
        self.baudrateCBox.setObjectName("baudrateCBox")
        self.baudrateCBox.addItem("")
        self.baudrateCBox.addItem("")
        self.baudrateCBox.addItem("")
        self.baudrateCBox.addItem("")
        self.baudrateCBox.addItem("")
        self.gridLayout.addWidget(self.baudrateCBox, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.settingsGBox)
        self.graphsGBox = QtWidgets.QGroupBox(self.centralwidget)
        self.graphsGBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphsGBox.sizePolicy().hasHeightForWidth())
        self.graphsGBox.setSizePolicy(sizePolicy)
        self.graphsGBox.setTitle("")
        self.graphsGBox.setObjectName("graphsGBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.graphsGBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bufferSlider = QtWidgets.QSlider(self.graphsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bufferSlider.sizePolicy().hasHeightForWidth())
        self.bufferSlider.setSizePolicy(sizePolicy)
        self.bufferSlider.setMinimum(100)
        self.bufferSlider.setMaximum(1000)
        self.bufferSlider.setPageStep(100)
        self.bufferSlider.setProperty("value", 100)
        self.bufferSlider.setSliderPosition(100)
        self.bufferSlider.setOrientation(QtCore.Qt.Horizontal)
        self.bufferSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.bufferSlider.setTickInterval(100)
        self.bufferSlider.setObjectName("bufferSlider")
        self.gridLayout_3.addWidget(self.bufferSlider, 2, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.graphsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 3)
        self.bufferlabel = QtWidgets.QLabel(self.graphsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bufferlabel.sizePolicy().hasHeightForWidth())
        self.bufferlabel.setSizePolicy(sizePolicy)
        self.bufferlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bufferlabel.setObjectName("bufferlabel")
        self.gridLayout_3.addWidget(self.bufferlabel, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.graphsGBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.graphsGBox)
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
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setStyleSheet("color: red;")
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 22))
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
        self.baudrateLabel.setBuddy(self.baudrateCBox)
        self.serialLabel.setBuddy(self.serialCBox)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        self.bufferSlider.valueChanged['int'].connect(self.label.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.baudrateLabel.setText(_translate("MainWindow", "BaudRate (bps)"))
        self.serialLabel.setText(_translate("MainWindow", "Serial Port"))
        self.baudrateCBox.setItemText(0, _translate("MainWindow", "9600"))
        self.baudrateCBox.setItemText(1, _translate("MainWindow", "19200"))
        self.baudrateCBox.setItemText(2, _translate("MainWindow", "38400"))
        self.baudrateCBox.setItemText(3, _translate("MainWindow", "57600"))
        self.baudrateCBox.setItemText(4, _translate("MainWindow", "115200"))
        self.bufferlabel.setText(_translate("MainWindow", "Buffer"))
        self.label.setText(_translate("MainWindow", "100"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.cleanButton.setText(_translate("MainWindow", "Clean"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

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
        pts= serial.tools.list_ports.comports()
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
            else: line = [ float(x) for x in data.decode('utf-8')[:-2].split(';') ]
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
    ''' Oкно o программe

.. figure:: ./png/about_window.png
    :scale: 70 %
    :align: center
    '''
    def __init__(self, *args, obj=None, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        self.setupUi(self)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ''' Основное окно программы

.. figure:: ./png/main_window.png
    :scale: 70 %
    :align: center
    '''

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

        self.graphWidget1 = pyqtgraph.PlotWidget()
        self.graphWidget2 = pyqtgraph.PlotWidget()

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
        pen = pyqtgraph.mkPen(color=(0, 180, 0), width=2, style=QtCore.Qt.SolidLine)
        self._line1 = self.graphWidget1.plot(self._x, self._y1, name='RPM', symbolBrush=(0, 180, 0), symbolSize=6, pen=pen)
        pen = pyqtgraph.mkPen(color='b', width=2, style=QtCore.Qt.SolidLine)
        self._line2 = self.graphWidget2.plot(self._x, self._y2, name='T(C)/16', symbolBrush='b', symbolSize=6, pen=pen)
        pen = pyqtgraph.mkPen(color=(196, 160, 0), width=2, style=QtCore.Qt.SolidLine)
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

            # data[2] = data[2]/16
            self._x.append(next(self._index)) #self._x[-1] + 1)   # Add a new value 1 higher than the last.
            self._y1.append( data[0])   # Add a new value.
            self._y2.append( data[1])   # Add a new value.
            self._y3.append( data[2])   # Add a new value.

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