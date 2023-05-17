import tkinter
import setup
# setups
screen = tkinter.Tk()
setup.setup_win(screen)

label = tkinter.Label()
label2 = tkinter.Label()
label3 = tkinter.Label()
setup.setup_label(label=label, label2=label2, label3=label3)

entry = tkinter.Entry()
entry2 = tkinter.Entry()
setup.setup_entry(entry=entry, entry2=entry2)

button = tkinter.Button()
setup.setup_button(button)

setup.setup_placement(label=label, label2=label2, label3=label3, entry=entry, entry2=entry2, button=button)


# Button action
def button_action():
    if entry.get() == "" and entry2.get() == "":
        label3.config(text="Please enter weight and height")
    elif entry.get().isdecimal() and entry2.get() == "":
        label3.config(text="Please enter height")
    elif entry.get() == "" and entry2.get().isdecimal():
        label3.config(text="Please enter weight")
    elif entry.get().isdecimal() and entry2.get().isdecimal():
        weight = int(entry.get())
        height = int(entry2.get())
        if weight > 0 and height > 0:
            bmi = weight / ((height / 100) * (height / 100))
            result = ""
            if bmi <= 18.5:
                result = "Under Weight"
            elif 18.5 < bmi <= 24.49:
                result = "Normal"
            elif 24.49 < bmi <= 29.9:
                result = "Over Weight"
            elif 30 < bmi <= 34.9:
                result = "Obesity (Class I)"
            elif 35 < bmi <= 39.9:
                result = "Obesity (Class II)"
            elif bmi > 39.9:
                result = "Extreme Obesity"
            label3.config(text=f"Your BMI is {int(bmi)}, you are {result}")
        else:
            label3.config(text="Height or weight cannot be negative")

    else:
        label3.config(text="Please enter valid number!")


button.config(command=button_action)
screen.mainloop()
