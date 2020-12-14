# Python program to illustrate a stop watch
# using Tkinter
# importing the required libraries
import tkinter as Tkinter
from datetime import datetime
from pygame import mixer
mixer.init()
mixer.music.load(r'C:\Users\kumarsa\Desktop\music'+ r'/Dus.mp3')

counter = 6
running = False


def counter_label(label):
    def count():
        global running
        if running:
            global counter

            # To manage the initial delay.
            if counter == 6:
                display = "Starting..."
            if counter == 0:
                # global running
                running = False  ##khel##
                display = (datetime.utcfromtimestamp(counter)).strftime("%H:%M:%S")
                # stop['state'] = 'disabled'
                start['state'] = 'normal'
                counter = 6
                mixer.music.play()
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string

            label['text'] = display  # Or label.config(text=display)

            # label.after(arg1, arg2) delays by
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count)  # recursion
            counter -= 1

    # Triggering the start of the counter.
    count()


# start function of the stopwatch
def Start(label):
    global running
    running = True
    global counter
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# Stop function of the stopwatch
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False
    mixer.music.stop()


# Reset function of the stopwatch
def Reset(label):
    global counter
    counter = 6

    # If rest is pressed after pressing stop.
    if not running:
        reset['state'] = 'disabled'
        label['text'] = 'Duolingo!'

    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'


root = Tkinter.Tk()
root.title("Duolingo Timer")

# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(
    root,
    text="Duolingo!",
    fg="black",
    font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(
    f,
    text='Reset',
    width=6,
    state='disabled',
    command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
root.mainloop()
