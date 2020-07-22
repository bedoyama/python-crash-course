def describe_pet(animal_type, pet_name='virgil'):
    """Display info about Virgil"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog', 'virgil')
describe_pet('hamster', 'harry')
describe_pet(pet_name='garfield', animal_type='cat')
describe_pet('dog')
