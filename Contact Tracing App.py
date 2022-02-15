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


import cv2
import datetime as datetime 
import os as access 

def webcam ():
    webcam = cv2.VideoCapture (0)
    qr_detector = cv2.QRCodeDetector ()
    while True:
        _, img = webcam.read ()
        data, one, _ = qr_detector.detectAndDecode (img)
        cv2.imshow ('QR Code Scanner', img)
        if data:
            contacttracing = data
            datatotextfile (contacttracing)
            break
        if cv2.waitKey (1) == ord('q'):
            print ('No QR code has been scanned.')
            break
    
def datatotextfile (contact_tracing):
        current_date_time = datetime.now ()
        file = open ("Contact Tracing.txt", 'w+')
        file.write (f'{contact_tracing} \n')
        file.write (' \n')
        file.write ('QR Code scanned in: \n')
        file.write (f'     Date: {current_date_time.strftime ("%B %d, %Y")} \n')
        file.write (f'     Time: {current_date_time.strftime ("%H:%M")}')
        file.close ()
        
