from tkinter import *
from time import strftime
from views.commons import Color

#funcs
def time():
    srt_time = strftime('%M:%S %p')
    label_clock.config(text=srt_time)
    label_clock.after(1000, time)

def format_time(min, sec):
    format_min = ['0','0']
    format_sec = ['0','0']
    if min < 10:
        format_min[1] = str(min)
    else:
        format_min = str(min).split()
    if sec < 10:
        format_sec[1] = str(sec)
    else:
        format_sec = str(sec).split()
    return '{min}:{sec}'.format(min=''.join(format_min), sec=''.join(format_sec))


min = None
sec = None

def initial_state():
    global min,sec
    min, sec = None, None
    label_clock.config(text='00:00', fg=Color.sucess, font=("Arial",40))

def tick():
    global min
    global sec
    if sec == None and min == None:
        min = 0
        sec = 0
    if sec == 5:
        label_clock.config(text='Fim do Pomodori',fg=Color.danger, font=("Arial",40))
        label_clock.after(1000, initial_state)
    else:
        sec = sec + 1
        if sec == 60:
            min = min + 1
            sec = 0
        label_clock.config(text=format_time(min, sec))
        label_clock.after(1000, tick)



window = Tk()

# window styles
window.title('PyModoro')
window["bg"] = Color.light
window.resizable(FALSE,FALSE)
window.geometry("700x450+140+100")

# clock container
clock_container = Frame(window, width=500, height=450, background=Color.dark)
clock_container.pack(side=LEFT)
clock_container.pack_propagate(FALSE)

#clock label
label_clock = Label(
    clock_container,
    text="00:00",
    bg=Color.dark,
    fg=Color.sucess,
    font=("Arial",40),
    anchor=CENTER
)
label_clock.pack(side=TOP, padx=10, pady=10)

# log container
log_container = Frame(window, width=200, height=450, background=Color.light)
log_container.pack(side=RIGHT)
log_container.pack_propagate(False)

#control container

controls_container = Frame(clock_container, width=500, height=100, background=Color.dark)
controls_container.pack(side=BOTTOM)
controls_container.pack_propagate(False)

# Start Botton
start_bomtton = Button(
    controls_container,
    width= 20,
    height=2,
    bg=Color.warning,
    fg=Color.dark,
    text="Iniciar",
    font=("Arial",10),
    command=tick
)
start_bomtton.pack(side=LEFT, padx=10, pady=20)

# Pause Botton
Pause_bomtton = Button(
    controls_container,
    width= 20,
    height=2,
    bg=Color.warning,
    fg=Color.dark,
    text="Pause",
    font=("Arial",10)
)
Pause_bomtton.pack(side=RIGHT, padx=10, pady=20)


window.mainloop()
