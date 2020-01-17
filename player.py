class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.currentLocation = current_location

    def __str__(self):
        return (F'{self.name}, {self.current_location}')