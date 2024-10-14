#Super simple demo using glasses detector demo, take an input frame from webcam and parse via https://github.com/mantasu/glasses-detector library to determine if user is wearing glasses or not.

import cv2
from glasses_detector import GlassesClassifier, GlassesDetector

camera_id = 0
delay = 1
cap = cv2.VideoCapture(camera_id,cv2.CAP_DSHOW)


def frame_capture():
    result, image = cap.read()
    if result:
            cv2.imshow("Captured Frame", image)
            cv2.imwrite("ExampleFrame.png", image)
            cv2.waitKey(0)
            cv2.destroyWindow("Captured Frame")

    else:
        print('Error has occured')

img = "ExampleFrame.png"
def glasses_detection(imgpath):
    classifier = GlassesClassifier()
    if classifier.process_file(
        input_path=imgpath,     # can be a list of paths
        format={True: "1", False: "0"},   # similar to format="int"
        show=True,                        # to print the prediction
    ) == "1":
        print("Glasses Present")
    else:
        print("No Glasses")

frame_capture()
glasses_detection(img)
