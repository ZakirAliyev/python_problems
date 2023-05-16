import tkinter as tk
import pygame

pygame.init()
pygame.mixer.init()


def play_do():
    pygame.mixer.Sound("do.wav").play()


def play_re():
    pygame.mixer.Sound("re.wav").play()


def play_mi():
    pygame.mixer.Sound("mi.wav").play()


def play_fa():
    pygame.mixer.Sound("fa.wav").play()


def play_sol():
    pygame.mixer.Sound("sol.wav").play()


def play_la():
    pygame.mixer.Sound("la.wav").play()


def play_si():
    pygame.mixer.Sound("si.wav").play()


root = tk.Tk()
root.title("Piano")

button_do = tk.Button(root, command=play_do, width=20, height=40)
button_do.grid(row=0, column=1)

button_re = tk.Button(root, command=play_re, width=20, height=40)
button_re.grid(row=0, column=2)

button_mi = tk.Button(root, command=play_mi, width=20, height=40)
button_mi.grid(row=0, column=3)

button_fa = tk.Button(root, command=play_fa, width=20, height=40)
button_fa.grid(row=0, column=4)

button_sol = tk.Button(root, command=play_sol, width=20, height=40)
button_sol.grid(row=0, column=5)

button_la = tk.Button(root, command=play_la, width=20, height=40)
button_la.grid(row=0, column=6)

button_si = tk.Button(root, command=play_si, width=20, height=40)
button_si.grid(row=0, column=7)

button_1 = tk.Button(root, command=play_re, width=10, height=25, bg="black")
button_1.place(x=108, y=0)

button_2 = tk.Button(root, command=play_mi, width=10, height=25, bg="black")
button_2.place(x=260, y=0)

button_3 = tk.Button(root, command=play_sol, width=10, height=25, bg="black")
button_3.place(x=558, y=0)

button_4 = tk.Button(root, command=play_la, width=10, height=25, bg="black")
button_4.place(x=708, y=0)

button_5 = tk.Button(root, command=play_si, width=10, height=25, bg="black")
button_5.place(x=858, y=0)

root.mainloop()
