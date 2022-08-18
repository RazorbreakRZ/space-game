import pygame

RESOURCES = {
    "mouse": {
        "file": "Resources/cursor.png",
        "sprites": [
            [[0,0],[100,100]]
        ]
    },
    "objects": {
        "file": "Resources/sheet.png",
        "sprites": [
            [[0,0],[0,0]]
        ]
    }
}

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(RESOURCES["mouse"]["file"]).convert()
        self.rect = self.image.get_rect()
        print("Mouse created!")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (pygame.display.get_window_size()[0]/2,pygame.display.get_window_size()[1]/2)
        print("Player created!")

class GreenBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        print("Player created!")

    # def update(self):
    #     self.rect.x = pygame.display.get_window_size()[0]/2
    #     self.rect.y = pygame.display.get_window_size()[1]/2
    