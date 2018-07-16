#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import threading
import datetime
import time
import wiringpi as pi


serCom = serial.Serial('/dev/ttyAMA0', 115200, timeout = 1 )

class serialRead():

    def __init__(self):
        self.threadRead = threading.Thread( target = self.target )
        self.threadRead.start()

    def target(self):
        flag=True
        while flag:
            if( serCom.inWaiting() > 0 ):
                strC = serCom.read( serCom.inWaiting() )
                print( "[%s]" % strC )
                if( strC == "Sonic"):
                    num = 0
                    while num < 10:
                        num = num + 1
                        strDistance = mesure()
                        serCom.write( strDistance )
                        print( strDistance )
                        time.sleep(1.0)

                if( strC == "Date" ):
                    objDate = datetime.date.today()
                    strDate = objDate.strftime("%Y/%m/%d")
                    serCom.write(strDate)
                    print(strDate)

                if( strC == "Time"):
                    objTime = datetime.datetime.now()
                    strTime = objTime.strftime("%H:%M:%S")
                    serCom.write(strTime)
                    print(strTime)

    def quit(self):
        flag=False

def main():
    print( "Start reading..." , serCom.portstr )
    while True:
        try:
            strA = raw_input("send: ")
            serCom.write( strA )
            print( "[%s] sent" % strA )
        except:
            serCom.close()
            threadRead.quit()
            exit()

def sonicInit():
    global TRIG_PIN
    global ECHO_PIN
    global pi
    TRIG_PIN = 18
    ECHO_PIN = 17
    pi.wiringPiSetupGpio()
    pi.pinMode( TRIG_PIN, pi.OUTPUT )
    pi.pinMode( ECHO_PIN, pi.INPUT )
    pi.digitalWrite( TRIG_PIN, pi.LOW )

def mesure():
    pi.digitalWrite( TRIG_PIN, pi.HIGH )
    time.sleep(0.00001)
    pi.digitalWrite( TRIG_PIN, pi.LOW )
    while ( pi.digitalRead( ECHO_PIN ) == pi.LOW ):
        sigoff = time.time()
    while ( pi.digitalRead( ECHO_PIN ) == 1 ):
        sigon = time.time()
    strTemp = str( round((( sigon - sigoff ) * 34000) / 2, 5 )) + "cm"
    time.sleep(1.0)
    return ( strTemp )

if __name__ == '__main__':
    sonicInit()
    threadRead = serialRead()
    main()

