#!/usr/bin/env python3

import colorschemesmod

NUM_LED = 200

print('Cyan Cycle')

MY_CYCLE = colorschemesmod.TheaterChase(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=100)
									
MY_CYCLE2 = colorschemesmod.TheaterChase2(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=100)

MY_CYCLE.start()


print('Stopped')
