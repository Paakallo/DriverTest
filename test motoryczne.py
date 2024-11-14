import sys
import tkinter as tk
from tkinter import messagebox
import pygame
import time
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt


sys.setrecursionlimit(10000)
# class show_test2:
#     def test_2(self):
#         pygame.init()
#         p= pyaudio.PyAudio()

#         screen = pygame.display.set_mode((800, 600))
#         pygame.display.set_caption("Test 2")

#         WHITE = (255, 255, 255)
#         BLACK = (0, 0, 0)
#         RED = (255, 0, 0)

#         fs= 44100 #sampling rate
#         duration = 0.5
#         f1 = 500
#         f2 = 1000
#         t= np.linspace(0, duration, int(duration * fs), False)  # time array
#         audio_stimulus1 = np.sin(f1 * 2 * np.pi * t)  # audio stimulus 1 (sine wave)
#         audio_stimulus2 = np.sin(f2 * 2 * np.pi * t)  # audio stimulus 2 (sine wave)

#         screen.fill(WHITE)

#         pygame.draw.rect(screen, RED, (350, 250, 100, 100))

#         stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
#         stream.write(audio_stimulus1.astype(np.float32).tobytes())
#         stream.stop_stream()
#         stream.close()

#         pygame.display.update()
#         pygame.display.flip()

#         start_time = time.time()
#         event_found = False
#         while not event_found:
#              for event in pygame.event.get():
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     end_time = time.time()
#                     reaction_time3 = end_time - start_time
#                     event_found = True
#                     break
            

        
#         screen.fill(WHITE)

#         # draw a red circle
#         pygame.draw.circle(screen, RED, (400, 300), 50)

#         # play audio stimulus 2
#         stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
#         stream.write(audio_stimulus2.astype(np.float32).tobytes())
#         stream.stop_stream()
#         stream.close()

#         # update the screen
#         pygame.display.update()
#         pygame.display.flip()

#         # wait for a reaction
#         start_time = time.time()
#         event_found = False
#         while not event_found:
#             for event in pygame.event.get():
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     end_time = time.time()
#                     reaction_time2 = end_time - start_time
#                     event_found = True
#                     break

        
#         # calculate average reaction time and display it'
#         self.dialog = tk.Toplevel()
#         self.dialog.geometry("800x300")

#         self.label= tk.Label(self.dialog, text= f"Your reaction time in test 1 is {reaction_time3:.3f} seconds.")
#         self.label.pack()

#         self.label= tk.Label(self.dialog, text= f"Your reaction time in test 2 is {reaction_time2:.3f} seconds.")
#         self.label.pack()

#         total_reaction_time = reaction_time3 + reaction_time2
#         self.label= tk.Label(self.dialog, text= f"Your total reaction time is {total_reaction_time:.3f} seconds.")
#         self.label.pack()
        
#         avg_reaction_time = (reaction_time3 + reaction_time2) / 2
#         self.label= tk.Label(self.dialog,text=f"Your average reaction time is {avg_reaction_time:.3f} seconds.")
#         self.label.pack()
#         self.close_button = tk.Button(self.dialog, text="Close", command=self.close_dialog3)
#         self.close_button.pack()

#          # clean up Pygame and Pyaudio
#         p.terminate()
#         pygame.quit()


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

        self.start_button = tk.Button(master, text="Show results", command=self.show_results)
        self.start_button.pack()

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

        test2_button = tk.Button(self.menu, text="Test 2", command=self.test_2)
        test2_button.pack()

    def test_1(self):
        # initialize pygame
        pygame.init()
        # Tu jest kod
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

    def close_dialog1(self):
        self.dialog.destroy()
        pygame.quit() 
            
    def test_2(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Test 2")
        p= pyaudio.PyAudio()

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)

        fs= 44100 #sampling rate
        duration = 0.5
        f1 = 500
        f2 = 1000
        t= np.linspace(0, duration, int(duration * fs), False)  # time array
        audio_stimulus1 = np.sin(f1 * 2 * np.pi * t)  # audio stimulus 1 (sine wave)
        audio_stimulus2 = np.sin(f2 * 2 * np.pi * t)  # audio stimulus 2 (sine wave)

        screen.fill(WHITE)

        pygame.draw.rect(screen, RED, (350, 250, 100, 100))

        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
        stream.write(audio_stimulus1.astype(np.float32).tobytes())
        stream.stop_stream()
        stream.close()

        pygame.display.update()
        pygame.display.flip()

        start_time = time.time()
        event_found = False
        while not event_found:
             for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end_time = time.time()
                    reaction_time3 = end_time - start_time
                    event_found = True
                    break
            

        
        screen.fill(WHITE)

        # draw a red circle
        pygame.draw.circle(screen, RED, (400, 300), 50)

        # play audio stimulus 2
        stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
        stream.write(audio_stimulus2.astype(np.float32).tobytes())
        stream.stop_stream()
        stream.close()

        # update the screen
        pygame.display.update()
        pygame.display.flip()

        # wait for a reaction
        start_time = time.time()
        event_found = False
        while not event_found:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end_time = time.time()
                    reaction_time2 = end_time - start_time
                    event_found = True
                    break

        
        # calculate average reaction time and display it'
        self.dialog = tk.Toplevel()
        self.dialog.geometry("400x300")

        self.label= tk.Label(self.dialog, text= f"Your reaction time in test 1 is {reaction_time3:.3f} seconds.")
        self.label.pack()

        self.label= tk.Label(self.dialog, text= f"Your reaction time in test 2 is {reaction_time2:.3f} seconds.")
        self.label.pack()

        total_reaction_time = reaction_time3 + reaction_time2
        self.label= tk.Label(self.dialog, text= f"Your total reaction time is {total_reaction_time:.3f} seconds.")
        self.label.pack()
        
        avg_reaction_time = (reaction_time3 + reaction_time2) / 2
        self.label= tk.Label(self.dialog,text=f"Your average reaction time is {avg_reaction_time:.3f} seconds.")
        self.label.pack()
        self.close_button = tk.Button(self.dialog, text="Close", command=self.close_dialog1)
        self.close_button.pack()
    #TODO: Trzeba przerobić funckję od zera
    # def show_results(self):
    #     accuracy = (correct / total) * 100
    #     print(f"Accuracy: {accuracy:.2f}%")
    #     precision = (tp / (tp + fp)) * 100
    #     print(f"Precision: {precision:.2f}%")
    #     recall = (tp / (tp + fn)) * 100
    #     print(f"Recall: {recall:.2f}%")

    #     # create a bar chart to display results
    #     labels = ["Accuracy", "Precision", "Recall"]
    #     values = [accuracy, precision, recall]
    #     plt.bar(labels, values)
    #     plt.title("Results")
    #     plt.ylabel("Percentage")
    #     plt.show()
    
         


         
root = tk.Tk()
app = MainWindow(root)
root.mainloop()