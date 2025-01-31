import pygame as p
import os
from chess import Gamestate

DIMENSION = 512
BLACK = (0, 0, 0)        # Black
WHITE = (255, 255, 255)  # White
RED = (255, 0, 0)        # Red
GREEN = (0, 128, 0)      # Green
BLUE = (220, 220, 250)   # Blue


def load_images():
    pieces = ['bR', 'bN', 'bB', 'bK', 'bQ', 'bP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'wP']
    images = {}
    for piece in pieces:
        img_path = os.path.join("images", piece + ".png")
        images[piece] = p.image.load(img_path)
    return images


def draw_board(screen):
    colors = [WHITE, GREEN]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, [c * 64, r * 64, 64, 64])  # Fixed row/col order


def draw_pieces(screen, board, images):
    b_array = board.gs  # Ensure board.gs is a valid 2D list or NumPy array

    for r in range(8):
        for c in range(8):
            piece = b_array[r][c]  # Use list indexing instead of tuple indexing
            if piece != "--":
                screen.blit(images[piece], (c * 64 + 5, r * 64 + 5))


def glow_borders(screen, coords, piece_selected):
    if piece_selected:
        p.draw.rect(screen, BLUE, [coords[1] * 64, coords[0] * 64, 64, 64], 3)  # Thicker highlight


def display_winner(screen, winner, font):
    """Displays the winner and waits for the SPACE key to restart."""

    message = f"{winner} wins!"
    text = font.render(message, True, RED)
    screen.blit(text, (DIMENSION // 2 - 100, DIMENSION // 2 - 60))
    message = f"Press SPACE to restart."
    text = font.render(message, True, RED)
    screen.blit(text, (DIMENSION // 2 - 200, DIMENSION // 2 - 32))
    p.display.flip()

    # Wait for SPACE to restart
    waiting = True
    while waiting:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                exit()
            if e.type == p.KEYDOWN and e.key == p.K_SPACE:
                waiting = False  # Break loop to restart game


def main():
    p.init()
    screen = p.display.set_mode([DIMENSION, DIMENSION])
    screen.fill(WHITE)
    p.display.set_caption('Two-Player Chess Game')

    images = load_images()
    board = Gamestate()
    piece_selected = False
    coords = None
    white_turn = True
    game_ended = False

    font = p.font.Font(None, 50)  # Default font, size 50
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            if game_ended:
                display_winner(screen, "Black" if white_turn else "White", font)
                board = Gamestate()  # Reset board
                piece_selected = False
                coords = None
                white_turn = True
                game_ended = False

            if e.type == p.MOUSEBUTTONDOWN and piece_selected:
                x, y = p.mouse.get_pos()
                d_coords = (y // 64, x // 64)
                white_turn = board.make_move(coords, d_coords, white_turn)
                piece_selected = False

            elif e.type == p.MOUSEBUTTONDOWN:
                x, y = p.mouse.get_pos()
                coords = (y // 64, x // 64)
                piece_selected = True

        # Checkmate detection in every frame
        if board.check_checkmate(white_turn):
            game_ended = True

        # Update screen
        draw_board(screen)
        glow_borders(screen, coords, piece_selected)
        draw_pieces(screen, board, images)
        p.display.flip()

    p.quit()


main()
