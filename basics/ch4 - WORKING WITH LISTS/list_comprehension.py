squares = [value ** 2 for value in range(1, 11)]
print(squares)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

a_million = list(range(1, 1_000_0001))
print(min(a_million))
print(max(a_million))
print(sum(a_million))
