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

sys.setrecursionlimit(10000)

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
        self.label = tk.Label(self.dialog, text=f"Do you want to go through a tutorial")
        self.label.pack()

        self.yes_button = tk.Button(self.dialog, text="Yes", command=self.tutorial)
        self.yes_button.pack()

        self.no_button = tk.Button(self.dialog, text="No", command=self.dialog.destroy)
        self.no_button.pack()


    def tutorial(self):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.RANDOM, (350, 250, 100, 100))
        pygame.display.update()

        init = False
        event_found = False
        while not event_found:
            events = pygame.event.get()
            for event in events:

                if not init:
                    start_time= self.init_level(5,self.audio_stimulus1)
                    init = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    event_found = True
                    break
        self.screen.fill(self.BLACK)
        

    def init_level(self,duration:int,stimulus):
        # wait n sec
        self.cool_down(time.time(),duration)

        start_time = time.time()
        self.audio_stimulus(stimulus)
        return start_time


    def first_level(self):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.RED, (350, 250, 100, 100))
        pygame.display.update()

        init = False
        start_time = 0
        event_found = False
        while not event_found:
            events = pygame.event.get()
            for event in events:

                if not init:
                    start_time= self.init_level(5,self.audio_stimulus1)
                    init = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    end_time = time.time()
                    reaction_time = end_time - start_time
                    self.results.append(reaction_time)
                    event_found = True
                    break
            

    def second_level(self):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.GREEN, (350, 250, 100, 100))
        pygame.display.update()

        init = False
        start_time = 0
        event_found = False
        while not event_found:
            events = pygame.event.get()
            for event in events:
                
                if not init:
                    start_time= self.init_level(3,self.audio_stimulus2)
                    init = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    end_time = time.time()
                    reaction_time = end_time - start_time
                    self.results.append(reaction_time)
                    event_found = True
                    break


    def third_level(self):
        self.screen.fill(self.WHITE)
        pygame.draw.rect(self.screen, self.BLUE, (350, 250, 100, 100))
        pygame.display.update()

        init = False
        start_time = 0
        event_found = False
        while not event_found:
            events = pygame.event.get()
            for event in events:
                
                if not init:
                    start_time= self.init_level(1,self.audio_stimulus2)
                    init = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    end_time = time.time()
                    reaction_time = end_time - start_time
                    self.results.append(reaction_time)
                    event_found = True
                    break


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
                pygame.quit()
                break
    
    def get_result(self):
        return self.results
    

    
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
    def __init__(self, master):
        self.master = master
        master.title("Psychomotor Fitness Tester")
        master.geometry("400x200")
        

        self.label = tk.Label(master, text="Welcome to the Psychomotor Fitness Tester!")
        self.label.pack()

        self.introduction_button = tk.Button(master, text="Introduction", command=self.show_introduction)
        self.introduction_button.pack()
      
        self.start_button = tk.Button(master, text="Start Testing", command=self.show_menu)
        self.start_button.pack()

        # self.start_button = tk.Button(master, text="Show results", command=self.show_results)
        # self.start_button.pack()

        self.menu = None
       
    def show_introduction(self):
        self.intro = IntroductionDialog(self.master)

    
    def show_menu(self):
        if self.menu is not None:
            self.menu.destroy()

        self.menu = tk.Frame(self.master)
        self.menu.pack()

        test1_button = tk.Button(self.menu, text="Test 1", command=self.test_1)
        test1_button.pack()

        test2_button = tk.Button(self.menu, text="Test 2", command=self.start_test2)
        test2_button.pack()

    def test_1(self):
        # initialize pygame
        pygame.init()

        # set up the window
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Test 1")

        # set up the colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)

        #  draw a white background
        screen.fill(WHITE)

        # draw a red circle
        pygame.draw.circle(screen, RED, (400, 300), 50)

        # update the screen
        pygame.display.update()

        
            

        # wait for a reaction
        start_time = time.time()
        event_found = False
        while not event_found:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end_time = time.time()
                    reaction_time = end_time - start_time
                    self.dialog = tk.Toplevel()
                    self.dialog.title("Test 1 Results")
                    self.label = tk.Label(self.dialog, text=f"Your reaction time is {reaction_time:.3f} seconds.")
                    self.label.pack()
                    self.close_button = tk.Button(self.dialog, text="Close", command=self.close_dialog1)
                    self.close_button.pack()
                    event_found = True
                    break


            
    def start_test2(self):
        game2 = Test2()
        game2.game_loop()


         
root = tk.Tk()
app = MainWindow(root)
root.mainloop()