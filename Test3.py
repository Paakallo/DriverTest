import sys
import tkinter as tk
from tkinter import messagebox
import pygame
import time
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import csv

class Test3:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Test 3")
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        
        self.COLOR_MAP = {
            "Red": (255, 0, 0),
            "Green": (0, 255, 0),
            "Blue": (0, 0, 255),
            "Yellow": (255, 255, 0),
            "Cyan": (0, 255, 255),
            "Magenta": (255, 0, 255),
        }
        self.COLORS = list(self.COLOR_MAP.items())  # [(name, value), ...]

        self.shapes = []  
        self.results = []


    def draw_random_figures(self, num_figures=5):
        
        self.shapes = []
        self.screen.fill(self.WHITE)

        for _ in range(num_figures):
            shape_type = random.choice(["rect", "circle"])
            color_name, color_value = random.choice(self.COLORS)
            x = random.randint(50, 700)
            y = random.randint(50, 500)
            size = random.randint(30, 80)  # Size for both circles and rectangles

            if shape_type == "rect":
                self.shapes.append({"type": "rect", "color_name": color_name, "color_value": color_value, "x": x, "y": y, "size": size})
                pygame.draw.rect(self.screen, color_value, (x, y, size, size))
            elif shape_type == "circle":
                self.shapes.append({"type": "circle", "color_name": color_name, "color_value": color_value, "x": x, "y": y, "size": size})
                pygame.draw.circle(self.screen, color_value, (x, y), size)

        pygame.display.update()


    def get_target_instruction(self):
        """Select a target and provide an instruction."""
        target_shape = random.choice(self.shapes)
        return target_shape


    def tutorial(self):
        self.draw_random_figures(5)
        target = self.get_target_instruction()
        instruction_text = f"Click on the {target['type']} with color {target['color_name']}."
        print(instruction_text)  # For debugging, can replace with on-screen instructions

        # start_time = time.time()
        event_found = False

        while not event_found:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    for shape in self.shapes:
                        if shape["type"] == "rect":
                            # Check if the click is inside the rectangle
                            if (
                                shape["x"] <= mouse_x <= shape["x"] + shape["size"]
                                and shape["y"] <= mouse_y <= shape["y"] + shape["size"]
                            ):
                                if shape == target:
                                    # end_time = time.time()
                                    # reaction_time = end_time - start_time
                                    # self.results.append({"level": level, "time": reaction_time})
                                    # print(f"Correct! Reaction time: {reaction_time:.3f} seconds.")
                                    event_found = True
                                else:
                                    print("Incorrect shape! Try again.")
                        elif shape["type"] == "circle":
                            # Check if the click is inside the circle
                            distance = ((mouse_x - shape["x"]) ** 2 + (mouse_y - shape["y"]) ** 2) ** 0.5
                            if distance <= shape["size"]:
                                if shape == target:
                                    # end_time = time.time()
                                    # reaction_time = end_time - start_time
                                    # self.results.append({"test_no": 3,"level": level, "time": reaction_time})
                                    # print(f"Correct! Reaction time: {reaction_time:.3f} seconds.")
                                    event_found = True
                                else:
                                    print("Incorrect shape! Try again.")

        print('End of tutorial')
        
        self.dialog = tk.Toplevel()
        self.dialog.title("Tutorial")

        self.continue_button = tk.Button(
            self.dialog, text="Continue", command=lambda: self.dialog.destroy())
        self.continue_button.pack()
        self.dialog.wait_window()


    def tutorial_menu(self):
        self.dialog = tk.Toplevel()
        self.dialog.title("Tutorial")
        self.label = tk.Label(self.dialog, text="Do you want to go through a tutorial?")
        self.label.pack()

        self.yes_button = tk.Button(
            self.dialog, text="Yes", command=lambda: [self.dialog.destroy(), self.tutorial()]
        )
        self.yes_button.pack()

        self.no_button = tk.Button(self.dialog, text="No", command=self.dialog.destroy)
        self.no_button.pack()

        self.dialog.wait_window()


    def introduction(self):
        self.dialog = tk.Toplevel()
        self.dialog.title("Test Decription")
        self.label = tk.Label(self.dialog, text="Your goal is to select appropriate object given by a terminal instruction from a set of randomly generated objects on the screen")
        self.label.pack()

        self.continue_button = tk.Button(
            self.dialog, text="Continue", command=lambda: [self.dialog.destroy(),self.tutorial_menu()])
        self.continue_button.pack()

        self.dialog.wait_window()


    def run_level(self, level, num_figures=5):

        
        self.draw_random_figures(num_figures)
        target = self.get_target_instruction()
        instruction_text = f"Click on the {target['type']} with color {target['color_name']}."
        print(instruction_text)  # For debugging, can replace with on-screen instructions

        start_time = time.time()
        event_found = False

        while not event_found:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    for shape in self.shapes:
                        if shape["type"] == "rect":
                            # Check if the click is inside the rectangle
                            if (
                                shape["x"] <= mouse_x <= shape["x"] + shape["size"]
                                and shape["y"] <= mouse_y <= shape["y"] + shape["size"]
                            ):
                                if shape == target:
                                    end_time = time.time()
                                    reaction_time = end_time - start_time
                                    self.results.append({"level": level, "time": reaction_time})
                                    print(f"Correct! Reaction time: {reaction_time:.3f} seconds.")
                                    event_found = True
                                else:
                                    print("Incorrect shape! Try again.")
                        elif shape["type"] == "circle":
                            # Check if the click is inside the circle
                            distance = ((mouse_x - shape["x"]) ** 2 + (mouse_y - shape["y"]) ** 2) ** 0.5
                            if distance <= shape["size"]:
                                if shape == target:
                                    end_time = time.time()
                                    reaction_time = end_time - start_time
                                    self.results.append({"test_no": 3,"level": level, "time": reaction_time})
                                    print(f"Correct! Reaction time: {reaction_time:.3f} seconds.")
                                    event_found = True
                                else:
                                    print("Incorrect shape! Try again.")
        self.show_result_dialog()


    def show_result_dialog(self):
        self.dialog = tk.Toplevel()
        self.dialog.title("Test 3 Results")

        for result in self.results:
            label = tk.Label(self.dialog, text=f"Your reaction time is {result['time']:.3f} seconds.")
            label.pack()

        close_button = tk.Button(self.dialog, text="Close", command=self.dialog.destroy)
        close_button.pack()

        self.dialog.wait_window() 


    def game_loop(self):
       
       self.introduction()
       # 3 levels
       for level in range(1, 4):
            print(f"Starting Level {level}...")
            self.run_level(level)

       self.save_results()
       self.show_results()
       pygame.quit()


    def save_results(self):
        
        file_exists = os.path.isfile("Test3_results.csv")
        with open("Test3_results.csv", mode="a", newline="") as csv_file:
            fieldnames = ["test_no", "level", "time"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerows(self.results)


    def show_results(self):
        
        times = [result["time"] for result in self.results]
        levels = [result["level"] for result in self.results]

        plt.plot(levels, times, marker="o")
        plt.xlabel("Level")
        plt.ylabel("Reaction Time (s)")
        plt.title("Reaction Time per Level")
        plt.show()