#toolsPy3
#tools for python 3
#by David


def hamming(str1, str2):
	assert len(str1) == len(str2)
	return sum(c1 != c2 for c1, c2 in zip(str1, str2))