import pygame

class GameEngine:
    def __init__(self):
        pygame.init()
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        self._isRunning = True
        self.keyMapping = []
        
    
    def __config(self):
        self.keyMapping = [
            {
                "name": "EXIT",
                "callback": self.__callback_exit,
                "triggers": [
                    {"type": pygame.QUIT},
                    {"type": pygame.KEYDOWN, "key": pygame.K_ESCAPE}
                ]
            }
        ]
        print(self.keyMapping)
    
    def loop(self):
        self.__config()
        while self._isRunning:
            self.__inputs()
            self.__logic()
            self.__draw()
        pygame.quit()
            
    def __inputs(self):
        for event in pygame.event.get():
            print(event)
            for keymap in self.keyMapping:
                for trigger in keymap.get("triggers"):
                    if event.type == trigger["type"]:
                        if event.key == trigger.get("key"):
                            keymap["callback"]()
    
    def __logic(self):
        pass
    
    def __draw(self):
        pass
    
    def __tick(self):
        pygame.display.update()
        self.clock.tick(30)

    def __callback_exit(self):
        self._isRunning = False

ge = GameEngine()
ge.loop()