#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import colorschemesmod

NUM_LED = 200

print('Repeated rainbow')

while True:
		MY_CYCLE = colorschemesmod.Rainbow(num_led=NUM_LED, pause_value=0.05,
									   num_steps_per_cycle=255, num_cycles=10000)
		MY_CYCLE.start()

		print('Finished a cycle')
