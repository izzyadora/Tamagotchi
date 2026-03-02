from view.animation_class import Animation

class PetView:
    def __init__(self):
        self.animation = Animation("view/assets/tamagotchi_babyboy", 150)

    def update(self, dt):
        self.animation.update(dt)

    def draw(self, surface):
        self.animation.draw(surface, (200, 200))