motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []

motorcycles.append('suzuki')
motorcycles.append('honda')
motorcycles.append('bmw')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles.insert(2, 'yamaha')
print(motorcycles)

del motorcycles[3]+
print(motorcycles)

print('\npop example')
popped = motorcycles.pop()
print(motorcycles)
print(popped)

print('\npop from first position')
popped = motorcycles.pop(0)
print(motorcycles)
print(popped)

print('\nappend at the end and remove by value: only removes first ocurrence')
motorcycles.append('suzuki')
motorcycles.remove('suzuki')
print(motorcycles)

print('\nremove by value using var')
remove_this = 'yamaha'
motorcycles.remove(remove_this)
print(motorcycles)
