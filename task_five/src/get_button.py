import pygame

class Get(pygame.sprite.Sprite):

    def __init__(self, x, y, data):
        get_1 = pygame.image.load(data).convert()
        pygame.sprite.Sprite.__init__(self)
        self.rect = get_1.get_rect(center=(x, y))
        self.image = get_1
    
    def update(self, *args):
        if args[0] == '1':
            self.kill()

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False




