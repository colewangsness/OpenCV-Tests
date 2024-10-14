#This example is similar to the picture QR demo, except it displays video content.

# importing libraries
import cv2
import tkinter as tk

#Define User Screen Size & Get Size
win = tk.Tk()
screen_X = win.winfo_screenwidth()
screen_Y = win.winfo_screenheight()

#Define File Paths
path = 'FILE PATH TO MP4 CONTENT'
border_path = 'FILE PATH TO BACKGROUND IMAGE'

video = cv2.imread(path)
border = cv2.imread(border_path)
border_window = 'border'

#Create Fullscreen Background (OL Pantone 540c)
cv2.namedWindow(border_window,cv2.WINDOW_NORMAL)
cv2.setWindowProperty(border_window,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
border_copy = cv2.copyMakeBorder(border,50,50,50,50,cv2.BORDER_REFLECT101)
cv2.imshow(border_window,border_copy)

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(path)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video file")

    # Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame', frame)


        # Press Q on keyboard to exit
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
