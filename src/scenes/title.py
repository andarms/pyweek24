from .scene import Scene


class TitleScene(Scene):
    """docstring for TitleScene"""

    def __init__(self):
        super(TitleScene, self).__init__()

    def draw(self, surface):
        surface.fill((255, 255, 255))
