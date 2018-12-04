#!/usr/bin/python 
import tkinter as tk
from time import time,sleep
from PIL import Image,ImageTk
from random import choice,uniform,randint
from math import sin,cos,radians

root = tk.Tk()
w = tk.Label(root,text='Love Ling !')
w.pack()
root.mainloop()

GRAVITY = 0.05
colors= ['red','blue','yellow','white','green','orange','purple','seagreen','indigo','cornflowerblue']
class Particle:
    def __init__(self,cv,idx,total,explosion_speed,x=0.,y=0.,vx=0.,vy=0.,size=2.,color='red',    lifespan=2,**kwags):
        self.id = idx
        self.x = x 
        self.y = y
        self.initial_speed = explosion_speed
        self.vx = vx
        self.vy = vy
        self.total = total
        self.age = 0
        self.color = color
        self.cv = cv
        self.lifespan = lifespan
        self.cid = self.cv.create_oval( x - size ,y - size ,x + size ,y + size, fill = self.color)
    def update(self,dt):
        self.age += dt 
        if self.alive() and self.expand():
            move_x = cos(radians(self.id*360/self.total))*self.initial_speed
            move_y = sin(radians(self.id*360/self.total))*self.initial_speed
            self.vx = move_x/(float(dt)*1000)
            self.vy = move_y/(float(dt)*1000)
            self.cv.move(self.cid,move_x,move_y)
        elif self.alive():
            move_x = cos(radians(self.id*360/self.total))
            self.cv.move(self.cid, self.vx + move_x, self.vy + GRAVITY * dt)
            self.vy += GRAVITY * dt
        elif self.cid is not None :
            cv.delete(self.cid)
            self.cid = None
    def expand(self):
        return self.age <= 1.2
    def alive(self):
        return self.age <= self.lifespan
       
def simulate(cv):
    t = time()
    explode_points = []
    wait_time = randint(10,100)
    numb_explode = randint(6,10)
    for point in range(numb_explode):
        objecks = []
        x_cordi = randint(50,550)
        y_cordi = randint(50,150)
        speed = uniform(0.5,1.5)
        size = uniform(0.5,3)
        color = choice(colors) 
        explosion_speed = uniform(0.2,1)
        total_particles = randint(10,50)
        for i in range(1,total_particles):
            r = Particle(cv,idx=i,total=total_particles,explosion_speed=explosion_speed,x=x_cordi,y=y_cordi,vx=speed,vy=speed,color=color,size=size,lifespan=uniform(0.6,1.75))
            objecks.append(r)
        explode_points.append(objecks)
    total_time = 0.
    while total_time < 1.8 :
        sleep(0.01)
        tnew = time()
        t,dt = tnew,tnew - t
        for point in explode_points:
            for item in point:
                item.update(dt)
        cv.update()
        total_time += dt
    root.after(wait_time,simulate,cv)
def close(*ignore):
    global root
    root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    cv = tk.Canvas(root,heigh=529,width=800)
    image = Image.open("./image.jpg")
    photo=ImageTk.PhotoImage(image)
    cv.create_image(0,0,image=photo,anchor='nw')
    cv.pack()
    root.protocol("WM_DELETE_WINDOW",close)
    root.after(100,simulate,cv)
    root.mainloop()
    
    
       
       