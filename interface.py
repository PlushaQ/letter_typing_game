import pygame


class Interface:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Letter shooting game")
        self.font_size = 50
        self.font = pygame.font.Font('font/Pixeltype.ttf', self.font_size)
        self.music_bg = None

        self.scoreboard_btn_pos = self.width - 110, 40
        self.scoreboard_btn_width = 80
        self.scoreboard_btn_height = 80

    def music_init(self):
        self.music_bg = pygame.mixer.Sound('audio/music.wav')
        self.music_bg.set_volume(0.1)
        self.music_bg.play(loops=-1)

    def render_game_screen(self, bg_imgs, score, lives, level):
        
        if level > 5:
            self.screen.blit(bg_imgs[1], (0, 0))
        else:
            self.screen.blit(bg_imgs[0], (0, 0))

        lives_surface = self.font.render(f'Lives: {"<3 " * lives}', False, '#000000')
        lives_rect = lives_surface.get_rect(midleft=(20, 40))
        level_surface = self.font.render(f'Level: {level}', False, '#000000')
        level_rect = level_surface.get_rect(midright=(self.width - 20, 40))
        score_surface = self.font.render(f'Score: {score}', False, '#000000')
        score_rect = score_surface.get_rect(center=(self.width // 2, 40))
        self.screen.blit(lives_surface, lives_rect)
        self.screen.blit(level_surface, level_rect)
        self.screen.blit(score_surface, score_rect)
        return score

    def show_scoreboard_button(self):
        pygame.draw.rect(
            self.screen,
            (0, 122, 122),
            (self.scoreboard_btn_pos[0], self.scoreboard_btn_pos[1],
             self.scoreboard_btn_width, self.scoreboard_btn_height)
        )
        label = self.font.render("TOP", True, (255, 255, 255))
        label_pos = 710, 60
        self.screen.blit(label, label_pos)

    def show_intro_and_end_screen(self, score, intro_bg):
        # Function about rendering intro or end screen depending on state of game
        welcome_text = self.font.render("Letter Shooting Game", False, 'Black')
        welcome_text_rect = welcome_text.get_rect(center=(400, 50))

        
        intro_bg_rect = intro_bg.get_rect(topleft=(0, 0))

        instruction_text = self.font.render("Press SPACE to play!", False, 'Black')
        instruction_text_rect = instruction_text.get_rect(center=(400, 350))

        self.screen.blit(intro_bg, intro_bg_rect)
        self.screen.blit(welcome_text, welcome_text_rect)
        self.show_scoreboard_button()

        score_message = self.font.render(f"Your score: {score}!", False, 'Black')
        score_message_rect = score_message.get_rect(center=(400, 310))
        
        self.screen.blit(instruction_text, instruction_text_rect)
        if score > 0:
            self.screen.blit(score_message, score_message_rect)


interface = Interface(800,400)


class Scoreboard:
    def __init__(self):
        self.scoreboard_pos = (400, 200)
        self.scoreboard_width = 300
        self.scoreboard_height = 300
        self.scoreboard_color = (0, 122, 122)
        self.scoreboard_border_color = (0, 0, 0)
        self.scoreboard_border_width = 2
        self.scoreboard_label = "SCOREBOARD"
        self.scoreboard_label_color = (0, 0, 0)
        self.scoreboard_label_pos = (
            self.scoreboard_pos[0] - self.scoreboard_width // 2, self.scoreboard_pos[1] - self.scoreboard_height // 2
        )

    def show_scoreboard(self, scores, screen, font, font_size):
        # Draw the scoreboard background and border
        pygame.draw.rect(screen, self.scoreboard_color, (
            self.scoreboard_pos[0] - self.scoreboard_width // 2,
            self.scoreboard_pos[1] - self.scoreboard_height // 2,
            self.scoreboard_width, self.scoreboard_height
        ))
        pygame.draw.rect(screen, self.scoreboard_border_color, (
            self.scoreboard_pos[0] - self.scoreboard_width // 2,
            self.scoreboard_pos[1] - self.scoreboard_height // 2,
            self.scoreboard_width, self.scoreboard_height
        ), self.scoreboard_border_width)

        # Draw the scoreboard label
        label = font.render(self.scoreboard_label, True, self.scoreboard_label_color)
        label_pos = (300, 65)
        interface.screen.blit(label, label_pos)

        # Draw the scores
        for i in range(len(scores)):
            score_label = font.render(f'{i + 1}. {scores[i][0]} points ', True, self.scoreboard_label_color)

            score_pos = (self.scoreboard_pos[0] - self.scoreboard_width // 2 + font_size,
                         self.scoreboard_pos[1] - self.scoreboard_height // 2 + font_size + (
                                     i * font_size))
            interface.screen.blit(score_label, score_pos)