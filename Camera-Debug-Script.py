#https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html

import cv2
backend = cv2.videoio_registry.getBackends()
cameraback = cv2.videoio_registry.getCameraBackends()
runtime = cv2.videoio_registry.getBackendName(cv2.CAP_DSHOW) #Used for Windows

print(backend)
print(cameraback)
