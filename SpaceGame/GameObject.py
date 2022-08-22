import math
import pygame
import random

RESOURCES = {
    "spritesheet": {
        "file": "Resources/sheet.png",
        "surface": None,
        "sprites": {
            "ship_a": { "offset": (222,0,102,84), "rect": None, "surface": None }
        }
    }
}

def preloadResources():
    for resource in RESOURCES:
        sheet = RESOURCES[resource]["surface"]
        if not sheet:
            sheet = pygame.image.load(RESOURCES[resource]["file"]).convert_alpha()
            RESOURCES[resource]["surface"] = sheet
        for sprite in RESOURCES[resource]["sprites"]:
            offset = RESOURCES[resource]["sprites"][sprite]["offset"]
            rect = pygame.Rect(offset)
            image = pygame.Surface(rect.size).convert_alpha()
            image.set_colorkey((0,0,0))
            image.blit(sheet, (0,0), rect)
            RESOURCES[resource]["sprites"][sprite]["rect"] = rect
            RESOURCES[resource]["sprites"][sprite]["surface"] = image

class Text(pygame.sprite.Sprite):
    def __init__(self, text="Hello, world!", color=(255,255,255), size=16, location=(0,0)):
        super().__init__()
        self.text = text
        self.size = size
        self.color = color
        self.font = pygame.font.Font(None, self.size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = location

    def update(self, **kwargs):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 16
        self.image = pygame.Surface((self.size,self.size))
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, (255,0,0), (self.size/2,self.size/2), self.size/2, 1)
        pygame.draw.circle(self.image, (255,0,0), (self.size/2,self.size/2), 1, 2)
        self.rect = self.image.get_rect()
        pygame.mouse.set_visible(False)
        print("Mouse created!")
        self.group = pygame.sprite.Group()
        self.group.add(Text("I'm the mouse!"))

    def update(self, **kwargs):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - self.size/2
        self.rect.y = pos[1] - self.size/2

    def draw(self, surface: pygame.Surface):
        print("Hey!")
        return [self.image.get_rect()]
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 25
        self.image_original = RESOURCES["spritesheet"]["sprites"]["ship_a"]["surface"]
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (pygame.display.get_window_size()[0]/2,pygame.display.get_window_size()[1]/2)
        self.last_update = pygame.time.get_ticks()
        print("Player created!")

    def update(self, **kwargs):
        pos = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(pos[1]-self.rect.centery, pos[0]-self.rect.centerx))
        # print(pos,angle)
        # self.rotate(angle)

    def rotate(self, angle):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            old_center = self.rect.center
            self.image = pygame.transform.rotate(self.image_original, angle)
            self.rect = self.image.get_rect()
            self.rect.center = old_center

class Grid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sizex = pygame.display.get_window_size()[0]
        self.sizey = pygame.display.get_window_size()[1]
        self.image = pygame.Surface((self.sizex,self.sizey))
        self.image.set_colorkey((0,0,0))
        self.image.set_alpha(64)
        pygame.draw.line(self.image, (0,255,0), (0,0), (self.sizex, 0),1) # TOP
        pygame.draw.line(self.image, (0,255,0), (0,0), (0, self.sizey),1) # LEFT
        pygame.draw.line(self.image, (0,255,0), (0,self.sizey-1), (self.sizex, self.sizey-1),1) # BOTTOM
        pygame.draw.line(self.image, (0,255,0), (self.sizex-1,0), (self.sizex-1, self.sizey),1) # RIGHT
        pygame.draw.line(self.image, (0,255,0), (0,self.sizey/2), (self.sizex, self.sizey/2),1) # CENTER X
        pygame.draw.line(self.image, (0,255,0), (self.sizex/2,0), (self.sizex/2, self.sizey),1) # CENTER Y
        self.rect = self.image.get_rect()
        self.rect.center = (self.sizex/2,self.sizey/2)
        

class GreenBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 50
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        print("GreenBox created!")
        self.dir = (random.randint(-10,10),random.randint(-10,10))

    def update(self, **kwargs):
        if self.rect.centerx < 0:
            self.rect.x = pygame.display.get_window_size()[0] - self.size/2
            self.dir = (random.randint(-20,20),random.randint(-20,20))
        elif self.rect.centerx > pygame.display.get_window_size()[0]:
            self.rect.x = 0 - self.size/2
            self.dir = (random.randint(-20,20),random.randint(-20,20))
        if self.rect.centery < 0:
            self.rect.y = pygame.display.get_window_size()[1] - self.size/2
            self.dir = (random.randint(-20,20),random.randint(-20,20))
        elif self.rect.centery > pygame.display.get_window_size()[1]:
            self.rect.y = 0 - self.size/2
            self.dir = (random.randint(-20,20),random.randint(-20,20))
        self.rect.move_ip(self.dir[0], self.dir[1])