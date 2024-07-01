import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import random
import threading

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

truck1_img = pygame.image.load("truck1.png")
truck2_img = pygame.image.load("truck2.png")
finish_line_img = pygame.image.load("finish_line.png")
finish_line_rect = finish_line_img.get_rect(midtop=(WIDTH // 2, 50))

truck1_rect = truck1_img.get_rect(midbottom=(WIDTH // 4, HEIGHT - 50))
truck2_rect = truck2_img.get_rect(midbottom=(3 * WIDTH // 4, HEIGHT - 50))


truck1_speed = random.randint(5, 10)
truck2_speed = random.randint(5, 10)

screen = pygame.Surface((WIDTH, HEIGHT))

def run_race():
    global truck1_rect, truck2_rect, truck1_speed, truck2_speed
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        truck1_rect.y -= truck1_speed
        truck2_rect.y -= truck2_speed

        if truck1_rect.top <= finish_line_rect.bottom or truck2_rect.top <= finish_line_rect.bottom:
            winner = "Truck 1" if truck1_rect.top <= finish_line_rect.bottom else "Truck 2"
            running = False
            messagebox.showinfo("Race Result", f"{winner} wins the race!")
            reset_race()

        screen.fill(WHITE)

        screen.blit(finish_line_img, finish_line_rect)

        screen.blit(truck1_img, truck1_rect)
        screen.blit(truck2_img, truck2_rect)

        display_game()
        pygame.time.Clock().tick(30)

def display_game():
    global screen
    game_image = pygame.surfarray.array3d(screen)
    game_image = game_image.swapaxes(0, 1)
    game_image = Image.fromarray(game_image)
    game_photo = ImageTk.PhotoImage(image=game_image)
    canvas.create_image(0, 0, image=game_photo, anchor=tk.NW)
    canvas.image = game_photo
    root.update_idletasks()

def reset_race():
    global truck1_rect, truck2_rect, truck1_speed, truck2_speed
    truck1_rect.midbottom = (WIDTH // 4, HEIGHT - 50)
    truck2_rect.midbottom = (3 * WIDTH // 4, HEIGHT - 50)
    truck1_speed = random.randint(5, 10)
    truck2_speed = random.randint(5, 10)

root = tk.Tk()
root.title("The Great Ice-Cream Truck Race")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

start_button = tk.Button(root, text="Start Race", command=lambda: threading.Thread(target=run_race).start())
start_button.pack(pady=20)

root.mainloop()
pygame.quit()
