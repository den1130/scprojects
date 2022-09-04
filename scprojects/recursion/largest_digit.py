"""
File: largest_digit.py
Name: stanCode example answer
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	Find the largest digit!
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int
	:return: int, the largest digit in n
	"""
	if n < 0:
		n *= -1

	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, maximum):
	"""
	:param n: int
	:param max: int, stores the maximum digit as the finding goes.
	"""
	# Base case
	if n < 10:
		if n > maximum:
			return n
		else:
			return maximum
	# Recursive case
	else:
		digit = n % 10
		if digit > maximum:
			maximum = digit

		return find_largest_digit_helper(n // 10, maximum)


if __name__ == '__main__':
	main()
