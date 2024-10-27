#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
from apa102_pi.colorschemes import colorschemes

NUM_LED = 576
BRIGHTNESS = 15


def main(colour_list=[]):
    # Cycles through a custom colour list
    print('Cycles through a custom colour list')

    my_cycle = colorschemes.Custom(num_led=NUM_LED, num_steps_per_cycle=len(colour_list), order='rgb', colours=colour_list)
    my_cycle.start()

    print('Finished the test')


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
