import serial
import time
from audioPlay import playAudio
from downloadSong import downloadSong
from interenetCheck import connect
if __name__ == '__main__':
    connected = False;
    while connected == False:# loop to check once there is a usb cable plugged in and connected      
        try:
            ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
            connected = True
        except:
            try:
                ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1) #if replug the usb cable it will switch to USB1 and if replug again it will gp back to USB0
                connected = True
            except:
                print("no usb cable")
    ser.flush()
#     playAudio("1","Flying")
#     print("Play" == 'Play')
    while(1):
        messamay=""
        try:
            if (ser.inWaiting()>0):
                line = ser.readline().decode('utf-8').rstrip()
                messageArray= line.split(",")
                print(messageArray)
                playBool = messageArray[0].find('Play')==0
                downloadBool = messageArray[0].find('Download')==0
                endBool = messageArray[0].find('End')==0
                checkInterenet = messageArray[0].find('CheckInterenet')==0
                if(playBool):
                      playAudio(messageArray[1],messageArray[2])
                elif (downloadBool):
                    if(connect()):
                        ser.write(b"Interenet");
                        downloadSong(int(messageArray[1]),messageArray[2])
                    elif(connect() == False):
                        print("No internet")
                        ser.write(b"No internet from pi");
                elif (endBool):
                    ser.write(b"Done")
                    line = ser.readline().decode('utf-8').rstrip()
                    print(line)
                elif(checkInterenet):
                    if(connect()):
                        ser.write(b"interenetWork")
                    else:
                        ser.write(b"noInternet")
                    print('interenetWork' if connect() else 'noInternet')
            
        except:
            print("error")
        time.sleep(1)