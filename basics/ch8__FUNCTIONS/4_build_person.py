def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name.title(), 'last': last_name.title()}

    if age:
        person['age'] = age

    return person

musician = build_person('JEHTRO', 'TULL')
print(musician)
print(build_person('ronaldo', 'de leon', 22))