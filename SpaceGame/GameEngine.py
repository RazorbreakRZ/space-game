import pygame
from Utils import merge
import GameObject

class GameEngine:
    def __init__(self, config):
        pygame.init()
        pygame.font.init()
        self.config = merge(self.__getDefaultConfig(), config)
        # print(self.config)
        pygame.display.set_caption("Space Game v1.0.0")
        self.screen = pygame.display.set_mode(size=self.config["screen"]["resolution"], display=self.config["screen"]["device"])
        if self.config["screen"]["fullscreen"]:
            pygame.display.toggle_fullscreen()
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.allSprites = {}

    def __getDefaultConfig(self):
        defaultConfig = {
            "screen": {
                "device": 0,
                "resolution": [0, 0],
                "fullscreen": True,
                "fps": 30
            },
            "controls": {
                "QUIT": pygame.K_ESCAPE,
                "HELP": pygame.K_F1,
                "TURN_LEFT": pygame.K_LEFT,
                "TURN_RIGHT": pygame.K_RIGHT,
                "FIRE": 1,
                "SPAN": 3
            }
        }
        return defaultConfig

    def getConfig(self):
        return self.config

    def __load(self):
        GameObject.preloadResources()
        self.allSprites = { 
            "background": pygame.sprite.Group(),
            "player": pygame.sprite.Group(),
            "enemies": pygame.sprite.Group(),
            "hud": pygame.sprite.Group()
        }
        self.allSprites["background"].add(GameObject.Grid())
        self.allSprites["player"].add(GameObject.Player())
        self.allSprites["enemies"].add(GameObject.GreenBox())
        self.allSprites["hud"].add(GameObject.Mouse())
    
    def loop(self):
        self.__load()
        while self.isRunning:
            self.__inputs()
            self.__update()
            self.__draw()
            self.__tick()
        pygame.quit()
            
    def __inputs(self):
        for event in pygame.event.get():
            # print(event)
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYUP and event.key == self.config["controls"]["QUIT"]):
                self.__callback_exit(event)
                
    def __update(self):
        for group in self.allSprites:
            self.allSprites[group].update()
    
    def __draw(self):
        self.screen.fill((0,0,0))
        for group in self.allSprites:
            self.allSprites[group].draw(self.screen)
    
    def __tick(self):
        pygame.display.flip()
        self.clock.tick(self.config["screen"]["fps"])

    def __callback_exit(self, event):
        # print(event)
        self.isRunning = False
    