class Item:
    def __init__(self, screen, color, position, size):
        self.screen = screen
        self.position = position
        self.size = size
        self.color = color

    def is_hovered(self, mouse):
        if (self.position[0] <= mouse[0] <= self.position[0] + self.size[0] and
                self.position[1] <= mouse[1] <= self.position[1] + self.size[1]):
            return True
