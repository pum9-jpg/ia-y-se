# tres_rayalimpio_sin_menu.py
import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 700, 750
BOARD_XY = 600
SQ = BOARD_XY // 3
LINE_W = 15
RADIO = SQ // 3
CIRC_W = 15
CROSS_W = 25
SPACE = SQ // 4

BG        = (30, 30, 40)
LINE      = (90, 90, 120)
CIRC      = (255, 105, 180)
CROSS     = (0, 195, 255)
TEXT      = (240, 240, 250)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tres en Raya")
clock = pygame.time.Clock()
font_big   = pygame.font.SysFont("arial", 60, True)
font_small = pygame.font.SysFont("arial", 30, True)

# ---------- ESTADO ----------
board  = [[0]*3 for _ in range(3)]
turn   = 1
winner = 0
particles = []

# ---------- FUNCIONES ----------
def draw_text(text, font, color, x, y, center=True):
    t = font.render(text, True, color)
    rect = t.get_rect(center=(x, y)) if center else (x, y)
    screen.blit(t, rect)

def draw_board():
    screen.fill(BG)
    for i in range(1, 3):
        pygame.draw.line(screen, LINE, (50, 50+i*SQ), (50+BOARD_XY, 50+i*SQ), LINE_W)
        pygame.draw.line(screen, LINE, (50+i*SQ, 50), (50+i*SQ, 50+BOARD_XY), LINE_W)

def draw_figures():
    for r in range(3):
        for c in range(3):
            x = 50 + c*SQ + SQ//2
            y = 50 + r*SQ + SQ//2
            if board[r][c] == 1:
                pygame.draw.circle(screen, CIRC, (x, y), RADIO, CIRC_W)
            elif board[r][c] == 2:
                pygame.draw.line(screen, CROSS, (x-SPACE, y-SPACE), (x+SPACE, y+SPACE), CROSS_W)
                pygame.draw.line(screen, CROSS, (x+SPACE, y-SPACE), (x-SPACE, y+SPACE), CROSS_W)

def free(r, c): return board[r][c] == 0
def full(): return all(board[r][c] != 0 for r in range(3) for c in range(3))

def check_win(pl):
    for r in range(3):
        if all(board[r][c] == pl for c in range(3)): return True
    for c in range(3):
        if all(board[r][c] == pl for r in range(3)): return True
    if all(board[i][i] == pl for i in range(3)): return True
    if all(board[i][2-i] == pl for i in range(3)): return True
    return False

def reset():
    global board, turn, winner
    board = [[0]*3 for _ in range(3)]
    turn = 1
    winner = 0
    particles.clear()

# ---------- CONFETI ----------
def create_confeti():
    for _ in range(80):
        particles.append({
            "x": random.randint(0, WIDTH),
            "y": random.randint(-50, 0),
            "vy": random.randint(2, 8),
            "color": random.choice([CIRC, CROSS, (255, 255, 255)]),
            "size": random.randint(4, 8)
        })

def update_confeti():
    for p in particles[:]:
        p["y"] += p["vy"]
        pygame.draw.circle(screen, p["color"], (int(p["x"]), int(p["y"])), p["size"])
        if p["y"] > HEIGHT:
            particles.remove(p)

# ---------- BUCLE ----------
reset()  # primera partida limpia
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        # Teclas rápidas
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:   # nueva partida
                reset()
            elif e.key == pygame.ESCAPE:  # salir
                pygame.quit(); sys.exit()

        # Click sobre el tablero
        if winner == 0 and e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            if 50 <= x <= 50+BOARD_XY and 50 <= y <= 50+BOARD_XY:
                c, r = (x-50)//SQ, (y-50)//SQ
                if free(r, c):
                    board[r][c] = turn
                    if check_win(turn):
                        winner = turn
                        create_confeti()
                    elif full():
                        winner = 3
                        create_confeti()
                    else:
                        turn = 3 - turn

    # DIBUJO
    draw_board()
    draw_figures()
    if winner == 0:
        draw_text(f"Turno: {'O' if turn == 1 else 'X'}", font_small, TEXT, WIDTH//2, HEIGHT-40)
    else:
        update_confeti()
        if winner == 1:   msg, color = "¡O GANA!", CIRC
        elif winner == 2: msg, color = "¡X GANA!", CROSS
        else:             msg, color = "¡EMPATE!", TEXT
        draw_text(msg, font_big, color, WIDTH//2, 120)
        draw_text("ESPACIO → Nueva partida    ESC → Salir", font_small, TEXT, WIDTH//2, HEIGHT-40)

    pygame.display.flip()
    clock.tick(60)