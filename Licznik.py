from tkinter import *
from tkinter import font
import random

HEIGHT = 600
WIDTH = 600

pl1Life = 20
pl2Life = 20
n =1

number_big = 132
number_small = 80

numberSize = number_big
numberSize2 = number_big

backgrounds = [['black', 'white'],['#1f7a1f', '#ffff00'], ['blue','black'], ['white','black'], ['red','black'], ['#4d4d4d', '#a6a6a6']]

pl1Background = backgrounds[0][0]
pl2Background = backgrounds[0][0]
fontColourPl1 = backgrounds[0][1]
fontColourPl2 = backgrounds [0][1]

def addpl1Life(event):
    global  pl1Life
    pl1Life += 1
    start()

def minuspl1Life(event):
    global pl1Life
    global numberSize
    pl1Life -= 1
    start()

def addpl2Life(event):
    global  pl2Life
    pl2Life += 1
    start()

def minuspl2Life(event):
    global  pl2Life
    pl2Life -= 1
    start()

def reset():
    global pl1Life
    global pl2Life
    pl1Life = 20
    pl2Life = 20
    start()

def commander():
    global pl1Life
    global pl2Life
    pl1Life = 40
    pl2Life = 40
    start()

def changeColorPl1():
    global n
    if n == 6:
        n = 0
    else:
        pass
    global pl1Background
    pl1Background = backgrounds[0+n][0]
    global fontColourPl1
    fontColourPl1 = backgrounds[0+n][1]
    n += 1
    start()

def changeColorPl2():
    global n
    if n == 6:
        n = 0
    else:
        pass
    global pl2Background
    pl2Background = backgrounds[0+n][0]
    global fontColourPl2
    fontColourPl2 = backgrounds[0+n][1]
    n += 1
    start()

def rollDice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    global pl1Life
    pl1Life = roll1 + roll2
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    global pl2Life
    pl2Life = roll3 + roll4
    start()

root = Tk()

backgroung_image = PhotoImage(file='lifeCounter.png')
color_image = PhotoImage(file='changeColor.png')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def start():
    if pl1Life < -99 or pl1Life > 99:
        global numberSize
        numberSize = number_small
    else:
        numberSize = number_big

    if pl2Life < -99 or pl2Life > 99:
        global numberSize2
        numberSize2 = number_small
    else:
        numberSize2 = number_big


    myfont = font.Font(family='Apple Chancery', size=15, weight='bold')
    myfontNumbers1 = font.Font(family='Arial Black', size=numberSize, weight='bold')
    myfontNumbers2 = font.Font(family='Arial Black', size=numberSize2, weight='bold')

    frameOptions = Frame(root, bg='black')
    frameOptions.place(x=0, y=0, relwidth=1, relheight=0.20)

    backgroung_label = Label(frameOptions, image=backgroung_image)
    backgroung_label.place(relwidth=1, relheight=1)

    resetButton = Button(frameOptions, text='Reset', font=myfont, command=lambda: reset())
    resetButton.place(relx=0.05, rely=0.15)

    commanderButton = Button(frameOptions, text='Commander', font=myfont, command=lambda: commander())
    commanderButton.place(relx=0.05, rely=0.5)

    rollDiceButton = Button(frameOptions, text='Roll Dice', font=myfont, command=lambda: rollDice())
    rollDiceButton.place(relx=0.85, rely=0.15)

    framePlayer1 = Frame(root, bg=pl1Background)
    framePlayer1.place(x=0, rely=0.20, relwidth=0.5, relheight=1)

    framePl1Minus = Frame(framePlayer1, bg=pl1Background)
    framePl1Minus.focus_set()
    framePl1Minus.place(x=0, rely=0.0, relwidth=0.5, relheight=1)
    framePl1Minus.bind("<Button-1>", minuspl1Life)
    framePl1Add = Frame(framePlayer1, bg=pl1Background)
    framePl1Add.focus_set()
    framePl1Add.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
    framePl1Add.bind("<Button-1>", addpl1Life)

    labelPl1 = Label(framePlayer1, text=str(pl1Life), bg=pl1Background, fg=fontColourPl1, font=myfontNumbers1)
    labelPl1.place(relx=0.15, rely=0.25, relwidth=0.70, relheight=0.30)

    colorButton1 = Button(framePlayer1, image=color_image, command=lambda: changeColorPl1())
    colorButton1.place(relx=0.06, rely=0.03, relwidth=0.25, relheight=0.1)

    framePlayer2 = Frame(root, bg=pl2Background)
    framePlayer2.place(relx=0.5, rely=0.20, relwidth=0.5, relheight=1)

    framePl2Minus = Frame(framePlayer2, bg=pl2Background)
    framePl2Minus.focus_set()
    framePl2Minus.place(x=0, rely=0.0, relwidth=0.5, relheight=1)
    framePl2Minus.bind("<Button-1>", minuspl2Life)
    framePl2Add = Frame(framePlayer2, bg=pl2Background)
    framePl2Add.focus_set()
    framePl2Add.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
    framePl2Add.bind("<Button-1>", addpl2Life)


    labelPl2 = Label(framePlayer2, text=str(pl2Life), bg=pl2Background, fg=fontColourPl2, font=myfontNumbers2)
    labelPl2.place(relx=0.15, rely=0.25, relwidth=0.70, relheight=0.30)

    colorButton2 = Button(framePlayer2, image=color_image, command=lambda: changeColorPl2())
    colorButton2.place(relx=0.70, rely=0.03, relwidth=0.25, relheight=0.1)


start()

root.mainloop()