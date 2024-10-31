#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
from apa102_pi.colorschemes import colorschemes
from coloraide import Color

NUM_LED = 576
BRIGHTNESS = 15

def _colour_list():
  num_points = 100
  interpolation = Color.interpolate(["#dfff0e", "#0eff2f", "#9ac063", "#0ceeb9", "#c2f841"], method="bspline")
  result = [_convert_colour(interpolation(x / num_points)) for x in range(num_points + 1)]
  # print([hex(num) for num in result])
  return result

def _convert_colour(colour):
   colour_string = colour.convert("srgb").to_string(hex=True).removeprefix("#")
   colour_string[2:4], colour_string[4:5] = colour_string[4:5], colour_string[2:4]
   return int(colour_string, 16)

def main():
    # Cycles through a custom colour list
    print('Cycles through a custom colour list')
    colour_list = _colour_list()
    my_cycle = colorschemes.Custom(num_led=NUM_LED, num_steps_per_cycle=len(colour_list), order='rbg', colours=colour_list)
    my_cycle.start()

    print('Finished the test')


if __name__ == '__main__':
    main()
