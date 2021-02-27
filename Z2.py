# https://habr.com/ru/company/edison/blog/480884/
# Графический интерфейс на Python за 5 минут

import PySimpleGUI as sg
import re
import hashlib

#**************

import numpy as np
import matplotlib.pyplot as plt

#********
import os, sys, fnmatch
import csv

 
mask = '*.log'

layout = [
    [sg.Text('File'), sg.InputText(), sg.FileBrowse(),
     sg.Checkbox('600 sec')],
    [sg.Output(size=(70, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('File open', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        file1 = isitago = None
        
#        print(values[0])
        
        if values[0]:
            file1 = re.findall('.+:\/.+\.+.', values[0])
            if not file1 and file1 is not None:
                print('Error: File path not valid.')
        else:
            print('Please choose files.')

#------
#        print (file1)
        print ('File: ', values[0])
        file2=values[0]
        
        with open (file2,'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        print('Total lines: ', line_count)



#**************

#***********************

        x=np.arange(line_count-7)
        y=np.arange(line_count-7)
        z=np.arange(line_count-7)
        
        v=np.arange(line_count-7)
        w=np.arange(line_count-7)


#***********************
        handle = open(file2, "r")
        data = handle.readlines() # read ALL the lines!
        print ('**********',file2)
        lc = 0
        while lc < line_count-8:
            lc=lc+1

# здесь мы будем расчленять строку с учетом отрезания начала и конца файла
            s=''
            q=['','','','','','','']

            j=0
            for char in data[lc+2]:
                if char==';':
                    q[j]=s
#        print (j,' = ', s,'***', q[j])
                    s=''
                    j=j+1
                else:
                    s=s + char
            q[j]=s

# конец расчленения

                
            x[lc]=float(q[5])
            y[lc]=float(q[2])
            v[lc]=6000000./float(q[1])
            w[lc]=6000000./float(q[0])       


#***********************

        fig, (ax1, ax2, ax3 ) = plt.subplots(
            nrows=1, ncols=3,
            figsize=(12, 5)
        )

        x[0]=x[1]
        y[0]=y[1]
        z[0]=z[1]

        ax1.set_xlabel('Time, sec')
        ax1.set_ylabel('RPM')
        ax1.plot(z,v)
        ax1.plot(z,w)

        ax2.set_xlabel('Temperature, C')
        ax2.set_ylabel('ADC')
        ax2.plot(y/16.0,x)

        ax3.set_xlabel('Time, sec')
        ax3.set_ylabel('ADC/50, T (C)')
        ax3.plot(z,y/16.0)
        ax3.plot(z,x*2/100.)

        plt.show()
#            top=0.88,
#            bottom=0.11,
#            left=0.045,
#            right=0.98,
#            hspace=0.2,
#            wspace=0.2)

