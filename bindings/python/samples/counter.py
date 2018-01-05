from samplebase import SampleBase
from rgbmatrix import graphics
import time
import sys
import requests
from rgbmatrix import RGBMatrix, RGBMatrixOptions

myToken='EAAO6Vy3npTsBAGQeL1RpZAVCrISxxtQcYiysdMnNga4Fr13ZCy78wQuc1xVYB1ZAIuVQMP44sGf1JpTVRzg18ai9YVKSkOLaHZAshSxxLMP2bd2mYRXB8rYaxhU9XRQ2FuD57VTFF4WnrcwuaAe8A64vnRp21WOLyRwhPmmt6gZDZD'
myUrl = 'https://graph.facebook.com/https://www.facebook.com/Thrillist/?fields=engagement'
head = {'Authorization': 'OAuth {}'.format(myToken)}
response = requests.get(myUrl, headers=head)
#print(response.content)
counts = response.json()['engagement']['count']

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'

#matrix = RGBMatrix(options = options)
font = graphics.Font().LoadFont("../../../fonts/7x13.bdf")
canvas = self.matrix
blue = graphics.Color(0,255,0)
graphics.DrawText(canvas, font, 2, 10, blue, counts)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)