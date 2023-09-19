import pygame


class Player(pygame.sprite.Sprite):

    def __int__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load(r"C:\Users\y_mc\PycharmProjects\Mogwai_Wallet\Map\Sprout Lands - "
                                              r"Sprites - Basic pack\Characters\Basic Charakter Spritesheet.png")
        self.image = self.get_image(0,0)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.position = [x,y]

    def update(self):
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
    def get_image(self,x,y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet,(0,0),(x,y,32,32))

        return image