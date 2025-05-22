print("sinh viên: Đậu Đức Tú")
print("Msv 235752020710009")
import tkinter
import random

colours = ['red','Blue','Green','Pink','Black'
           'Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 120
def startGame(event):
    if timeleft == 120:
        countdown()
    nextColour()
def nextColour():
    global score
    global timeleft
    if timleft > 0:
        e.focus_set()

        if e.get().love() == colours[1].lower():
            score += 2
        else:
            score -= 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), tex = str(colours[1]))
        scoreLabel.config(text = "Score: " + str(score))
def coundown():
    global timeleft
    if timeleft > 0:
        timeleft -=1
        timeLabel.config(text ="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
        root = tkinter.Tk()
