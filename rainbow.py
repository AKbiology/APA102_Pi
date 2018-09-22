#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import colorschemes

NUM_LED = 200

print('Repeated rainbow')
While True:
		MY_CYCLE = colorschemes.Rainbow(num_led=NUM_LED, pause_value=0.05,
									   num_steps_per_cycle=255, num_cycles=5)
		MY_CYCLE.start()

		print('Finished a cycle')
