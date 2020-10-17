import numpy as np
import cv2

class CameraStream:

    def __init__(self, camid: int):
        self.__cam = camid
        self.vcap = cv2.VideoCapture(self.__cam)

    def read(self):
        ret, frame = self.vcap.read()
        if(not ret):
            print('Error: camera srteam not reachable')
            return
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray

    def close(self):
        self.vcap.release()
        cv2.destroyAllWindows()