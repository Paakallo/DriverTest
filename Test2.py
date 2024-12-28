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



class Test2:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Test 2")
        self.p= pyaudio.PyAudio()

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.RANDOM = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

        self.fs= 44100 #sampling rate

        duration = 0.5
        f1 = 500
        f2 = 1000
        t= np.linspace(0, duration, int(duration * self.fs), False)  # time array

        self.audio_stimulus1 = np.sin(f1 * 2 * np.pi * t)  # audio stimulus 1 (sine wave)
        self.audio_stimulus2 = np.sin(f2 * 2 * np.pi * t)  # audio stimulus 2 (sine wave)

        self.results = []


    def audio_stimulus(self,stimuli):
        stream = self.p.open(format=pyaudio.paFloat32, channels=1, rate=self.fs, output=True)
        stream.write(stimuli.astype(np.float32).tobytes())
        stream.stop_stream()
        stream.close()


    def cool_down(self,wait1:time.time, endtime:int):
        wait_time = 0
        while wait_time < endtime + 1:
            wait2 = time.time()
            wait_time = wait2 - wait1
            if wait_time >= endtime:
                break
 

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
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.RANDOM, (350, 250, 100, 100))
        pygame.display.update()

        event_found = False
        while not event_found:
            events = pygame.event.get()
            for event in events:          
                if event.type == pygame.MOUSEBUTTONDOWN:
                    event_found = True
                    break
        self.screen.fill(self.BLACK)
        
        self.dialog = tk.Toplevel()
        self.dialog.title("Tutorial")
        
        self.no_button = tk.Button(self.dialog, text="Continue", command=self.dialog.destroy)
        self.no_button.pack()

        self.dialog.wait_window()


    def init_level(self,duration:int,stimulus):
        # wait n sec
        self.cool_down(time.time(),duration)

        start_time = time.time()
        self.audio_stimulus(stimulus)
        return start_time


    def run_level(self, color, stimulus, duration, level):
        self.screen.fill(self.WHITE)

        # Randomize rectangle position
        rect_x = random.randint(0, 700)  # Ensure the rectangle fits within the screen width
        rect_y = random.randint(0, 500)  # Ensure the rectangle fits within the screen height
        rect_width, rect_height = 100, 100  # Rectangle size

        # Draw the rectangle
        pygame.draw.rect(self.screen, color, (rect_x, rect_y, rect_width, rect_height))
        pygame.display.update()

        # Play audio after a delay
        start_time = None
        pygame.time.delay(int(duration * 1000))  # Wait before playing audio
        self.audio_stimulus(stimulus)
        start_time = time.time()

        # Wait for user interaction
        event_found = False
        while not event_found:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Check if the click is inside the rectangle
                    if rect_x <= mouse_x <= rect_x + rect_width and rect_y <= mouse_y <= rect_y + rect_height:
                        reaction_time = time.time() - start_time
                        self.results.append({"test_no": 2, "level": level, "time": reaction_time})
                        event_found = True
        
        

    def first_level(self):
        self.run_level(self.RED,self.audio_stimulus1,2,1)      

    def second_level(self):
        self.run_level(self.GREEN,self.audio_stimulus2,1,2)

    def third_level(self):
        self.run_level(self.BLUE,self.audio_stimulus2,0.75,3)


    def game_loop(self):
        first_check = False
        second_check = False
        third_check = False

        self.tutorial_menu()
        self.cool_down(time.time(),1)

        while True:
            if not first_check:
                self.first_level()
                first_check = True

            elif not second_check:
                self.second_level()
                second_check = True

            elif not third_check:
                self.third_level()
                third_check = True

            if first_check and second_check and third_check:
                self.save_results()
                self.show_results()
                pygame.quit()
                break
    

    def save_results(self):
        
        file_exists = os.path.isfile("test2.csv")
        with open("test2.csv", mode='a', newline='') as csv_file:
            fieldnames = self.results[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                  
            if not file_exists:
                writer.writeheader()
  
           
            for data in self.results:
                writer.writerow(data)


    def show_result_dialog(self):
        self.dialog = tk.Toplevel()
        self.dialog.title("Test 2 Results")

        for result in self.results:
            label = tk.Label(self.dialog, text=f"Your reaction time is {result['time']:.3f} seconds.")
            label.pack()

        # Dodanie przycisku zamykającego
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
