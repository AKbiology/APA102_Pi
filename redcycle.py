#!/usr/bin/env python3

import colorschemesmod

NUM_LED = 200

print('Red Cycle')

MY_CYCLE = colorschemesmod.TheaterChase3(num_led=NUM_LED, pause_value=0.04,
                                    num_steps_per_cycle=35, num_cycles=200)

							
MY_CYCLE.start()


print('Stopped')
