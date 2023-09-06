"""
File: boggle.py
Name: Janelle
----------------------------------------
Play Boggle game; input 4*4 characters, each of them isolated by space
"""

import time

FILE = 'dictionary.txt'


def main():
	"""
	Play Boggle game
	"""
	start = time.time()
	dictionary = read_dictionary()

	# Create a list(b) in which store the character
	b = []

	# Input, check and form it into a nested list
	for i in range(4):
		print(f"{i + 1} ", end="")
		chs = input("row of letters: ").lower().split()

		if len(chs) == 4 and all(len(c) == 1 for c in chs):
			b.append(chs)
		else:
			print("Illegal input")
			break

	if b:
		# Create another list(v) in which store a character's visited status
		v = [[False] * 4 for _ in range(4)]

		# Process the boggle and find words matched
		ans_lst = []
		for row in range(4):
			for col in range(4):
				v[row][col] = True
				find_words(b, v, row, col, '', ans_lst, dictionary)
				v[row][col] = False

		# Print result count
		print(f"There are {len(ans_lst)} words in total.")

		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(boggle, visited, row, col, current_word, ans_lst, dictionary):
	"""
	This recursive function find words appear in dictionary
	:param boggle: The user's input 4*4 boggle saved in a nested list.
	:param visited: The status of character's visited status
	:param row: The row number of a character in the boggle game
	:param col: The column number of a character in the boggle game
	:param current_word: The current status of permutation
	:param ans_lst: The list which holds the results and save them from duplication
	:param dictionary: The dictionary for looking up
	:return: None
	"""
	# Base case
	if len(current_word) >= 4:
		if current_word not in ans_lst and current_word in dictionary:
			ans_lst.append(current_word)
			print('Found "' + current_word + '"')

	for dr in range(-1, 2):
		for dc in range(-1, 2):
			new_row, new_col = row + dr, col + dc
			if (dr, dc) != (0, 0) and 0 <= new_row < 4 and 0 <= new_col < 4 and not visited[new_row][new_col]:

				# Recursive case
				# Choose
				current_word += boggle[row][col]
				visited[row][col] = True

				# Explore
				if has_prefix(current_word, dictionary):
					find_words(boggle, visited, new_row, new_col, current_word, ans_lst, dictionary)

				# Un-choose
				current_word = current_word[:-1]
				visited[row][col] = False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if 17 > len(word) > 3:  # Only consist words which length is in between
				dictionary.append(word)
	dictionary = set(dictionary)

	return dictionary


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
