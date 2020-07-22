cars = ['mazda', 'hyundai', 'subaru', 'volkswagen']

print('before sort')
print(cars)

cars.sort()
print('after sort')
print(cars)

cars.sort(reverse=True)
print('after reverse sort')
print(cars)

print('copy and sort only applied to the copy')
sorted_cars = sorted(cars)
print(sorted_cars)
print(cars)

cars.sort(reverse=True)
print('after reverse sort original list')
print(cars)

cars = ['mazda', 'hyundai', 'subaru', 'volkswagen']

print('before sort')
print(cars)

cars.reverse()
print('reversed (not sorted)')
print(cars)

print('len')
print(len(cars))
