fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'rachel': 'matlab',
    'thomas': 'c'
}

print(f"Thomas' favorite language is {fav_languages['thomas'].title()}")
print(f"Tony's favorite language is {fav_languages.get('tony','ERR 3.14: no favorite language assigned for tony')}")

for name, language in fav_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\nThese people took the poll")
# for name in fav_languages.keys():
for name in sorted(fav_languages):
    print(name.title())

print("\nResults")
for name in set(fav_languages.values()):
    print(name.title())

print("\nPoll results for friends")

friends = ['rachel', 'thomas']

for friend in friends:
    print(f"{friend.title()}, I see you love {fav_languages[friend]}")
