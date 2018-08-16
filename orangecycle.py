#!/usr/bin/env python3

import colorschemesmod

NUM_LED = 200

print('Visual cycle')

MY_CYCLE = colorschemesmod.OrangeChase(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=1000)

while True:									
	MY_CYCLE.start()


print('Stopped')
