class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.currentLocation = current_location

    def __str__(self, name, current_location):
        return (F'{name}, {current_location}')