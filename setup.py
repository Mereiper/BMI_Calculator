def setup_win(screen):
    screen.title("BMI Calculator")
    screen.eval('tk::PlaceWindow . center')
    screen.minsize(width=200, height=200)
    screen.maxsize(width=300, height=300)


def setup_label(label, label2, label3):
    label.config(text="Enter your weight (kg)", padx=10, pady=10)
    label2.config(text="Enter your height (cm)", padx=10, pady=10)
    label3.config(padx=10, pady=10)


def setup_entry(entry, entry2):
    entry.config(width=10)
    entry2.config(width=10)


def setup_placement(label, label2, label3, entry, entry2, button):
    label.pack()
    entry.pack()
    label2.pack()
    entry2.pack()
    button.pack()
    label3.pack()


def setup_button(button):
    button.config(text="Calculate")
