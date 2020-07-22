alien_0 = {'color': 'yellow', 'points': 2}
alien_1 = {'color': 'blue', 'points': 12}
alien_2 = {'color': 'magenta', 'points': 22}

aliens = [alien_0, alien_1, alien_2]

aliens.append({'color': 'beige', 'points': 23})

for idx in range(8):
    aliens.append({'color': 'blue', 'points': 9})

for alien in aliens[8:]:
    alien['color'] = 'pink'
    alien['points'] = 11

for alien in aliens:
    print(f"Alien with the color {alien['color']} has {alien['points']} points.")
