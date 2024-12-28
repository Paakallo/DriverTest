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


class Test1:
    def __init__(self, parent):
        pygame.init()

        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)

        self.parent = parent # parent tkinter
        self.results = []  


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


    def tutorial(self):
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Test 1")

        circle_center = (random.randint(0, 400), random.randint(0, 300))
        circle_radius = 50

        screen.fill(self.WHITE)
        pygame.draw.circle(screen, self.RED, circle_center, circle_radius)
        pygame.display.update()

        event_found = False

        while not event_found:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    distance = ((mouse_x - circle_center[0]) ** 2 + (mouse_y - circle_center[1]) ** 2) ** 0.5

                    if distance <= circle_radius:
                        event_found = True
                        break
        
        self.dialog = tk.Toplevel()
        self.dialog.title("Tutorial")
        
        self.no_button = tk.Button(self.dialog, text="Continue", command=self.dialog.destroy)
        self.no_button.pack()

        self.dialog.wait_window()


    def draw_circle(self,level):
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Test 1")

        circle_center = (random.randint(0, 400), random.randint(0, 300))
        circle_radius = 50

        screen.fill(self.WHITE)
        pygame.draw.circle(screen, self.RED, circle_center, circle_radius)
        pygame.display.update()

        start_time = time.time()
        event_found = False

        while not event_found:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    distance = ((mouse_x - circle_center[0]) ** 2 + (mouse_y - circle_center[1]) ** 2) ** 0.5

                    if distance <= circle_radius:
                        end_time = time.time()
                        reaction_time = end_time - start_time
                        self.results.append({"test_no":1,"level":level,"time":reaction_time})
                        event_found = True
                        break

        self.show_result_dialog()


    def introduction(self):
        self.dialog = tk.Toplevel()
        self.dialog.title("Test Decription")
        self.label = tk.Label(self.dialog, text="Your goal is to click on a randomly generated circle")
        self.label.pack()

        self.continue_button = tk.Button(
            self.dialog, text="Continue", command=lambda: [self.dialog.destroy(),self.tutorial_menu()])
        self.continue_button.pack()

        self.dialog.wait_window()


    def run_test(self):
        
        self.introduction()
        for i in range(3):
            self.draw_circle(i+1)

        self.save_results()
        self.show_results()
        pygame.quit()


    def show_result_dialog(self):
        self.dialog = tk.Toplevel()
        self.dialog.title("Test 1 Results")

        for result in self.results:
            label = tk.Label(self.dialog, text=f"Your reaction time is {result['time']:.3f} seconds.")
            label.pack()

        close_button = tk.Button(self.dialog, text="Close", command=self.dialog.destroy)
        close_button.pack()

        self.dialog.wait_window()    


    def show_results(self):
        result_times = []

        for result in self.results:
            result_times.append(result['time'])

        plt.plot(result_times, label='Reaction Time (s)')
        plt.xlabel('Trial')
        plt.ylabel('Reaction Time (s)')
        plt.title('Reaction Time Results')
        plt.legend()
        plt.show()


    def save_results(self):
    
        file_exists = os.path.isfile("Test1_results.csv")
        with open("Test1_results.csv", mode='a', newline='') as csv_file:
            fieldnames = self.results[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    
            if not file_exists:
                writer.writeheader()

            
            for data in self.results:
                writer.writerow(data)