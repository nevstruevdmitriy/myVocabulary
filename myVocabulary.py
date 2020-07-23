import sys
import random

filename = sys.argv[1]
iterations = int(sys.argv[2])

f = open(filename, 'r')

words = f.read().split('\n')

bal = 0

for i in range(iterations):
	print(random.choice(words))
	answer = "-"

	while answer != 'y' and answer != 'n':
		answer = str(input())

	if (answer == 'y'):
		bal += 1

print("\n\n\nКолличство правильных слов -", bal)
print("Из", iterations)
print("Доля", bal / iterations)
print("А всего слов в словаре", len(words))
print("Перемножим последние, получим", bal / iterations * len(words))
