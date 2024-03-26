from math import factorial
from typing import List


def permutaion(n: int, r: int, identicals: List[int]) -> int:
	permutaions = factorial(n) / factorial(r)
	try:
		for i in identicals:
			permutaions /= factorial(i)
			return permutaions
	except :
		print('something')



print(permutaion(5, 4))