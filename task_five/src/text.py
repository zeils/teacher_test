import pygame


class Text(pygame.sprite.Sprite):




    
    
    def __init__(self, x, y, text):
        self.text = text
        pygame.sprite.Sprite.__init__(self)
        



        self.rect = (x-50, y-25, 100, 50)
        self.image = self.edit_text(text)
    



    def edit_text(self, text):

        surface = pygame.Surface((150,75))

        text_color = (250,250,250)
        length = 200
        height = 100
        x = -25
        y = -10


        font_size = int(length//len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    #def update(self, text):
        #self.edit_text(text)
    