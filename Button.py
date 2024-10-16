import pygame
import time
pygame.init()


class Button():
    def __init__(self, Text, x, y, fg=(255, 255, 255), fonts="SimHei", font_size=16, scale=1) -> None:
        font = pygame.font.SysFont(fonts, font_size)
        self.image = font.render(Text, True, fg)
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def draw(self, surface, bg=(0, 0, 0), lg=(255, 255, 255), pg=(255, 0, 0)) -> None:
        pygame.draw.rect(surface, bg, (self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()))
        self.bc = pygame.draw.rect(surface, lg,
                                   (self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()), 3)
        surface.blit(self.image, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.bc.collidepoint(pos):
            self.bc = pygame.draw.rect(surface, pg,(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()), 3)

    def get_button_state(self) -> bool:
        pos = pygame.mouse.get_pos()
        if self.bc.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.2)
                return True
        else:
            return False