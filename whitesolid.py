#!/usr/bin/env python3

import colorschemes

NUM_LED = 200

print('Visual cycle')

MY_CYCLE = colorschemes.Solid(num_led=NUM_LED, pause_value=5000, num_steps_per_cycle=1, num_cycles=1)
						
MY_CYCLE.start()


print('Stopped')
