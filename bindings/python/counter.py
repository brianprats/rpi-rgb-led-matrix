#!/usr/bin/python3
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
    self.count = str(response.json()['engagement']['count'])
    #self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

  def run(self):
    offscreen_canvas = self.matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("../../fonts/9x18.bdf")
    pos = 0
    color_pulse = True
    self.get_likes()
    first_count = int(self.count)
    #i = 0
    red = 0
    green = 0
    blue = 0
    #pos = offscreen_canvas.width
    while True:
      self.get_likes()
      print(self.count)
      start = time.time()
      i = 10*(int(self.count) - first_count)
      print(i)
      while time.time()-start <= 15:
          if color_pulse == True:
              if i <= 255:
                  red = i
                  blue = 255 - i
              elif 255 < i <= 510:
                  red = 510 - i
                  green = i - 255
              elif 510 < i <= 765:
                  green = 765 - i
                  blue = i - 510
              else:
                  i = 0
              textColor = graphics.Color(red, green, blue)
          offscreen_canvas.Clear()
          len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, self.count)

      #   pos -= 1
      #    if (pos + len < 0):
      #       pos = offscreen_canvas.width
          time.sleep(0.05)
      #    i = i + 5
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
      print("Press CTRL-C to stop sample")
      self.run()

    except KeyboardInterrupt:
      print("Exiting\n")
      sys.exit(0)

Counter().process()
