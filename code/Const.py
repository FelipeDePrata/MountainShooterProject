#Archive to standardize images values and display's size.
import pygame

# C

COLOR_MAX_BLUE = (13, 0, 255)
COLOR_MAX_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

# M
MENU_OPTION = ('NEW GAME - 1P',
               'NEW GAME - 2P - COOPERATIVE',
               'NEW GAME - 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}

PLAYER_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}

PLAYER_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}

PLAYER_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

# S
SPAWN_ENEMY = 2000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324