#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import serial
import serial.tools.list_ports as prtlst
import io

import numpy as np
import matplotlib.pyplot as plt

from abc import ABCMeta, abstractmethod
from datetime import datetime
# Create an Iterator for scale X on plot
class NumbersIterator:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

class Plotter:
    _iter = iter(NumbersIterator())
    _stop = True

    _num = 100 # число отсчетов по оси Х на графиках

    @staticmethod
    def is_open() -> bool:
        return Plotter._stop

    def update(line: str):
        print(line)

    def _on_close(self, event):
        print('Closed Figure!')
        Plotter._stop = False

class MatPlotter(Plotter):
    _figure = None
    _ax1, _ax2 = None, None
    _line1, _line2, _line3 = None, None, None
    _x1 = np.zeros(Plotter._num, dtype=int)
    _y1 = np.zeros(Plotter._num)
    _x2 = np.zeros(Plotter._num, dtype=int)
    _y2 = np.zeros(Plotter._num)
    _x3 = np.zeros(Plotter._num, dtype=int)
    _y3 = np.zeros(Plotter._num)
    _x4 = np.zeros(Plotter._num, dtype=int)
    _y4 = np.zeros(Plotter._num)

    def __init__(self, title=""):
        #turns on the interactive mode
        plt.ion()

        self._figure, (self._ax1, self._ax2 ) = plt.subplots( 1, 2, figsize=(8,4) )

        self._figure.canvas.set_window_title("Dynamic serial port")
        self._figure.suptitle(title,fontsize=14)

        self._figure.canvas.mpl_connect('close_event', self._on_close)

        self._ax1.grid()
        self._ax2.grid()

        self._line1, = self._ax1.plot(self._x1, self._y1)
        self._line2, = self._ax2.plot(self._x2, self._y2)
        self._line3, = self._ax2.plot(self._x3, self._y3)

        self._line1.set_label('RPM')
        self._line2.set_label('T(C)')
        self._line3.set_label('ADC')

        self._ax1.legend()
        self._ax2.legend()

        self._ax1.set_xlabel('Step',fontsize=12)
        self._ax1.set_ylabel('RPM',fontsize=12)

        self._ax2.set_xlabel('Step',fontsize=12)
        self._ax2.set_ylabel('ADC, T (C)',fontsize=12)
        plt.tight_layout()

    def update(self, Y):
        try:
            index = next(Plotter._iter)
            self._y1 = np.delete(self._y1, 0)
            self._x1 = np.delete(self._x1, 0)
            self._y1 = np.append(self._y1, Y[0])
            self._x1 = np.append(self._x1, index)

            self._y2 = np.delete(self._y2, 0)
            self._x2 = np.delete(self._x2, 0)
            self._y2 = np.append(self._y2, Y[2])
            self._x2 = np.append(self._x2, index)

            self._y3 = np.delete(self._y3, 0)
            self._x3 = np.delete(self._x3, 0)
            self._y3 = np.append(self._y3, Y[3])
            self._x3 = np.append(self._x3, index)

            self._line1.set_xdata(self._x1)
            self._line1.set_ydata(self._y1)
            self._line2.set_xdata(self._x2)
            self._line2.set_ydata(self._y2)
            self._line3.set_xdata(self._x3)
            self._line3.set_ydata(self._y3)


            dy1 = (np.max(self._y1) - np.min(self._y1))/100
            minimum = np.min(np.concatenate((self._y2, self._y3), axis=None ))
            maximum = np.max(np.concatenate((self._y2, self._y3), axis=None ))
            dy2 = (maximum - minimum)/100

            self._ax1.set_ylim([np.min(self._y1)-dy1, np.max(self._y1)+dy1])
            self._ax1.set_xlim([self._x1[0], self._x1[Plotter._num-1]])
            self._ax2.set_ylim([minimum-dy2, maximum]+dy2)
            self._ax2.set_xlim([self._x2[0], self._x2[Plotter._num-1]])

            self._figure.canvas.draw()
            self._figure.canvas.flush_events()
            Plotter.update(Y)
            plt.pause(0.005)

        except Exception as e:
           print(e)
           exit()

class _LoggerCallback(metaclass=ABCMeta):
    @abstractmethod
    def __call__():
        ...

class _FileLoggerCallback(_LoggerCallback):
    _file_name = "uart.log" # имя лог файла

    def __call__(self, data: str):
        with open(self._file_name, 'a') as f:
            f.write('%s %.3f;%.3f;%.3f\n'%(datetime.now(), data[0], data[1], data[2]))

class UDevice:
    _port = None
    _logger = None
    _name = None

    def __init__(self, baudrate: int, timeout: int, logger : _LoggerCallback):
        UDevice._logger = logger
        try:
            UDevice._port = serial.Serial(port=self._get_device(), baudrate=baudrate, timeout=timeout)
        except Exception as e:
           print(e.strerror)
           exit()

    def __del__(self):
        if UDevice._port is not None:
            print('Closed Port!')
            UDevice._port.close()

    def _get_device(self):
        devices = list()
        pts= prtlst.comports()

        for index, pt in enumerate(pts):
            #print(pt)
            if 'USB' or 'ACM'  in pt[1]:
                devices.append(pt)
                print('%d. %s %s'%(index, pt[0], pt[1]))

        if len(devices)==0:
            print('No USB device found.')
            exit()

        elif len(devices)==1:
            x=0
        elif len(devices)>1:
            x=int(input('Input the device number: '))

        self._name = devices[x][0]
        return self._name

    def readline(self) ->str:
        data = UDevice._port.readline()
        if data == b'': 
            print('Device did not respond, timeout %.1fs'%timeout)
            exit()
        line = [ float(x) for x in data.decode('utf-8')[:-2].split(';') ]
        self._logger(line)
        return line

if __name__ == "__main__":

    # Define UART settings
    baudrate = 9200
    timeout = 3

    device = UDevice(baudrate, timeout, _FileLoggerCallback())
    chp = MatPlotter(device._name)

    while(chp.is_open()):
        line = device.readline()
        line[2] = line[2]/16
        chp.update(line)
    del device

    # except serial.SerialException as e:
    #     print('error open serial port: ' + str(e))
    #     exit()

    # except serial.SerialTimeoutException:
    #     print('Timeout Exception')

    # finally:
    #     port.close()
