def greet_user():
	"""Display a simple string."""
	print("Hello!")

greet_user()

def greet_user(username):
	"""Greet a user by its username"""
	print(f"Howdy {username.title()}!")

greet_user("jbedoya")
greet_user("charles manson")