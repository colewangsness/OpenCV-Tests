#The following demo uses OpenCV to dynamically display content as new QR Codes are scanned. Images are centered using Tkinter. QR Codes should match image file names. Line 47 will create file extension type.
#Depending on environment, camera, etc. QR Codes should be at least 2"x2", Ideal results were performed with codes 4"x4"

import cv2
import tkinter as tk

#Define User Screen Size & Get Size
win = tk.Tk()
screen_X = win.winfo_screenwidth()
screen_Y = win.winfo_screenheight()
center_x = screen_X/2
center_y = screen_Y/2

#Define File Path
path = 'FILE PATH TO IMAGES'
border_path = 'FILE PATH TO USE SOLID COLOR BACKGROUND IMAGE, PNG OR JPG OK'
camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'

#Generate Background Image
border = cv2.imread(border_path)
border_window = 'border'
cv2.namedWindow(border_window,cv2.WINDOW_NORMAL)
cv2.setWindowProperty(border_window,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
border_copy = cv2.copyMakeBorder(border,50,50,50,50,cv2.BORDER_REFLECT101)
cv2.imshow(border_window,border_copy)

#Initialize Webcam and QR Detection

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id,cv2.CAP_DSHOW) ##CAP_DSHOW Flag required for Windows, Remove for Linux

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)

        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    #print(s) #debug only
                    color = (0, 255, 0)

                    #generates file path
                    editedpath = path + s +'.jpg'

                    #Stores Current Value
                    storedpath = s

                    #Reading File
                    aa = cv2.imread(editedpath, -1)

                    #Get Current Image Dimensions
                    image_height = aa.shape[0]
                    image_width = aa.shape[1]

                    #Define Tuple for top_left coordinate, show and move window to center
                    top_left = ((center_x - (image_width / 2)), ((center_y - (image_height / 2))))
                    cv2.imshow('OnLogic', aa)
                    cv2.moveWindow('OnLogic', int(top_left[0]), int(top_left[1]))

                    #Destroys Window when value changes
                    if s != storedpath:
                        cv2.destroyWindow('OnLogic')
                else:
                    color = (0, 0, 255)
                    frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
       #Define Webcame Window, Set to always be on top, and display
        cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
        cv2.imshow(window_name, frame)
        cv2.moveWindow(window_name,0,0)
        #cv2.resizeWindow(window_name,200,200)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()


#Debug Code

#backend = cv2.videoio_registry.getBackends()
#cameraback = cv2.videoio_registry.getCameraBackends()
#runtime = cv2.videoio_registry.getBackendName(cv2.CAP_DSHOW)

#print(backend)
#print(cameraback)
