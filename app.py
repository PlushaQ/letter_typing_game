import pygame
from sys import exit

from interface import Interface, Scoreboard
from images import Image
from database import Database
db = Database()

interface = Interface(800, 400)
scoreboard = Scoreboard()
images = Image()


class Game:
    def __init__(self, player):
        # images.convert_images()
        # interface.music_init()
        self.run = True
        self.name_screen = False
        self.game_active = False
        self.scoreboard_show = False
        self.score = 0
        self.level = 1
        self.lives = 3
        self.start_time = 0
        self.clock = pygame.time.Clock()
        # Groups
        #
        # self.obstacles = pygame.sprite.Group()

    def start_game(self):
        # Main loop
        while self.run:
            # Event checking loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(1)
                if self.game_active:
                    pass
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.scoreboard_show:
                            self.scoreboard_show = False
                        if interface.scoreboard_btn_pos[0] <= mouse_pos[0] <= interface.scoreboard_btn_pos[0] + interface.scoreboard_btn_height and \
                                interface.scoreboard_btn_pos[1] <= mouse_pos[1] <= interface.scoreboard_btn_pos[1] + interface.scoreboard_btn_width:
                            # Show scoreboard when button is clicked
                            self.scoreboard_show = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.game_active = True
                            self.start_time = pygame.time.get_ticks()

            if self.game_active:
                interface.render_game_screen(images.bg_image, self.score, self.lives, self.level)

            else:
                if self.scoreboard_show:
                    scoreboard.show_scoreboard(db.get_top_five(), interface.screen, interface.font, interface.font_size)
                else:
                    interface.show_intro_and_end_screen(self.score)
            pygame.display.update()
            self.clock.tick(60)

game = Game('player')
game.start_game()