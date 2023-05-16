import tkinter


def setup_win(screen):
    screen.title("BMI Calculator")
    screen.eval('tk::PlaceWindow . center')
    screen.minsize(width=200, height=200)
    screen.maxsize(width=400, height=400)
