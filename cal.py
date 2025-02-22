from customtkinter import *

set_appearance_mode("black")
app = CTk()
app.geometry("400x570")
app.resizable(False, False)

button_width = 50
button_height = 60
radius = button_width + button_height

entry = CTkEntry(
    master=app, placeholder_text="0", bg_color="#495057", width=389, height=190,
    text_color="#FFCC70", corner_radius=10, font=('arial', 40,), justify='right'
)
entry.place(x=5, y=5)

first_number = None
operator = None

# Function to update the entry field dynamically
def button_click(value):
    current_text = entry.get()
    if current_text == "0":
        entry.delete(0, "end")
    entry.insert("end", value)

# Function to perform the calculation
def calculation():
    global first_number, operator
    if operator and first_number is not None:
        second_number = float(entry.get())
        try:
            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "x":
                result = first_number * second_number
            elif operator == "÷":
                result = first_number / second_number if second_number != 0 else "Error"

            entry.delete(0, "end")
            entry.insert("end", str(result))
            first_number = None
            operator = None
        except Exception:
            entry.delete(0, "end")
            entry.insert("end", "Error")

# Function to store the first number and operator
def operator_click(op):
    global first_number, operator
    if first_number is None:
        first_number = float(entry.get())
        operator = op
        entry.delete(0, "end")

# Function to clear the calculator (AC button)
def clear():
    global first_number, operator
    first_number = None
    operator = None
    entry.delete(0, "end")
    entry.insert("end", "0")

# Function to handle percentage calculation
def percentage():
    try:
        value = float(entry.get()) / 100
        entry.delete(0, "end")
        entry.insert("end", str(value))
    except ValueError:
        entry.delete(0, "end")
        entry.insert("end", "Error")

# Function to toggle positive/negative sign
def toggle_sign():
    try:
        value = float(entry.get())
        entry.delete(0, "end")
        entry.insert("end", str(-value))
    except ValueError:
        entry.delete(0, "end")
        entry.insert("end", "Error")

buttons = [
    ("7", 20, 280), ("8", 120, 280), ("9", 220, 280),
    ("4", 20, 350), ("5", 120, 350), ("6", 220, 350),
    ("1", 20, 420), ("2", 120, 420), ("3", 220, 420),
    (".", 220, 490)
]

fn_btn = [
    ("AC", 20, 210, clear), ("-/+", 120, 210, toggle_sign), ("%", 220, 210, percentage)
]

o_btn = [("0", 20, 490)]
sum_btn = [("=", 315, 490)]
cal_btn = [("÷", 315, 210), ("x", 315, 280), ("-", 315, 350), ("+", 315, 420)]

for text, x, y, cmd in fn_btn:
    btn = CTkButton(
        app, text=text, width=button_width, height=button_height,
        corner_radius=radius // 2, fg_color="#a5a5a5",
        text_color="black", hover_color="green",
        font=('arial', 20), command=cmd
    )
    btn.place(x=x, y=y)

for text, x, y in buttons:
    btn = CTkButton(
        app, text=text, width=button_width, height=button_height,
        corner_radius=radius // 2, fg_color="#333333",
        text_color="white", hover_color="green",
        font=('arial', 20), command=lambda t=text: button_click(t)
    )
    btn.place(x=x, y=y)

for text, x, y in o_btn:
    btn = CTkButton(
        app, text=text, width=180, height=button_height,
        corner_radius=radius // 2, fg_color="#333333",
        text_color="white", hover_color="green",
        font=('arial', 20), command=lambda t=text: button_click(t)
    )
    btn.place(x=x, y=y)

for text, x, y in sum_btn:
    btn = CTkButton(
        app, text=text, width=button_width, height=button_height,
        corner_radius=radius // 2, fg_color="#ffa00b",
        text_color="white", hover_color="green",
        font=('arial', 28), command=calculation
    )
    btn.place(x=x, y=y)

for text, x, y in cal_btn:
    btn = CTkButton(
        app, text=text, width=button_width, height=button_height,
        corner_radius=radius // 2, fg_color="#ffa00b",
        text_color="white", hover_color="green",
        font=('arial', 28), command=lambda t=text: operator_click(t)
    )
    btn.place(x=x, y=y)

app.mainloop()
