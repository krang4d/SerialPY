#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import serial
import serial.tools.list_ports as prtlst
import io

import numpy as np
import matplotlib.pyplot as plt

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

class Uart_ploter():
    def __init__(self):
        num =800
        self._x1 = np.zeros(num)
        self._y1 = np.zeros(num)
        self._x2 = np.zeros(num)
        self._y2 = np.zeros(num)
        self._x3 = np.zeros(num)
        self._y3 = np.zeros(num)
        self._x4 = np.zeros(num)
        self._y4 = np.zeros(num)
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
            self._y1 = np.delete(self._y1, 0)
            self._x1 = np.delete(self._x1, 0)
            self._y1 = np.append(self._y1, Y[0])
            self._x1 = np.append(self._x1, next(self.iter))

            self._y2 = np.delete(self._y2, 0)
            self._x2 = np.delete(self._x2, 0)
            self._y2 = np.append(self._y2, Y[1])
            self._x2 = np.append(self._x2, next(self.iter))

            self._y3 = np.delete(self._y3, 0)
            self._x3 = np.delete(self._x3, 0)
            self._y3 = np.append(self._y3, Y[2])
            self._x3 = np.append(self._x3, next(self.iter))

            self.line1.set_xdata(self._x1)
            self.line1.set_ydata(self._y1)
            self.line2.set_xdata(self._x2)
            self.line2.set_ydata(self._y2)
            self.line3.set_xdata(self._x3)
            self.line3.set_ydata(self._y3)

            dx, dy = ( .5, .5 )
            self.ax1.set_ylim([np.min(self._y1)-dy, np.max(self._y1)+dy])
            self.ax1.set_xlim([np.min(self._x1)-dx, np.max(self._x1)+dx])
            self.ax2.set_ylim([np.min(self._y2)-dy, np.max(self._y2)+dy])
            self.ax2.set_xlim([np.min(self._x2)-dx, np.max(self._x2)+dx])
            self.ax3.set_ylim([np.min(self._y3)-dy, np.max(self._y3)+dy])
            self.ax3.set_xlim([np.min(self._x3)-dx, np.max(self._x3)+dx])

            self.figure.canvas.draw()
            self.figure.canvas.flush_events()
            #time.sleep(0.1)
        except Exception as e:
            print(e)
            exit()

# Define UART settings
baudrate = 115200
timeout = 3

if __name__ == "__main__":

    devices = list()
    pts= prtlst.comports()
    i=0
    for pt in pts:
        #print(pt)
        if 'USB'or 'ACM'  in pt[1]:
            devices.append(pt)
            print('%d. %s %s'%(i, pt[1], pt[0]))
            i+=1

    if len(devices)==0:
            print('No USB device found.')
            exit()
    elif len(devices)==1:
            x=0
    elif len(devices)>1:
        x=int(input('Input the device number: '))

    uplot = Uart_ploter()

    try:
        with serial.Serial(port=devices[x][0], baudrate=baudrate, timeout=timeout) as port:
            while port.is_open:
                read_data = port.readline()
                if read_data == b'': print('timeout %.1fs'%timeout)
                data = [ float(x) for x in read_data.decode('utf-8')[:-2].split(';') ]
                uplot.update(data)
                with open("uart.log", 'a') as f:
                    f.write('%s %.3f;%.3f;%.3f\n'%(datetime.now(), data[0], data[1], data[2]))

    except serial.SerialException as e:
        print('error open serial port: ' + str(e))
        exit()

    except serial.SerialTimeoutException:
        print('Timeout Exception')

    finally:
        port.close()
