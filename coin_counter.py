import tkinter as tk
from gpiozero import Button

button = Button(17) #GPIO pin 17

curr_coins = 0
max_coins = 3

bg_color = "green"
fg_color = "white"
font_size = 300

def update_counter():
    global curr_coins

    button.wait_for_active()

    # update coin count for GUI
    curr_coins += 1
    string_var.set(str(curr_coins) + "/" + str(max_coins))

    button.wait_for_inactive()


# setup tkinter main window
root = tk.Tk()
root.configure(bg=bg_color)
root.title("first program")
root.geometry("1920x1080")

# init string var that will hold and update coin count
string_var = tk.StringVar()
string_var.set("0/" + str(max_coins))

# widgets
label = tk.Label(root, text="Coins:", font=("Times, " + str(font_size)), fg= fg_color, bg=bg_color).pack()
count_widget = tk.Label(root, textvariable=string_var, font=("Times, " + str(font_size)),  fg= fg_color, bg=bg_color).pack()
while True:

    # update GUI elements
    root.update()

    # close program when
    if curr_coins >= max_coins:
        break

    update_counter()