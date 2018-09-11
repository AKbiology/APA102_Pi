#!/usr/bin/env python3

import colorschemesmod

NUM_LED = 200

print('Visual cycle')

MY_CYCLE = colorschemesmod.Solid(num_led=NUM_LED, num_steps_per_cycle=0, num_cycles=1000)

while True:									
	MY_CYCLE.start()


print('Stopped')
