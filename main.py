import pygame
import tkinter as tk
from tkinter import simpledialog
import os

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SPACE MARKER")

icon = pygame.image.load('assets/space.png')
icon = pygame.transform.scale(icon, (32, 32)) #redimensionar icone pro tamanho certo
pygame.display.set_icon(icon)

background_image = pygame.image.load('assets/bg.jpg')

markers = []

def draw_markers(screen, markers):
    for marker in markers:
        pygame.draw.circle(screen, (255, 0, 0), (marker[0], marker[1]), 5)
        font = pygame.font.Font(None, 24)
        display_text = marker[2]
        if marker[2] == "Desconhecido":
            display_text += f" ({marker[0]}, {marker[1]})"
        text = font.render(display_text, True, (255, 255, 255))
        screen.blit(text, (marker[0] + 10, marker[1]))

    if len(markers) > 1:
        for i in range(len(markers) - 1):
            pygame.draw.line(screen, (0, 255, 0), (markers[i][0], markers[i][1]), (markers[i + 1][0], markers[i + 1][1]), 2)

def save_markers():
    try:
        with open('markers.txt', 'w') as f:
            for marker in markers:
                f.write(f"{marker[0]},{marker[1]},{marker[2]}\n")
    except Exception as e:
        print(f"Erro ao salvar marcações: {e}")

def load_markers():
    global markers
    try:
        if os.path.exists('markers.txt'):
            with open('markers.txt', 'r') as f:
                markers = []
                for line in f:
                    x, y, name = line.strip().split(',')
                    markers.append((int(x), int(y), name))
    except Exception as e:
        print(f"Erro ao carregar marcações: {e}")

def clear_markers():
    global markers
    markers = []


def get_star_name():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    star_name = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    if star_name is None or star_name.strip() == "":
        star_name = "Desconhecido"
    root.destroy()
    return star_name




running  = True
while running:
    screen.blit(background_image, (0, 0))
    draw_markers(screen, markers)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            star_name = get_star_name()
            markers.append((x, y, star_name))

    
    pygame.display.flip()

pygame.quit()
