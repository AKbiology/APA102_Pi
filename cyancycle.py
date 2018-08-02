#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import colorschemesmod

NUM_LED = 200

# Five quick trips through the rainbow
print('Cyan Cycle')

MY_CYCLE = colorschemesmod.TheaterChase(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=1)
									
MY_CYCLE2 = colorschemesmod.TheaterChase2(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=1)
while True:
				MY_CYCLE.start()
				MY_CYCLE2.start()

print('Stopped')
