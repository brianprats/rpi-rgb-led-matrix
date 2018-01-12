import time
import sys
import requests
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

class Counter(object):

  def get_likes(self):
    myToken='EAAO6Vy3npTsBAGQeL1RpZAVCrISxxtQcYiysdMnNga4Fr13ZCy78wQuc1xVYB1ZAIuVQMP44sGf1JpTVRzg18ai9YVKSkOLaHZAshSxxLMP2bd2mYRXB8rYaxhU9XRQ2FuD57VTFF4WnrcwuaAe8A64vnRp21WOLyRwhPmmt6gZDZD'
    myUrl = 'https://graph.facebook.com/https://www.facebook.com/Thrillist/?fields=engagement'
    head = {'Authorization': 'OAuth {}'.format(myToken)}
    response = requests.get(myUrl, headers=head)
    self.count = response.json()['engagement']['count']
    #self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

  def run(self):
    offscreen_canvas = self.matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("../../../fonts/7x13.bdf")
    textColor = graphics.Color(255, 255, 0)
    pos = offscreen_canvas.width
    while True:
      self.get_likes()
      while time.now() >= 30
          offscreen_canvas.Clear()
          len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, self.count)
          pos -= 1
          if (pos + len < 0):
              pos = offscreen_canvas.width

          time.sleep(0.05)
          offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

  def process(self):
    options = RGBMatrixOptions()

    options.rows = 32
    options.chain_length = 2
    options.parallel = 1
    options.pwm_bits = 11
    options.brightness = 100
    options.pwm_lsb_nanoseconds = 130
    options.led_rgb_sequence = 'RGB'

    options.disable_hardware_pulsing = True

    self.matrix = RGBMatrix(options = options)

    try:
      #  loop
      print("PrStartess CTRL-C to stop sample")
      self.run()

    except KeyboardInterrupt:
      print("Exiting\n")
      sys.exit(0)

# Main function
if __name__ == "__main__":
    run_text = Counter()
    if (not run_text.process()):
        run_text.print_help()