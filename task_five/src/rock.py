import pygame


class Rock(pygame.sprite.Sprite):
    
    def __init__(self, W, H, Count_of_stones):
        rock = pygame.image.load("data/rock.png").convert()
        pygame.sprite.Sprite.__init__(self)
        rock.set_colorkey((255,255,255))
        self.rect = rock.get_rect(center=(W//2, H//2))
        self.image = rock
    
    def update(self, *args):
        if args[0] == '1':
            self.kill()






        