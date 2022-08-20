import pygame


class Start_button(pygame.sprite.Sprite):
    
    def __init__(self):
        rock = pygame.image.load("data/start.png").convert()
        pygame.sprite.Sprite.__init__(self)
        self.rect = rock.get_rect(center=(500, 650))
        self.image = rock


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
    
    def update(self, *args):
        if args[0] == '1':
            self.kill()