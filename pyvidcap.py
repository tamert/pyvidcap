import vidcap
from PIL import Image

class Device:

    def __init__(self, devnum=0, showVideoWindow=0):
        self.dev = vidcap.new_Dev(devnum, showVideoWindow)

    def displayPropertyPage(self):
        self.dev.displaypropertypage()

    def displayCaptureFilterProperties(self):
        self.dev.displaycapturefilterproperties()

    def displayCapturePinProperties(self):
        self.dev.displaycapturepinproperties()

    def setResolution(self, width, height):
        self.dev.setresolution(width, height)

    def getDisplayName(self):
        return self.dev.getdisplayname()

    def getBuffer(self):
        return self.dev.getbuffer()

    def getImage(self):

        buffer, width, height = self.getBuffer()
        if buffer:
            im = Image.fromstring('RGB', (width, height), buffer, 'raw', 'BGR', 0, -1)
            return im

    def saveSnapshot(self, filename):
        self.getImage().save(filename)

        
if __name__ == '__main__':
    cam = Device(devnum=0)
    print("Select Device Name: ", cam.getDisplayName())
