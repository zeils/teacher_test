from glob import glob
from src.rock import Rock
from src.start_button import Start_button
from src.get_button import Get
from src.text import Text
import pygame


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

game_started = True
print('Введите число камней')
count_of_stones = int(input())
left_score = 0
right_score = 0
player = 1

    
sc = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Игра Баше")
W, H = pygame.display.get_surface().get_size()
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
sc.blit(pygame.image.load('data/background.jpg'), (0,0))






rock = Rock(W,H, count_of_stones)
start_button = Start_button()
get_one_left = Get(200,350, 'data/get_1.png')
get_two_left = Get(200,400, 'data/get_2.png')
get_three_left = Get(200,450, 'data/get_3.png')
get_one_right = Get(800,350, 'data/get_1.png')
get_two_right = Get(800,400, 'data/get_2.png')
get_three_right = Get(800,450, 'data/get_3.png')
get_left_score = Text(200,200, ("Камней у 1 игрока:"+ str(left_score)))
get_right_score = Text(800,200, ("Камней у 2 игрока:"+ str(right_score)))
get_all_count = Text(500,200, ("Осталось камней:"+ str(count_of_stones))) 



all_sprites.add(rock)
all_sprites.add(get_one_left)
all_sprites.add(get_two_left)
all_sprites.add(get_three_left)
all_sprites.add(get_one_right)
all_sprites.add(get_two_right)
all_sprites.add(get_three_right)
all_sprites.add(get_left_score)
all_sprites.add(get_right_score)
all_sprites.add(get_all_count)


def click(change):
    global count_of_stones
    global player
    count_of_stones = count_of_stones-change
    get_all_count.image = get_all_count.edit_text("Осталось камней:"+ str(count_of_stones))
    if player == 1:
        global left_score
        left_score = left_score+change
        get_left_score.image = get_left_score.edit_text("Камней у "+ str(player) + " игрока:"+ str(left_score))
        player = 2
    elif player ==2:
        global right_score
        right_score = right_score+change
        get_right_score.image = get_right_score.edit_text("Камней у "+ str(player) + " игрока:"+ str(right_score))
        player = 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (player == 1) and game_started == True:
                if (get_one_left.pressed(event.pos)) and count_of_stones > 0:
                    click(1)
                if (get_two_left.pressed(event.pos)) and count_of_stones > 1:
                    click(2)
                if (get_three_left.pressed(event.pos)) and count_of_stones > 2:
                    click(3)

            if (player == 2)  and game_started == True:
                if (get_one_right.pressed(event.pos)) and count_of_stones > 0:
                    click(1)
                if (get_two_right.pressed(event.pos)) and count_of_stones > 1:
                    click(2)
                if (get_three_right.pressed(event.pos)) and count_of_stones > 2:
                    click(3)

                

        
        if (count_of_stones == 0) and game_started == True:
            print ('игра закончена')

            game_started = False
            if player == 1:
                get_all_count.image = get_all_count.edit_text('Победил игрок 2')
                print('Победил игрок 2')
            elif player == 2:
                print('Победил игрок 1')
                get_all_count.image = get_all_count.edit_text('Победил игрок 1')


        all_sprites.update('0')
        all_sprites.draw(sc)
        pygame.display.update()


                
            

        
    
    clock.tick(60)