# Create class
class User:
    # Constructor
    # parsing the arguments
    def __init__(self, name, email, age):
        # assigning the arguments as properties to the class

        self.name = name
        self.email = email
        self.age = age


# initialising User object
Dennis = User("Dennis Njuguna", 'dnj445@gmail.com', 23)

print(Dennis.age)
