import pygame



class Health(pygame.sprite.Sprite):

    def __init__(self, position, obj_max_helath):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.position = position + pygame.Vector2(0, 5)
        self.max_health = obj_max_helath
        self.health = obj_max_helath
        self.ratio = self.health / self.max_health
        



    def draw(self, screen):
        pygame.draw.rect(screen, "red", (250, 250, 300, 40), self.position)
        pygame.draw.rect(screen, "green", (250, 250, 300 * self.ratio, 40), self.position)




