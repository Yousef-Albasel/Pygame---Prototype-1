import pygame
from sys import exit
from random import randint
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics\player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200,350))

def update_score():

    global Curr_time
    Curr_time = (int(pygame.time.get_ticks()/1000)) - start_time
    Score_surf = Score_font.render(f'Score: {Curr_time}',False,('white'))
    score_rect = Score_surf.get_rect(center = (400, 20))
    screen.blit(Score_surf,score_rect)
    return Curr_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 263:
                screen.blit(enemy2,obstacle_rect)
            else:
                screen.blit(enemy1,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100 ]
        return obstacle_list
    else:
        return []
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True
def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 350:
        player_surf=player_walk_1
    else:
        player_index += 0.1
        if player_index > len(player_anim):player_index = 0
        player_surf = player_anim[int(player_index)]
# Essential Parts of the game
pygame.init() 
screen = pygame.display.set_mode((800,400)) # This code creats a display " the main screen " when setting the width and height 
pygame.display.set_caption('Pop Adam V3')
Clock = pygame.time.Clock()
start_time = 0
game_active = False
#Loading Surfaces 

sky = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics\sky.png').convert_alpha()
clouds = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics\clouds.png').convert_alpha()
clouds2 = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics\clouds2.png').convert_alpha()
clouds_pos_x = 0
screen_width=800
clouds_width=800
clouds2_pos_x = -800
ground = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics\ground.png').convert_alpha()

#Enemy Surfaces

enemy1 = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics\enemy1.png').convert_alpha()
enemy2 = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics/bee.png').convert_alpha()
width_en = enemy1.get_rect().width
height_en = enemy1.get_rect().height
enemy1 = pygame.transform.scale(enemy1, (width_en*3, height_en*3))
enemy2 = pygame.transform.scale(enemy2, (60, 50))
obstacle_rect_list=[]
#Player Surfaces
player_walk_1 = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics\player.png').convert_alpha()
player_walk_2 = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics/player2.png').convert_alpha()
player_anim=[player_walk_1,player_walk_2]
player_index=0
width_pl=player_walk_1.get_rect().width
height_pl=player_walk_1.get_rect().height
player_surf = player_anim[player_index]
player_rect = player_surf.get_rect(midbottom = (80,350))

player_stand = pygame.image.load('F:\Projects i work on personally\Pop Adam 3.0\graphics\player.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (150, 150))
player_stand_rect= player_stand.get_rect(center = (400,200))
# Player Gravity 
Player_Grav = 0

#Score Surfaces
obstacle_timer = pygame.USEREVENT + 1 # adding this event so pygame can trigger it 
pygame.time.set_timer(obstacle_timer,900) # trigger the event every 900ms 

#Score Surfaces

Score_font = pygame.font.Font('F:\Projects i work on personally\Pop Adam 3.0\graphics\pixie.ttf',20)
# Score_surf = Score_font.render('Score',False,'white')
# Score_rect = Score_surf.get_rect(midtop = (400,20))

#Text Surfaces Surfaces
game_font = pygame.font.Font('F:\Projects i work on personally\Pop Adam 3.0\graphics\pixie.ttf',20)
game_text = game_font.render('Pop Adam',False,'White')
game_rect = game_text.get_rect( center =(400,50))
game_instruction = game_font.render('Press Space To Continue',False,'White')
game_instruction_rect = game_instruction.get_rect( center =(400,350))
score = 0

#Actual Game mechanics

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 350:
                        Player_Grav = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom == 350:
                        Player_Grav = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks()/1000)
        if event.type == obstacle_timer and game_active:
            if randint(0,2):   
                obstacle_rect_list.append(enemy1.get_rect(midbottom = (randint(900,1100),353)))
            else:
                obstacle_rect_list.append(enemy2.get_rect(midbottom = (randint(900,1100),263)))

    if game_active:
    # Screen blits 
        screen.blit(ground,(0,350))
        screen.blit(sky,(-0,-0))
        screen.blit(clouds, (clouds_pos_x, -0))
        screen.blit(clouds2, (clouds2_pos_x, -0))
        # screen.blit(Score_surf,Score_rect)
        score =  update_score()

    
    # Clouds Moving 
        clouds_pos_x += 5
        clouds2_pos_x += 5

        if clouds_pos_x > screen_width:
            clouds_pos_x = -clouds_width
        if clouds2_pos_x > screen_width:
            clouds2_pos_x = -clouds_width

    # Player phisycs 

        Player_Grav +=1
        player_rect.y += Player_Grav
        if player_rect.bottom >= 350 : player_rect.bottom = 350
        player_animation()
        screen.blit(player_surf,(player_rect))
        
    # enemy phisycs 
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # enemy_rect.left -= 3.5
        # if(enemy_rect.left < -100):
        #     enemy_rect.left = 800
        
    #Collisions 
        game_active = collisions(player_rect,obstacle_rect_list)
       # if enemy_rect.colliderect(player_rect):
         #   game_active= False
    else:
        obstacle_rect_list.clear()
        player_rect.midbottom=(80,350)
        screen.fill((0,199,213))
        screen.blit(player_stand,(player_stand_rect))
        screen.blit(game_text,(game_rect))
        screen.blit(game_instruction,(game_instruction_rect))
        score_massege = Score_font.render(f'Your Score :{score}',False,'White')
        score_massege_rect = score_massege.get_rect(center = (400,320))
        if score == 0: 
            game_text = game_font.render('Pop Adam',False,'White')
            
            screen.blit(game_instruction,(game_instruction_rect))
        else:
            game_text = game_font.render('Game Over',False,'White')

            screen.blit(score_massege,(score_massege_rect))

    pygame.display.update()
    Clock.tick(60) 