from tkinter import *
from time import sleep


def checker(a):
    """check whether the block is under the main block"""
    global block
    coord_start = canvas.coords(rectangle_start_block)
    x, y = coord_start[2]-84.5, coord_start[3]+a
    try:
        coord_block1 = canvas.coords(rectangle_block1)
        if (x >= coord_block1[0] and
             y >= coord_block1[1] and
             x <= coord_block1[2] and
             y <= coord_block1[3] and
             block == False):
            block1_action(int(krok.get()))
            block = True
        else:
            block = False
    except:
        pass
    try:
        coord_block2 = canvas.coords(rectangle_block2)
        if (x >= coord_block2[0] and
             y >= coord_block2[1] and
             x <= coord_block2[2] and
             y <= coord_block2[3] and
             block == False):
            block2_action()
            block = True
        else:
            block = False
    except:
        pass
    try:
        coord_block3 = canvas.coords(rectangle_block3)
        if (x >= coord_block3[0] and
             y >= coord_block3[1] and
             x <= coord_block3[2] and
             y <= coord_block3[3] and
             block == False):
            block3_action(int(subs.get()))
            block = True
        else:
            block = False
    except:
        pass
    try:
        coord_block4 = canvas.coords(rectangle_block4)
        if (x >= coord_block4[0] and
             y >= coord_block4[1] and
             x <= coord_block4[2] and
             y <= coord_block4[3] and
             block == False):
            block4_action(int(zom.get()))
            block = True
        else:
            block = False
    except:
        pass

def action_start():
    x = 20
    for i in range(4): # 4 in this case means the total number of blocks
        checker(x)
        x += 40 # distance between blocks


def start_block(x, y) -> int:
    """we create the main block"""
    global rectangle_start_block
    rectangle_start_block = canvas.create_rectangle(x,y,x+169,y-40, fill="OrangeRed3", tag='start_block')
    canvas.create_text(x+85,y-20, text="if check box then:", fill="white", font=('Helvetica 13'), tag='start_block')


def block1(x, y) -> int:
    """we create a movement block"""
    global rectangle_block1
    rectangle_block1 = canvas.create_rectangle(x,y,x+169,y-40, fill="skyblue", tag='block1')
    canvas.create_text(x+60,y-20, text="move to", fill="white", font=('Helvetica 13'), tag='block1')
    canvas.create_window(x+145,y-20, window=krok, height=25, width=40, tag='block1')

def block1_action(x=1) -> int:
    """the act of walking"""
    for i in range(x):
        sprite_coord = panel.coords(img)
        if rev == False:
            if sprite_coord[0] >= h/3.24:
                panel.move(img, -6,0)
            panel.move(img, 3,0)
        else:
            if sprite_coord[0] <= 100:
                panel.move(img, 6,0)
            panel.move(img, -3,0)
        panel.update_idletasks()
        sleep(.05)
        x -= 1


def block2(x, y) -> int:
    """180 degree turn block"""
    global rectangle_block2
    rectangle_block2 = canvas.create_rectangle(x,y,x+169,y-40, fill="skyblue", tag='block2')
    canvas.create_text(x+85,y-20, text="rotate by 180", fill="white", font=('Helvetica 13'), tag='block2')

def block2_action():
    """action of the second block"""
    global img, rev
    sprite_coord = panel.coords(img)
    panel.delete('sprite')
    if rev == False:
        img = panel.create_image(sprite_coord[0], sprite_coord[1], anchor=CENTER, image=rev_sprite, tag='sprite')
        rev = True
    else:
        img = panel.create_image(sprite_coord[0], sprite_coord[1], anchor=CENTER, image=sprite, tag='sprite')
        rev = False
    panel.update_idletasks()


def block3(x, y) -> int:
    """reduction block"""
    global rectangle_block3
    rectangle_block3 = canvas.create_rectangle(x,y,x+169,y-40, fill="purple", tag='block3')
    canvas.create_text(x+60,y-20, text="reduce in", fill="white", font=('Helvetica 13'), tag='block3')
    canvas.create_window(x+145,y-20, window=subs, height=25, width=40, tag='block3')

def block3_action(x):
    """reduction action"""
    global img, rev, rev_sprite, sprite
    if x != 0:
        sprite_coord = panel.coords(img)
        panel.delete('sprite')
        if rev == True:
            rev_sprite = rev_sprite.subsample(x,x)
            sprite = sprite.subsample(x,x)
            img = panel.create_image(sprite_coord[0], sprite_coord[1], anchor=CENTER, image=rev_sprite, tag='sprite')
        else:
            sprite = sprite.subsample(x,x)
            rev_sprite = rev_sprite.subsample(x,x)
            img = panel.create_image(sprite_coord[0], sprite_coord[1], anchor=CENTER, image=sprite, tag='sprite')


def block4(x, y) -> int:
    """block increase"""
    global rectangle_block4
    rectangle_block4 = canvas.create_rectangle(x,y,x+169,y-40, fill="purple", tag='block4')
    canvas.create_text(x+60,y-20, text="increase in", fill="white", font=('Helvetica 13'), tag='block4')
    canvas.create_window(x+145,y-20, window=zom, height=25, width=40, tag='block4')

