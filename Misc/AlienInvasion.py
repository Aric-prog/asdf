import sys     
import pygame
def run_game():    # Initialize game and create a screen object.u     
    pygame.init()     
    screen = pygame.display.set_mode((1200, 800))    
    pygame.display.set_caption("Alien Invasion")    # Start the main loop for the game.
    bg_color = (230, 230, 230)     
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()
                
run_game()