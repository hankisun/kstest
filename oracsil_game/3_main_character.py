import pygame

pygame.init() # 초기화

# 화면크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("oracsil game") # 게임 이름

# 배경 이미지 설정
background = pygame.image.load("D:\\myProjects\\oracsil_game\\background.png")

# 캐릭터 불러오기
character = pygame.image.load("D:\\myProjects\\oracsil_game\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# 이벤트 루프
running = True # 게임이 진행중인가
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    #screen.fill((0,0,255))
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # 게임화면다시 그리기

    


# pygame 종료
pygame.quit()
