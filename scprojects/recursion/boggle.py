"""
File: boggle.py
Name: stanCode example answer
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file.
# We will be checking if a word exists by searching through it.
FILE = 'dictionary.txt'


def main():
	"""
	When the user inputs 4*4 boggle board, this program will find all boggle answers.
	"""

	# Stores each line's characters into a list, and put all four lists into one single list.
	# This makes us easier to calculate its location using index information.
	boggle_board = []
	for i in range(4):
		while True:
			line = input(str(i + 1) + ' row of letters: ')
			line_lst = line.strip().split()

			valid_input = True
			if len(line_lst) != 4:								# Check if "four" characters are inputted.
				print('Illegal input')
				valid_input = False
			else:
				for ch in line_lst:
					if not ch.isalpha() or len(ch) != 1:		# Check if each character is valid.
						print('Illegal input')
						valid_input = False
						break								# Break this "for loop", stop checking.
			if valid_input:
				boggle_board.append(line_lst)
				break										# Break this "while loop", and goes on to next line.

	start = time.time()

	all_words = []
	read_dictionary(all_words)
	boggle_answers = []
	find_boggle(boggle_board, all_words, boggle_answers)
	print('There are ' + str(len(boggle_answers)) + ' words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(all_words):
	"""
	This function reads file "dictionary.txt" stored in FILE.
	and appends words in each line into a Python list.

	:param all_words: (list) This stores all of the vocabulary in an English dictionary.
	"""
	with open(FILE, 'r') as f:
		for line in f:
			all_words.append(line.strip())


def find_boggle(boggle_board, all_words, boggle_answers):
	"""
	This function choose a character to start with.
	:param boggle_board: (list) The boggle board to be used.
	:param all_words: (list) This stores all of the vocabulary in an English dictionary.
	:param boggle_answers: (list) The list used to store all found boggle answers.
	"""
	for x in range(0, 4):
		for y in range(0, 4):
			current_index = (x, y)
			current_str = boggle_board[x][y]
			used_index = [current_index]
			boggle_helper(boggle_board, all_words, boggle_answers, current_str, current_index, used_index)


def boggle_helper(boggle_board, all_words, boggle_answers, current_str, current_index, used_index):
	"""
	Helper function for find_boggle. This includes more locational information for use.
	:param boggle_board: (list) The boggle board to be used.
	:param all_words: (list) This stores all of the vocabulary in an English dictionary.
	:param boggle_answers: (list) The list used to store all found boggle answers.
	:param current_str: (str) Concatenates all characters that have been chosen.
	:param current_index: (tuple) Stores the locational information of the current character that has been chosen.
	:param used_index: (list) Stores all the chosen characters' position.
	"""

	# Check if current string is a valid word.
	if len(current_str) >= 4:
		if current_str in all_words and current_str not in boggle_answers:
			boggle_answers.append(current_str)
			print(f'Found "{current_str}"')

	for i in range(-1, 2):
		for j in range(-1, 2):
			new_x = current_index[0] + i
			new_y = current_index[1] + j
			if 4 > new_x >= 0 and 4 > new_y >= 0:		# Check if the positional information is valid.
				if (new_x, new_y) not in used_index:
					# Choose
					current_str += boggle_board[new_x][new_y]
					current_index = (new_x, new_y)
					used_index.append(current_index)

					# Explore
					if has_prefix(current_str, all_words):
						boggle_helper(boggle_board, all_words, boggle_answers, current_str, current_index, used_index)

					# Un-choose
					current_str = current_str[:-1]
					current_index = (new_x - i, new_y - j)
					used_index.pop()


def has_prefix(sub_s, all_words):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid.
	:param all_words: (list) This stores all of the vocabulary in an English dictionary.
	:return: (bool) If there is any words with prefix stored in sub_s.
	"""
	for word in all_words:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
