# Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
#	- Search how to generate QRCode
#	- Search how to read QRCode using webcam
#	- Search how to create and write to text file
#	- Your source code should be in github before Feb 19
#	- Create a demo of your program (1-2 min) and send it directly to my messenger.


import cv2 #imported cv2 in order to access the webcam
from pyzbar.pyzbar import decode
from datetime import datetime #imported datetime in order to get the date and time on when did the user scanned the qr code
import os as access #imported access so that text file can be opened in its default program (Notepad)

def QR_code ():
    webcam = cv2.VideoCapture (0)
    qr_detector = cv2.QRCodeDetector ()
    while True:
        _, img = webcam.read ()
        for qrcode in decode (img):
            if qrcode:
                QR_data = qrcode.data.decode ('utf-8')
                data_to_textfile (QR_data)
                break
        cv2.imshow ('QR Code Scanner', img) #opens webcam in new window
        if cv2.waitKey (1) == ord('q'): #pressing q from keyboard will close the webcam
            cv2.destroyAllWindows
            break
    
def data_to_textfile (QR_data):
        current_date_time = datetime.now () #getting the date and time as to when the QR code was scanned
        file = open ("Contact Tracing Information.txt", 'w') #creates new file 
        file.write (f'{QR_data} \n') #data read in QR code will be written in the text file
        file.write ('\n') #creates a new line (acts as the spacing between the last line from QR code and first line for the date and time part)
        file.write ('QR Code scanned in: \n')
        file.write (f'     Date: {current_date_time.strftime ("%B %d, %Y")} \n') #format of date will be in "month" "day", "year" (e.g. February 18, 2022)
        file.write (f'     Time: {current_date_time.strftime ("%I:%M %p")}') #format of time will be in hours:minutes and is stated in 12-hour format instead of 24-hour format (e.g. 12:22 PM)
        file.close ()
        access.startfile ("Contact Tracing Information.txt") #after creating the file, text file will start/open in Notepad app

QR_code () #this will execute the whole program

