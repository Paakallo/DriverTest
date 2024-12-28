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

sys.setrecursionlimit(10000)

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


    def run_test(self):
        
        self.tutorial_menu()
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
    
        file_exists = os.path.isfile("test1.csv")
        with open("test1.csv", mode='a', newline='') as csv_file:
            fieldnames = self.results[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    
            if not file_exists:
                writer.writeheader()

            
            for data in self.results:
                writer.writerow(data)


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


    # def run_level(self,color,stimulus, duration,level):
    #     self.screen.fill(self.WHITE)

    #     rect_center = (random.randint(0, 800), random.randint(0, 600))
    #     rect_length = 100

    #     pygame.draw.rect(self.screen, color, (rect_center[0], rect_center[1], rect_length, rect_length))
    #     pygame.display.update()

    #     init = False
    #     start_time = 0
    #     event_found = False
    #     while not event_found:
    #         events = pygame.event.get()
    #         for event in events:

    #             if not init:
    #                 start_time= self.init_level(duration,stimulus)
    #                 init = True

    #             if event.type == pygame.MOUSEBUTTONDOWN:

    #                 mouse_x, mouse_y = event.pos
    #                 distance = ((mouse_x - rect_center[0]) ** 2 + (mouse_y - rect_center[1]) ** 2) ** 0.5

    #                 # it's similar to a radius
    #                 if distance <= rect_length/2:

    #                     end_time = time.time()
    #                     reaction_time = end_time - start_time
    #                     self.results.append({"test_no":2,"level":level,"time":reaction_time})
    #                     event_found = True
    #                     break

    #     self.show_result_dialog()

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
        self.dialog.title("Test 1 Results")

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


class IntroductionDialog:
    def __init__(self, parent):
        self.parent = parent

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Introduction")
        self.dialog.geometry("800x300")
        

        self.label = tk.Label(self.dialog, text="Welcome to the Psychomotor Fitness Tester!\n\nThis application is designed to test your reaction time to optical and acoustic stimuli.\n\n Before starting the tests, please read the following information carefully:\n\nThe test consists of a series of different tests examining simple and complex reaction time to optical and acoustic stimuli.\n\n Every proper test should be preceded by information about the course of the test and the training phase,\n\n during which the tested person will perform the same activities as in during the test, but not graded.\n\n After performing a series of tests, the person subjected to the tests should be informed about the results achieved in a synthetic and analytical form \n\n using numerical values ​​and graphical representation.\n\nClick 'OK' to continue.")
        self.label.pack()

        self.button = tk.Button(self.dialog, text="OK",command=self.close_dialog)
        self.button.pack()

        
    def close_dialog(self):
        self.dialog.destroy()


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Psychomotor Fitness Tester")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Welcome to the Psychomotor Fitness Tester!")
        self.label.pack()

        self.introduction_button = tk.Button(self, text="Introduction", command=self.show_introduction)
        self.introduction_button.pack()

        self.test1_button = tk.Button(self, text="Start Test 1", command=self.start_test1)
        self.test1_button.pack()

        self.test2_button = tk.Button(self, text="Start Test 2", command=self.start_test2)
        self.test2_button.pack()

    def show_introduction(self):
        self.intro = IntroductionDialog(self)

    def start_test1(self):
        test1 = Test1(self)  # Przekazanie rodzica tkinter
        test1.run_test()

    def start_test2(self):
        game2 = Test2()
        game2.game_loop()



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
