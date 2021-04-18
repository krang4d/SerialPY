#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Serial Port Reader by Pavel Golovkin, aka pgg (14.04.2021).
# Feel free to use. No warranty
# Version 1.1.0

from PyQt5.QtCore import pyqtSignal, QObject, QTimer, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication

from pyqtgraph import PlotWidget
from uart_over_usb import UDevice, _FileLoggerCallback
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint


# Объект, который будет перенесён в другой поток для выполнения кода
class DeviceHandler(QObject):
    #running = False
    newTextAndColor = pyqtSignal(list)
    device = UDevice(baudrate=9200, timeout=3, logger=_FileLoggerCallback())

    # метод, который будет выполнять алгоритм в другом потоке
    def run(self):
        while True:
            data = self.device.readline()
            # посылаем сигнал из второго потока в GUI поток
            self.newTextAndColor.emit(data)
            QThread.msleep(100)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        # self.timer = QTimer()
        # self.timer.setInterval(50)
        # self.timer.timeout.connect(self.update_plot_data)
        # self.timer.start()

        # создадим поток
        self.thread = QThread()
        # создадим объект для выполнения кода в другом потоке
        self.DeviceHandler = DeviceHandler()
        # перенесём объект в другой поток
        self.DeviceHandler.moveToThread(self.thread)
        # после чего подключим все сигналы и слоты
        self.DeviceHandler.newTextAndColor.connect(self.update_plot_data)
        # подключим сигнал старта потока к методу run у объекта, который должен выполнять код в другом потоке
        self.thread.started.connect(self.DeviceHandler.run)
        # запустим поток
        self.thread.start()

    def update_plot_data(self, data):
        print(data)
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first 
        self.y.append( data[4])  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = MainWindow()

    w.show()
    sys.exit(app.exec_())