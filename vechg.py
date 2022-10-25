from src import WebCam
from src import Scene3D

webcam = WebCam()
scene3D = Scene3D(800, 600, 50, 50)

if __name__ == "__main__":
    # webcam.Run()
    # webcam.Exit()

    scene3D.Run()