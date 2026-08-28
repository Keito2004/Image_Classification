import cv2

from camera import Camera
from detector import ObjectDetector

def main():

    # setup camera
    camera = Camera()

    # setup YOLO
    detector = ObjectDetector()

    while True:

        # load a frame from camera
        frame = camera.get_frame()

        # YOLO object detection 
        results = detector.detect(frame)

        # plot figure
        annotated_frame = results[0].plot()

        # show figure
        cv2.imshow("YOLO Object Detection", annotated_frame)

        # stop program -> push "q"
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # end
    camera.release()
    cv2.destroyAllWindows()

if __name__ =="__main__":
    main()