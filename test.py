from PIL import Image
from lib.latergram import Latergram

img = Image.open('photo/kyoto.jpg')

latergram = Latergram(img)
latergram.show()
latergram.saturationUpdate(-50)
latergram.show()
