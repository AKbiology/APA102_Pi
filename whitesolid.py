#!/usr/bin/env python3

import colorschemesmod

NUM_LED = 300

print('Visual cycle')

MY_CYCLE = colorschemesmod.Solid(num_led=NUM_LED, pause_value=5000, num_steps_per_cycle=1, num_cycles=1)
						
MY_CYCLE.start()


print('Stopped')