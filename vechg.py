import threading
import time
from src import WebCam
from src import Scene3D

webcam = WebCam()
scene3D = Scene3D(800, 600, 50, 50)

def webcamThreadFunc():
    webcam.Run()
    webcam.Exit()

if __name__ == "__main__":

    try:
        webcam_thread = threading.Thread(target=webcamThreadFunc, args=())
    except Exception as e:
        print(e)
        exit()

    webcam_thread.start()

    scene3D.Run()

    webcam_thread.join()
    

    
    
