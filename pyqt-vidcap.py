#!/usr/bin/python
import sys
from pyvidcap import Device
from PyQt4 import Qt, QtCore, QtGui

def loopCamera():
	global webcamImage,cam
	cam.saveSnapshot('photo.jpg')
	webcamPixmap = QtGui.QPixmap('photo.jpg')
	webcamImage.setPixmap(webcamPixmap)

pygame.camera.init()
cam = Device()

a = Qt.QApplication(sys.argv)
webcamImage = Qt.QLabel()
loopCamera()
widget = Qt.QWidget()
verticalBox = Qt.QVBoxLayout()
verticalBox.addWidget(webcamImage)
widget.setLayout(verticalBox)
widget.show()

timer = QtCore.QTimer()
a.connect(timer, Qt.SIGNAL("timeout()"), loopCamera)
timer.start(1)
a.exec_()


pygame.camera.quit()
