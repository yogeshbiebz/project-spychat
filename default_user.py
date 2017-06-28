class Spy:
    def __init__(self, name, age, rating ):
        self.name = name
        self.age = age
        self.rating = rating
        self.is_online = True
        self.current_status=''
        self.chats = []


spy_user = Spy('Bond', 31, 4.0)

#   Default friends:
friend1 = Spy('Harry Potter', 20, 4.2)
friend2 = Spy('Tom Riddle', 41, 4.0)
