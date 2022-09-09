import pygame, random


class Display:
    def __init__(self):
        # Variables
        self.__is_running = True
        self.__FPS = 60
        self.__screen_size = (self.__screen_width, self.__screen_height) = (800, 600)

        # Colors
        self.__color_black = (0, 0, 0)
        self.__color_white = (255, 255, 255)

        # DVD Icon Variables
        self.__dvd_x = (self.__screen_width // 2) - 40
        self.__dvd_y = (self.__screen_height // 2) - 40
        self.__dvd_speed = [random.choice([4, -4]), random.choice([4, -4])]
        self.__side_hit = 0
        self.__corner_hit = 0

        self.__game_display = None
        self.__icon = pygame.image.load("DVD_logo.png")
        self.__clock = pygame.time.Clock()

    def __dvd(self):
        dvd = pygame.image.load("DVD_logo.png")

        self.__dvd_x += self.__dvd_speed[0]
        self.__dvd_y += self.__dvd_speed[1]

        if self.__dvd_x <= 0 or (self.__dvd_x >= self.__screen_width - 75):
            self.__side_hit += 1
            self.__dvd_speed[0] = -self.__dvd_speed[0]
        if self.__dvd_y <= -20 or self.__dvd_y >= (self.__screen_height - 60):
            self.__side_hit += 1
            self.__dvd_speed[1] = -self.__dvd_speed[1]
        if self.__dvd_x == 0 and self.__dvd_y == 0:
            self.__corner_hit += 1
        if self.__dvd_x == 0 and self.__dvd_y == (self.__screen_height - 60):
            self.__corner_hit += 1
        if self.__dvd_x == (self.__screen_width - 80) and self.__dvd_y == (self.__screen_height - 60):
            self.__corner_hit += 1
        if self.__dvd_x == (self.__screen_width - 80) and self.__dvd_y == 0:
            self.__corner_hit += 1

        self.__game_display.blit(dvd, [self.__dvd_x, self.__dvd_y])

    def __stats(self):
        text_font = pygame.font.SysFont(None, 25)

        corner_hit_text = text_font.render("Corner Hit: {}".format(self.__corner_hit), True, self.__color_white)
        corner_rect = corner_hit_text.get_rect()
        side_hit_text = text_font.render("Side Hit: {}".format(self.__side_hit), True, self.__color_white)
        side_rect = side_hit_text.get_rect()

        corner_rect.centerx = 100
        corner_rect.centery = 500
        side_rect.centerx = 100
        side_rect.centery = 525

        self.__game_display.blit(corner_hit_text, corner_rect)
        self.__game_display.blit(side_hit_text, side_rect)

    def display(self):
        pygame.init()

        self.__game_display = pygame.display.set_mode(self.__screen_size)
        pygame.display.set_caption("DVD Screensaver")
        pygame.display.set_icon(self.__icon)

        while self.__is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_running = False

            self.__game_display.fill(self.__color_black)
            self.__dvd()
            self.__stats()
            pygame.display.update()
            self.__clock.tick(self.__FPS)

        pygame.quit()
        quit()