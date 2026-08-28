import cv2

class Camera:

    def __init__(self, camera_id=0):

        self.camera = cv2.VideoCapture(camera_id)

        if not self.camera.isOpened():
            raise RuntimeError("Camera Open failed")

    def get_frame(self):

        ret, frame = self.camera.read()

        if not ret:
            raise RuntimeError("Can't get image")

        return frame

    def release(self):
        self.camera.release()
