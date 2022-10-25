import multiprocessing
from multiprocessing.dummy import freeze_support
from src import WebCam
from src import Scene3D

webcam = WebCam()
scene3D = Scene3D(800, 600, 50, 50)

p1 = multiprocessing.Process(target=webcam.Run())
p2 = multiprocessing.Process(target=scene3D.Run())

# p1.join()
# p2.start()

if __name__ == "__main__":

    freeze_support()

    p1.start()
    p2.start()

    # p1.join()
    # p2.join()

    # webcam.Exit()