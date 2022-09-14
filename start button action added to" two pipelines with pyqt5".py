from math import pi
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import gi  #it is a binding. named pyGobject
gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib

class pipelinevisualizer:
    pipeline = None
    main_loop= None

    def __init__(self):
        Gst.init()
        self.main_loop = GLib.MainLoop()
        
    def createPipeline(self):
        if self.pipeline is None:
            self.pipeline = Gst.parse_launch("v4l2src ! videoconvert ! autovideosink name=p")
            self.pipeline.set_state(Gst.State.PLAYING)
        else:
            self.pipeline.set_state(Gst.State.NULL)
            self.pipeline = Gst.parse_launch("v4l2src ! videoconvert ! autovideosink name=p")
            self.pipeline.set_state(Gst.State.PLAYING)

    def secondPipeline(self):
        if self.pipeline is None:
            self.pipeline = Gst.parse_launch("videotestsrc ! videoconvert ! autovideosink")
            self.pipeline.set_state(Gst.State.PLAYING)
        else:
            self.pipeline.set_state(Gst.State.NULL)
            self.pipeline = Gst.parse_launch("videotestsrc ! videoconvert ! autovideosink")
            self.pipeline.set_state(Gst.State.PLAYING)

    def releasePipeline(self):
        if self.pipeline is not None:
            self.pipeline.set_state(Gst.State.NULL)
            self.pipeline = None
            self.main_loop.quit()

    def pausePipeline(self):
        if self.pipeline is not None:
            self.pipeline.set_state(Gst.State.PAUSED)



visualizer01=pipelinevisualizer()

def close():
    visualizer01.releasePipeline()

def open_web_cam():  
    visualizer01.createPipeline()

def pause_web_cam():
    visualizer01.pausePipeline()

def open_video():
    visualizer01.secondPipeline()

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500,250)
    btn = QPushButton(w)
    btn2 = QPushButton(w)
    btn3 = QPushButton(w)
    btn4 = QPushButton(w)
    btn5 = QPushButton(w)

    btn.setText("Pop up")
    btn2.setText("Stop")
    btn3.setText("Start web cam")
    btn4.setText("Start video")
    btn5.setText("Pause")

    
    btn2.move(300,50)
    btn3.move(100,50)
    btn4.move(100,100)
    btn5.move(300,100)
    w.setWindowTitle("PyQt Dialog demo")

    btn2.clicked.connect(close)
    btn3.clicked.connect(open_web_cam)
    btn4.clicked.connect(open_video)
    btn5.clicked.connect(pause_web_cam)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
            window()