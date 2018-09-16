#!/usr/bin/env python3
"""Sample script to run a few colour tests on the strip."""
import colorschemes
import datetime

NUM_LED = 200
now = datetime.datetime.now()
today7am = now.replace(hour=7, minute=0, second=0, microsecond=0)
today7pm = now.replace(hour=19, minute=0, second=0, microsecond=0)

while true

	if (now > today7am) and (now < today7pm)
		print('White light')
		MY_CYCLE = colorschemes.Solid(num_led=NUM_LED, pause_value=4,
                            num_steps_per_cycle=1, num_cycles=1)
		MY_CYCLE.start()

	if (now < today7am) 
		print('Five quick trips through the rainbow')
		MY_CYCLE = colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
							num_steps_per_cycle=35, num_cycles=5)
		MY_CYCLE.start()

	if (now > today7pm)
		print('Five quick trips through the rainbow')
		MY_CYCLE = colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04,
							num_steps_per_cycle=35, num_cycles=5)
		MY_CYCLE.start()