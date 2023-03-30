import pygame

def main():
    game = Game()
    game.run()
    
    
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = False
        self.init_graphics()
        self.init_objects()
        
    def init_graphics(self):
        img_bird1 = pygame.image.load("images/chicken/flying/frame-1.png")
        self.img_bird1 = pygame.transform.rotozoom(img_bird1, 0, 1/16)
            
     
    def init_objects(self):
        self.bird_y_speed = 0
        self.bird_pos = (0, 300)
       
    def run(self): 
                
        clock = pygame.time.Clock()
        self.running = True
        while self.running: 
            self.handle_events() 
            self.handle_game_logic()          
            self.update_screen()
            #Odota niin kauan, että ruudun päivitysnopeus on 60 fps          
            
            clock.tick(60)  # limits FPS to 60

        pygame.quit()
        
    def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        
    def handle_game_logic(self):
        bird_y = self.bird_pos[1]

        #Painovoima
        bird_y_speed += 1
        bird_y += bird_y_speed

        bird_y = self.bird_pos[1]
        self.bird_pos = (self.bird_pos[0], bird_y)
                
    def update_screen(self):
        self.screen.fill((230, 230, 255))
        
        #Pirrä lintu
        self.screen.blit(self.img_bird1, self.bird_pos)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()