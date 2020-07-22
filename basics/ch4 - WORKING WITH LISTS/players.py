players = ['maradona', 'zico', 'pele', 'milla', 'valderrama', 'kempes']

print("0:3")
print(players[0:3])
print("1:4")
print(players[1:4])
print("1:")
print(players[1:])
print(":3")
print(players[:3])
print("-3:")
print(players[-3:])
print(":")
print(players[:])
print("0:3:2")
print(players[0:3:2])


print("Some players [::2]\n")
for player in players[::2]:
	print(f"{player.title()}, is one of them")
	

print("Some players [1::2]\n")
for player in players[1::2]:
	print(f"{player.title()}, is one of them")
	
