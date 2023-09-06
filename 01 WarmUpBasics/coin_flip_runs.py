"""
File: coin_flip_runs.py
Name: Janelle Lin
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	:input: number of runs (consecutive coin flipping results)
	:return: a random result which is consistent with the runs input by users
	"""
	print("Let's flip a coin!")
	runs = int(input('Number of runs: '))
	actual_run = 0
	result = ''
	flip1 = r.choice('HT')

	result += flip1
	is_in_a_row = False

	while True:
		flip2 = r.randrange(1, 3)
		if flip2 == 1:
			flip2 = 'T'
		else:
			flip2 = 'H'
		result += flip2

		if flip2 == flip1:
			if not is_in_a_row:
				is_in_a_row = True
				actual_run += 1
				if actual_run == runs:
					break
		else:
			is_in_a_row = False

		flip1 = flip2

	print(str(result))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
