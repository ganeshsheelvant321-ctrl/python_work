import tkinter as tk


# -----------------------------
# Window
# -----------------------------

root = tk.Tk()
root.title("Calc App")
root.geometry("420x650")
root.configure(bg="#fffaff")
root.resizable(False, False)


# -----------------------------
# Variables
# -----------------------------

expression = ""
display_text = tk.StringVar(value="0")


# -----------------------------
# Functions
# -----------------------------

def press(value):
    global expression

    if expression == "0":
        expression = ""

    expression += str(value)
    display_text.set(expression)


def clear():
    global expression

    expression = ""
    display_text.set("0")


def calculate():
    global expression

    try:
        result = eval(expression)
        expression = str(result)
        display_text.set(expression)

    except:
        expression = ""
        display_text.set("Error")


def percent():
    global expression

    try:
        result = float(expression) / 100
        expression = str(result)
        display_text.set(expression)

    except:
        display_text.set("Error")


def plus_minus():
    global expression

    try:
        if expression:
            result = -float(expression)
            expression = str(result)
            display_text.set(expression)

    except:
        display_text.set("Error")


# -----------------------------
# Header
# -----------------------------

header = tk.Frame(root, bg="#fffaff")
header.pack(fill="x", pady=(15, 5))

title = tk.Label(
    header,
    text="◀ Calc App",
    font=("Arial", 20),
    bg="#fffaff",
    fg="#777777"
)

title.pack(anchor="w", padx=20)


# -----------------------------
# Calculator Body
# -----------------------------

calculator = tk.Frame(
    root,
    bg="black",
    width=380,
    height=550
)

calculator.pack(padx=17, pady=25)
calculator.pack_propagate(False)


# -----------------------------
# Display
# -----------------------------

display = tk.Label(
    calculator,
    textvariable=display_text,
    font=("Arial", 40),
    bg="black",
    fg="white",
    anchor="e"
)

display.pack(
    fill="x",
    padx=25,
    pady=(35, 20)
)


# -----------------------------
# Button Frame
# -----------------------------

button_frame = tk.Frame(
    calculator,
    bg="black"
)

button_frame.pack(
    padx=20,
    pady=5,
    fill="both",
    expand=True
)


# -----------------------------
# Button Styling
# -----------------------------

number_color = "#36393d"
function_color = "#cbd1da"
operator_color = "#f59b00"


def create_button(
    text,
    row,
    column,
    command,
    bg,
    fg="white",
    colspan=1
):

    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Arial", 20),
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        bd=0,
        relief="flat",
        highlightthickness=0
    )

    button.grid(
        row=row,
        column=column,
        columnspan=colspan,
        padx=8,
        pady=8,
        sticky="nsew"
    )

    return button


# -----------------------------
# Grid Configuration
# -----------------------------

for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)


# -----------------------------
# Row 1
# -----------------------------

create_button(
    "AC",
    0, 0,
    clear,
    function_color,
    "black"
)

create_button(
    "+/-",
    0, 1,
    plus_minus,
    function_color,
    "black"
)

create_button(
    "%",
    0, 2,
    percent,
    function_color,
    "black"
)

create_button(
    "/",
    0, 3,
    lambda: press("/"),
    operator_color
)


# -----------------------------
# Row 2
# -----------------------------

create_button("7", 1, 0, lambda: press("7"), number_color)
create_button("8", 1, 1, lambda: press("8"), number_color)
create_button("9", 1, 2, lambda: press("9"), number_color)
create_button("*", 1, 3, lambda: press("*"), operator_color)


# -----------------------------
# Row 3
# -----------------------------

create_button("4", 2, 0, lambda: press("4"), number_color)
create_button("5", 2, 1, lambda: press("5"), number_color)
create_button("6", 2, 2, lambda: press("6"), number_color)
create_button("-", 2, 3, lambda: press("-"), operator_color)


# -----------------------------
# Row 4
# -----------------------------

create_button("1", 3, 0, lambda: press("1"), number_color)
create_button("2", 3, 1, lambda: press("2"), number_color)
create_button("3", 3, 2, lambda: press("3"), number_color)
create_button("+", 3, 3, lambda: press("+"), operator_color)


# -----------------------------
# Row 5
# -----------------------------

create_button(
    "0",
    4, 0,
    lambda: press("0"),
    number_color,
    colspan=2
)

create_button(
    ".",
    4, 2,
    lambda: press("."),
    number_color
)

create_button(
    "=",
    4, 3,
    calculate,
    operator_color
)


# -----------------------------
# Run Application
# -----------------------------

root.mainloop()
                   