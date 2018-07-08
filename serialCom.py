
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import threading
import time

serCom = serial.Serial('/dev/ttyAMA0', 115200, timeout = 1 )

class serialRead():

    def __init__(self):
        self.threadRead = threading.Thread( target = self.target )
        self.threadRead.start()

    def target(self):
        while True:
            if( serCom.inWaiting() > 0 ):
                strC = serCom.read( serCom.inWaiting() )
                print( "[%s]" % strC )
                if( strC == "IP addre"):
                    serCom.write( "192.168.1.23" )
                if( strC == "Date" ):
                    serCom.write("2018 JULY 07")
                if( strC == "Time"):
                    serCom.write("Message from my PC")

    def stop(self):
        self.stop_event.set()

def main():
    print( "Start reading..." , serCom.portstr )
    while True:
        try:
            strA = raw_input("send: ")
            serCom.write( strA )
            print( "[%s] sent" % strA )
        except:
            threadRead.stop()
            serCom.close()
            exit()

if __name__ == '__main__':
    threadRead = serialRead()
    main()
