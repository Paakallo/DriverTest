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

from Test1 import Test1
from Test2 import Test2
sys.setrecursionlimit(10000)

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
