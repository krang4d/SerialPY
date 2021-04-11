#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import serial
import serial.tools.list_ports as prtlst
import io

import numpy as np
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod
from datetime import datetime
# Create an Iterator for scale X on plot
class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

class Plotter(ABC):

    _figure = None
    _ax1, _ax2, _ax3 = None, None, None

    @abstractmethod
    def update(line: str):
        ...

class MatPlotter(Plotter):
    def __init__(self):
        self.num = 100
        self._x1 = np.zeros(self.num, dtype=int)
        self._y1 = np.zeros(self.num)
        self._x2 = np.zeros(self.num, dtype=int)
        self._y2 = np.zeros(self.num)
        self._x3 = np.zeros(self.num, dtype=int)
        self._y3 = np.zeros(self.num)
        self._x4 = np.zeros(self.num, dtype=int)
        self._y4 = np.zeros(self.num)
        self.iter = iter(Numbers())
        #turns on the interactive mode
        plt.ion()
        
        self.figure, (self.ax1, self.ax2, self.ax3 ) = plt.subplots( 1, 3, figsize=(15,5) )
        self.figure.suptitle("Dynamic UART",fontsize=14)

        self.ax1.grid()
        self.ax2.grid()
        self.ax3.grid()

        self.line1, = self.ax1.plot(self._x1, self._y1)
        self.line2, = self.ax2.plot(self._x2, self._y2)
        self.line3, = self.ax3.plot(self._x3, self._y3)

        self.ax1.set_xlabel('Time, sec',fontsize=18)
        self.ax1.set_ylabel('RPM',fontsize=18)

        self.ax2.set_xlabel('Temperature, C',fontsize=18)
        self.ax2.set_ylabel('ADC',fontsize=18)

        self.ax3.set_xlabel('Time, sec',fontsize=18)
        self.ax3.set_ylabel('ADC/50, T (C)',fontsize=18)

    def update(self, Y):
        try:
            index = next(self.iter)
            self._y1 = np.delete(self._y1, 0)
            self._x1 = np.delete(self._x1, 0)
            self._y1 = np.append(self._y1, Y[0])
            self._x1 = np.append(self._x1, index)

            self._y2 = np.delete(self._y2, 0)
            self._x2 = np.delete(self._x2, 0)
            self._y2 = np.append(self._y2, Y[1])
            self._x2 = np.append(self._x2, index)

            self._y3 = np.delete(self._y3, 0)
            self._x3 = np.delete(self._x3, 0)
            self._y3 = np.append(self._y3, Y[2])
            self._x3 = np.append(self._x3, index)

            self.line1.set_xdata(self._x1)
            self.line1.set_ydata(self._y1)
            self.line2.set_xdata(self._x2)
            self.line2.set_ydata(self._y2)
            self.line3.set_xdata(self._x3)
            self.line3.set_ydata(self._y3)

            dy = .5
            self.ax1.set_ylim([np.min(self._y1)-dy, np.max(self._y1)+dy])
            self.ax1.set_xlim([self._x1[0], self._x1[self.num-1]])
            self.ax2.set_ylim([np.min(self._y2)-dy, np.max(self._y2)+dy])
            self.ax2.set_xlim([self._x2[0], self._x2[self.num-1]])
            self.ax3.set_ylim([np.min(self._y3)-dy, np.max(self._y3)+dy])
            self.ax3.set_xlim([self._x3[0], self._x3[self.num-1]])

            self.figure.canvas.draw()
            plt.pause(0.001)
            self.figure.canvas.flush_events()
            #time.sleep(0.1)
        except Exception as e:
            print(e)
            exit()

class DrawPlotter(Plotter):

    def update(self, line):
        print(line)

class Logger(ABC):
    @abstractmethod
    def addLine():
        ...

class FileLogger(Logger):
    def addLine(self, data: str):
        with open("uart.log", 'a') as f:
            f.write('%s %.3f;%.3f;%.3f\n'%(datetime.now(), data[0], data[1], data[2]))

class UDevice:
    _port = None
    #_logger = None
    def __init__(self, baudrate: int, timeout: int, logger: Logger):
        UDevice._logger = logger
        UDevice._port = serial.Serial(port=self._get_device(), baudrate=baudrate, timeout=timeout)

    def __del__(self):
        print("UDevice.__del__")
        if UDevice._port is not None:
            print('close port')
            UDevice._port.close()

    def _get_device(self):
        devices = list()
        pts= prtlst.comports()

        for index, pt in enumerate(pts):
            #print(pt)
            if 'USB' or 'ACM'  in pt[1]:
                devices.append(pt)
                print('%d. %s %s'%(index, pt[1], pt[0]))

        if len(devices)==0:
            print('No USB device found.')
            exit()

        elif len(devices)==1:
            x=0
        elif len(devices)>1:
            x=int(input('Input the device number: '))

        return devices[x][0]

    def readline(self) ->str:
        data = UDevice._port.readline()
        if data == b'': print('timeout %.1fs'%timeout)
        line = [ float(x) for x in data.decode('utf-8')[:-2].split(';') ]
        self._logger.addLine(line)
        return line

if __name__ == "__main__":

    # Define UART settings
    baudrate = 9200
    timeout = 3
    chp = MatPlotter()

    device = UDevice(baudrate, timeout, FileLogger())
    while(True):
        line = device.readline()
        print(line)
        chp.update(line)
    del device


    # except serial.SerialException as e:
    #     print('error open serial port: ' + str(e))
    #     exit()

    # except serial.SerialTimeoutException:
    #     print('Timeout Exception')

    # finally:
    #     port.close()
