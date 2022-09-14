from math import pi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

import gi  #it is a binding. named pyGobject
gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib

Gst.init()
main_loop = GLib.MainLoop()

class pipelinevisualizer:
    def __init__(self):
        global pipeline
        pipeline = Gst.parse_launch("v4l2src ! videoconvert ! autovideosink")
        #global pipeline

visualizer01=pipelinevisualizer()

def close_web_cam():
    visualizer01
    end_pipeline = pipeline.set_state(Gst.State.NULL)

def open_web_cam():  
    visualizer01
    play_pipeline = pipeline.set_state(Gst.State.PLAYING)
      
def pause_web_cam():
    visualizer01
    pause_cam = pipeline.set_state(Gst.State.PAUSED)

def ready_web_cam(self):
        #ready_cam = pipeline.set_state(Gst.State.READY)
    pass

def window():

    app = QApplication(sys.argv)
    w = QWidget()
    btn = QPushButton(w)
    btn2 = QPushButton(w)
    btn3 = QPushButton(w)
    btn4 = QPushButton(w)
    btn5 = QPushButton(w)

    btn.setText("Pop up")
    btn2.setText("Stop")
    btn3.setText("Start")
    btn4.setText("Ready")
    btn5.setText("Pause")

    
    btn2.move(300,50)
    btn3.move(100,50)
    btn4.move(100,100)
    btn5.move(300,100)
    w.setWindowTitle("PyQt Dialog demo")

    btn2.clicked.connect(close_web_cam)
    btn3.clicked.connect(open_web_cam)
    btn4.clicked.connect(ready_web_cam)
    btn5.clicked.connect(pause_web_cam)
    w.show()
    sys.exit(app.exec_())

    
if __name__ == '__main__':
    window()

    main_loop.quit()



