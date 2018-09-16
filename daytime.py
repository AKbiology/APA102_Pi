#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import colorschemes
import datetime

NUM_LED = 200
now = datetime.datetime.now()
today7am = now.replace(hour=7, minute=0, second=0, microsecond=0)
today7pm = now.replace(hour=20, minute=0, second=0, microsecond=0)
CRYO = 0

while True:

	if (now > today7am) and (now < today7pm):
		CRYO = 1
		print('set daytime')
	if (now < today7am):
		print('set morning')
		CRYO = 2
	if (now > today7pm):
		print('set night')
		CRYO = 3

	if (CRYO == 1):
		print('Daytime')
		MY_CYCLE = colorschemes.Solid(num_led=NUM_LED, pause_value=4,
                            num_steps_per_cycle=1, num_cycles=1)
		MY_CYCLE.start()


	if (CRYO == 2):
		print('Early morning')
		MY_CYCLE = colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
							num_steps_per_cycle=35, num_cycles=5)
		MY_CYCLE.start()


	if (CRYO == 3):
		print('Nighttime')
		MY_CYCLE = colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
							num_steps_per_cycle=35, num_cycles=5)
		MY_CYCLE.start()
