from samplebase import SampleBase
from rgbmatrix import graphics
import time
import sys
import requests
from rgbmatrix import RGBMatrix, RGBMatrixOptions

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        myToken='EAAO6Vy3npTsBAGQeL1RpZAVCrISxxtQcYiysdMnNga4Fr13ZCy78wQuc1xVYB1ZAIuVQMP44sGf1JpTVRzg18ai9YVKSkOLaHZAshSxxLMP2bd2mYRXB8rYaxhU9XRQ2FuD57VTFF4WnrcwuaAe8A64vnRp21WOLyRwhPmmt6gZDZD'
        myUrl = 'https://graph.facebook.com/https://www.facebook.com/Thrillist/?fields=engagement'
        head = {'Authorization': 'OAuth {}'.format(myToken)}
        response = requests.get(myUrl, headers=head)
        #print(response.content)
        counts = response.json()['engagement']['count']
        #self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = counts

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()