#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import colorschemes

NUM_LED = 200

# One slow trip through the rainbow
print('One slow trip through the rainbow')
MY_CYCLE = colorschemes.Rainbow(num_led=NUM_LED, pause_value=0,
                               num_steps_per_cycle=255, num_cycles=1)
MY_CYCLE.start()

# Five quick trips through the rainbow
print('Five quick trips through the rainbow')
MY_CYCLE = colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=5)
MY_CYCLE.start()

print('Finished the test')