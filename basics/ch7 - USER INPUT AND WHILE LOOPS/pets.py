pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

while pets:
	pet = pets.pop()

	print(f"{pet.title()} was found in list of pets.")