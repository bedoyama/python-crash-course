pizza = {
    'crust': 'thick',
    'toppings': ['pepperoni', 'mushrooms', 'olives']
}

print(f"You ordered a {pizza['crust']}-crust pizza, "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")