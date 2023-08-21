import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import winsound
import time
import random
import sys

class Pet:
    def __init__(self):
        
        self.window = tk.Tk()

        self.walking_right = [tk.PhotoImage(file='moving.gif', format='gif -index %i' % i) for i in range(12)]
        self.walking_left = [tk.PhotoImage(file='moving-2.gif', format='gif -index %i' % i) for i in range(12)]
        self.idle = [tk.PhotoImage(file='idle.gif', format='gif -index %i' % i) for i in range(16)]
        self.sit = [tk.PhotoImage(file='sit.gif', format='gif -index %i' % i) for i in range(2)]
        self.drag = [tk.PhotoImage(file='drag.gif', format='gif -index %i' % i) for i in range(3)]
        self.land = [tk.PhotoImage(file='land.gif', format='gif -index %i' % i) for i in range(20)]
        self.dance1 = [tk.PhotoImage(file='dance-1.gif', format='gif -index %i' % i) for i in range(11)]
        self.dance2 = [tk.PhotoImage(file='dance-2.gif', format='gif -index %i' % i) for i in range(14)]
        self.fuckyou = [tk.PhotoImage(file='fuckyou.gif', format='gif -index %i' % i) for i in range(8)]
        self.happy = [tk.PhotoImage(file='happy.gif', format='gif -index %i' % i) for i in range(13)]
        self.frame_index = 0
        
        self.x = (self.window.winfo_screenwidth() // 2) + random.randint(-self.window.winfo_screenwidth() // 3, self.window.winfo_screenwidth() // 3)
        self.y = (self.window.winfo_screenheight() // 2) + random.randint(-self.window.winfo_screenheight() // 3, self.window.winfo_screenheight() // 3)
        self.img = self.walking_right[self.frame_index]
        self.pause_duration = 250
        self.direction = random.choices(['dance1', 'dance2'], weights=[1, 1])[0]

        self.timestamp = time.time()
        self.window.config(highlightbackground='green')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'green')
        self.label = tk.Label(self.window, bd=0, bg='green')
        self.label.configure(image=self.img)
        self.label.pack()
        self.is_dragging = False
        self.window.bind("<Button-1>", self.on_start_drag)
        self.window.bind("<B1-Motion>", self.on_drag)
        self.window.bind("<ButtonRelease-1>", self.on_stop_drag)
        self.window.after(0, self.update)
        self.window.mainloop()

    def on_start_drag(self, event):
        self.start_x = event.x_root
        self.start_y = event.y_root
        self.offset_x = self.window.winfo_x()
        self.offset_y = self.window.winfo_y()
        winsound.PlaySound("grab.wav", winsound.SND_ASYNC)
        self.is_dragging = True

    def on_drag(self, event):
        self.x = self.offset_x + (event.x_root - self.start_x)
        self.y = self.offset_y + (event.y_root - self.start_y)

    def on_stop_drag(self, event):
        self.is_dragging = False
        winsound.PlaySound("let.wav", winsound.SND_ASYNC)

    def update(self):
        if self.pause_duration <= 0:
            self.direction = random.choices(['up', 'down', 'left', 'right', 'none', 'sit', 'dance1', 'dance2', 'fuckyou', 'happy'], weights=[2.5, 2.1, 2.4, 2.3, 4, 2.75, 0.25, 0.25, 1, 1])[0]
            self.pause_duration = random.randint(25, 120)
        if self.is_dragging == False:
            if self.direction == 'right':
                if self.x < self.window.winfo_screenwidth() - 100:
                    self.x += 3
                else:
                    self.pause_duration = 0
                if self.img not in self.walking_right:
                    self.frame_index = 0
                self.img = self.walking_right[self.frame_index]
            elif self.direction == 'left':
                if self.x > 0:
                    self.x -= 3
                else:
                    self.pause_duration = 0
                if self.img not in self.walking_left:
                    self.frame_index = 0
                self.img = self.walking_left[self.frame_index]
            elif self.direction == 'up':
                if self.y > 0:
                    self.y -= 3
                else:
                    self.pause_duration = 0
                if self.img not in self.walking_right:
                    self.frame_index = 0
                self.img = self.walking_right[self.frame_index]
            elif self.direction == 'down':
                if self.y < self.window.winfo_screenheight() - 100:
                    self.y += 3
                else:
                    self.pause_duration = 0
                if self.img not in self.walking_right:
                    self.frame_index = 0
                self.img = self.walking_right[self.frame_index]
            elif self.direction == 'none':
                if self.img not in self.idle:
                    self.frame_index = 0
                self.img = self.idle[self.frame_index]
            elif self.direction == 'land':
                if self.img not in self.land:
                    self.frame_index = 0
                self.img = self.land[self.frame_index]
            elif self.direction == 'dance1':
                if self.img not in self.dance1:
                    self.frame_index = 0
                    self.pause_duration = 250
                    winsound.PlaySound("dance.wav", winsound.SND_ASYNC)
                self.img = self.dance1[self.frame_index]
            elif self.direction == 'dance2':
                if self.img not in self.dance2:
                    self.frame_index = 0
                    self.pause_duration = 250
                    winsound.PlaySound("dance.wav", winsound.SND_ASYNC)
                self.img = self.dance2[self.frame_index]
            elif self.direction == 'sit':
                if self.img not in self.sit:
                    winsound.PlaySound("woag.wav", winsound.SND_ASYNC)
                    self.frame_index = 0
                self.img = self.sit[self.frame_index]
            elif self.direction == 'fuckyou':
                if self.img not in self.fuckyou:
                    winsound.PlaySound("woag2.wav", winsound.SND_ASYNC)
                    self.frame_index = 0
                self.img = self.fuckyou[self.frame_index]
            elif self.direction == 'happy':
                if self.img not in self.happy:
                    winsound.PlaySound("woag3.wav", winsound.SND_ASYNC)
                    self.frame_index = 0
                self.img = self.happy[self.frame_index]
        else:
            self.direction = 'land'
            self.pause_duration = 20
            if self.img not in self.drag:
                self.frame_index = 0
            self.img = self.drag[self.frame_index]

        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            if self.img in self.walking_right or self.img in self.walking_left:
                frame_length = len(self.walking_right)
            elif self.img in self.idle:
                frame_length = len(self.idle)
            elif self.img in self.sit:
                frame_length = len(self.sit)
            elif self.img in self.drag:
                frame_length = len(self.drag)
            elif self.img in self.land:
                frame_length = len(self.land)
            elif self.img in self.dance1:
                frame_length = len(self.dance1)
            elif self.img in self.dance2:
                frame_length = len(self.dance2)
            elif self.img in self.fuckyou:
                frame_length = len(self.fuckyou)
            elif self.img in self.happy:
                frame_length = len(self.happy)
            self.frame_index = (self.frame_index + 1) % frame_length

        self.pause_duration -= 1
        self.window.geometry('100x100+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(10, self.update)

pet_selector = Pet()
