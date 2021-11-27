import time
import Adafruit_CharLCD as LCD
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import RPi.GPIO as GPIO

import sys
from PyQt5.uic import loadUiType



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) #led connection

lcd_rs=7
lcd_en=8
lcd_d4=25
lcd_d5=24
lcd_d6=23
lcd_d7=18
lcd_backlight=2
lcd_columns=16
lcd_rows=2

lcd=LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


ui,_=loadUiType('LED_CONTROL.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.label_2.hide()
        self.Handle_Buttons()
        
        
    
    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.led_on)
        self.pushButton_2.clicked.connect(self.led_off)
    
         
    
    def led_off(self):
        self.label_2.setText('LED OFF')
        self.label_2.show()
        self.label_2.setStyleSheet("color:red")
        lcd.clear()
        GPIO.output(17, GPIO.LOW)
        lcd.message('LED Off!!')
        
    def led_on(self):
        self.label_2.setText('LED ON')
        self.label_2.show()
        self.label_2.setStyleSheet("color:green")
        lcd.clear()
        GPIO.output(17, GPIO.HIGH)
        lcd.message('LED On!!')
    
def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec()
    
if __name__=='__main__':
    main()



