import tkinter
import setup

# setups
screen = tkinter.Tk()
setup.setup_win(screen)

label = tkinter.Label()
label2 = tkinter.Label()
setup.setup_label(label=label, label2=label2)

entry = tkinter.Entry()
entry2 = tkinter.Entry()
setup.setup_entry(entry=entry, entry2=entry2)

setup.setup_placement(label=label, label2=label2, entry=entry, entry2=entry2)

screen.mainloop()