def block4_action(x):
    """action of the zoom block"""
    global img, rev, rev_sprite, sprite
    if x != 0:
        sprite_coord = panel.coords(img)
        panel.delete('sprite')
        if rev == True:
            rev_sprite = rev_sprite.zoom(x,x)
            sprite = sprite.zoom(x,x)
            img = panel.create_image(sprite_coord[0], sprite_coord[1], anchor=CENTER, image=rev_sprite, tag='sprite')
        else:
            sprite = sprite.zoom(x,x)
            rev_sprite = rev_sprite.zoom(x,x)
            img = panel.create_image(sprite_coord[0], sprite_coord[1], anchor=CENTER, image=sprite, tag='sprite')


def create_sprite():
    """sprite creation and reset"""
    global img, rev_sprite, sprite, count, rev, block
    count = False
    rev = False
    block = False
    rev_sprite = PhotoImage(file = r'..\res\revers_cat.png')
    sprite = PhotoImage(file = r'..\res\cat.png')
    panel.delete('sprite')
    img = panel.create_image(w/1.8/2.6, h/3.2/2.3, anchor=CENTER, image=sprite, tag='sprite')


def move(self):
    """mouse movement"""
    global count
    try:
        coord_start = canvas.coords(rectangle_start_block)
        if (self.x >= coord_start[0] and
             self.y >= coord_start[1] and
             self.x <= coord_start[2] and
             self.y <= coord_start[3] and
             count == False):
            count = True
            canvas.delete('start_block')
            start_block(self.x-85, self.y+22)
        else:
            count = False
    except:
        pass
    try:
        coord_block1 = canvas.coords(rectangle_block1)
        if (self.x >= coord_block1[0] and
             self.y >= coord_block1[1] and
             self.x <= coord_block1[2] and
             self.y <= coord_block1[3] and
             count == False):
            count = True
            canvas.delete('block1')
            block1(self.x-85, self.y+22)
        else:
            count = False
    except:
        pass
    try:
        coord_block2 = canvas.coords(rectangle_block2)
        if (self.x >= coord_block2[0] and
             self.y >= coord_block2[1] and
             self.x <= coord_block2[2] and
             self.y <= coord_block2[3] and
             count == False):
            count = True
            canvas.delete('block2')
            block2(self.x-85, self.y+22)
        else:
            count = False
    except:
        pass
    try:
        coord_block3 = canvas.coords(rectangle_block3)
        if (self.x >= coord_block3[0] and
             self.y >= coord_block3[1] and
             self.x <= coord_block3[2] and
             self.y <= coord_block3[3] and
             count == False):
            count = True
            canvas.delete('block3')
            block3(self.x-85, self.y+22)
        else:
            count = False
    except:
        pass
    try:
        coord_block4 = canvas.coords(rectangle_block4)
        if (self.x >= coord_block4[0] and
             self.y >= coord_block4[1] and
             self.x <= coord_block4[2] and
             self.y <= coord_block4[3] and
             count == False):
            count = True
            canvas.delete('block4')
            block4(self.x-85, self.y+22)
        else:
            count = False
    except:
        pass


root = Tk()
root.title("Scratch")
root.geometry("1000x650")
root.resizable(False, False)


w = root.winfo_screenheight()
h = root.winfo_screenheight()


canvas = Canvas(root, width=w/1.8, height=h, bg="white")
canvas.pack(side=LEFT)
panel = Canvas(root, width=w/1.8, height=h/3.2, bg="skyblue")
panel.pack(side=TOP)

krok = Entry(canvas, font=('Helvetica 13'))
krok.insert(0, "0")
subs = Entry(canvas, font=('Helvetica 13'))
subs.insert(0, "0")
zom = Entry(canvas, font=('Helvetica 13'))
zom.insert(0, "0")

start_block_btn = Button(canvas, text="if the green flag", bg="OrangeRed3", fg="white",
             font=('Helvetica 12'), command=lambda:start_block(200, 47))
btn_block1 = Button(canvas, text="move n steps", bg="skyblue", fg="white",
             font=('Helvetica 12'), command=lambda:block1(200, 87))
btn_block2 = Button(canvas, text="rotate by 180", bg="skyblue", fg="white",
             font=('Helvetica 12'), command=lambda:block2(200, 127))
btn_block3 = Button(canvas, text="reduce by n times", bg="purple", fg="white",
             font=('Helvetica 12'), command=lambda:block3(200, 167))
btn_block4 = Button(canvas, text="increase by n times", bg="purple", fg="white",
             font=('Helvetica 12'), command=lambda:block4(200, 207))


ico = PhotoImage(file = r'..\res\icon.png')
flag_img = PhotoImage(file = r'..\res\flag.png')
flag_img = flag_img.subsample(45,45)

root.wm_iconphoto(False, ico) # adding an icon to the window

canvas.create_line(193,0,193,h, fill="grey", width=2)
canvas.create_window(95, 30, window=start_block_btn)
canvas.create_window(95, 65, window=btn_block1)
canvas.create_window(95, 100, window=btn_block2)
canvas.create_window(95, 135, window=btn_block3)
canvas.create_window(95, 170, window=btn_block4)

Button(root, image=flag_img, width=35, height=35, command=action_start).pack(side=TOP)
Button(root, text="reset", width=4, height=1, font=('Helvetica 14'),\
        command=create_sprite).pack(side=TOP)

root.bind("<B1-Motion>", move)


if __name__ == "__main__":
    create_sprite()
    root.mainloop()
