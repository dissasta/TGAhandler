import os

class image(object):
    def __init__(self, source):
        self.source = source
        self.format = None
        self.id = None
        self.colourMapType = None
        self.imgType = None
        self.colourMapSpec = None
        self.imageSpec = None
        self.imageId = None
        self.colourMapData = None
        self.imageData = None
        self.width = None
        self.height = None
        self.rle = None
        self.alpha = None
        self.properties = [self.source, self.width, self.height, self.rle, self.alpha]
        self.header = None
        self.footer = None
        self.load()

    def load(self):
        file = open(self.source, 'rb')
        try:

            file.seek(-26, os.SEEK_END)
            footerData = file.read()
            file.close()
            if 'TRUEVISION-XFILE' in footerData:
                self.format = 'NEW'
                self.footer = footerData.encode('HEX')
                with open(self.source, 'rb') as file:
                    headerData = file.read(18)
                    print headerData.encode('HEX')

        except Exception:
            #not a viable file
            pass


    def save(self, dest):
        pass
