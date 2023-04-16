import pygame
from string import ascii_uppercase
from sys import exit
from random import choice

from interface import Interface, Scoreboard
from images import Image
from database import Database
from sprites import Letter
db = Database()

interface = Interface(800, 400)
scoreboard = Scoreboard()
images = Image()


class Game:
    def __init__(self, player):
        images.convert_images()
        interface.music_init()
        
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
        
        self.obstacles = pygame.sprite.Group()

         # Timers
        self.letter_timer = pygame.USEREVENT + 1

    def timers_init(self):
        pygame.time.set_timer(self.letter_timer, 1400)

    def can_level_up(self):
        if self.score >= 100 * self.level:
            Letter.increase_speed()
            self.level += 1
        
    def add_letter(self):
        letter = choice(list(ascii_uppercase))
        new_obstacle = Letter(letter)
        self.obstacles.add(new_obstacle)
        new_group = [o for o in self.obstacles if o != new_obstacle]
        if pygame.sprite.spritecollide(new_obstacle, new_group, False):
            new_obstacle.kill()

    def if_missed_letter(self, lives):
        for obstacle in self.obstacles:
            if obstacle.destroy():
                return lives - 1
        return lives
    
    def end_game(self):
        self.game_active = False
        db.add_record(self.score)
        self.lives = 3
        self.obstacles.empty()

    def start_game(self):
        # Main loop
        while self.run:
            # Event checking loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(1)
                if self.game_active:
                    if event.type == self.letter_timer:
                        self.add_letter()

                    if event.type == pygame.KEYDOWN:
                        for obstacle in self.obstacles:
                            self.score = obstacle.hit(event.unicode, self.score)
                else:
                    # Scoreboard show event
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.scoreboard_show:
                            self.scoreboard_show = False
                        if interface.scoreboard_btn_pos[0] <= mouse_pos[0] <= interface.scoreboard_btn_pos[0] + interface.scoreboard_btn_height and \
                                interface.scoreboard_btn_pos[1] <= mouse_pos[1] <= interface.scoreboard_btn_pos[1] + interface.scoreboard_btn_width:
                            # Show scoreboard when button is clicked
                            self.scoreboard_show = True

                    # event to start game
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.game_active = True
                            self.start_time = pygame.time.get_ticks()

            if self.game_active:
                interface.render_game_screen(images.bacgrounds, self.score, self.lives, self.level)
                
                self.can_level_up()
                self.lives = self.if_missed_letter(self.lives)
                self.obstacles.update(self.level)
                self.obstacles.draw(interface.screen)
                if self.lives < 1:
                    self.end_game()
            else:
                if self.scoreboard_show:
                    scoreboard.show_scoreboard(db.get_top_five(), interface.screen, interface.font, interface.font_size)
                else:
                    interface.show_intro_and_end_screen(self.score, images.intro_bg)
            pygame.display.update()
            self.clock.tick(60)

game = Game('player')
game.timers_init()
game.start_game()