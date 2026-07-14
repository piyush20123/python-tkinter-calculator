import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1f1f1f")

        self.expression = ""

        # ---------------- Display ----------------
        self.display_var = tk.StringVar()

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 28, "bold"),
            justify="right",
            bg="#2d2d2d",
            fg="white",
            insertbackground="white",
            relief="flat",
            bd=10
        )
        display.grid(row=0, column=0, columnspan=4,
                     sticky="nsew", padx=10, pady=10, ipady=20)

        # Make grid expand evenly
        for i in range(1, 7):
            root.grid_rowconfigure(i, weight=1)

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        # ---------------- Buttons ----------------

        buttons = [
            ("C", 1, 0),
            ("⌫", 1, 1),
            ("(", 1, 2),
            (")", 1, 3),

            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("/", 2, 3),

            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("*", 3, 3),

            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("-", 4, 3),

            ("0", 5, 0),
            (".", 5, 1),
            ("%", 5, 2),
            ("+", 5, 3),

            ("=", 6, 0),
        ]

        for (text, row, col) in buttons:

            if text in "+-*/":
                bg = "#ff9800"
                fg = "black"

            elif text == "=":
                bg = "#4CAF50"
                fg = "black"

            elif text in ["C", "⌫"]:
                bg = "#d32f2f"
                fg = "black"

            elif text in ["(", ")", "%"]:
                bg = "#607D8B"
                fg = "black"

            else:
                bg = "#E0E0E0"
                fg = "black"

            command = lambda t=text: self.click(t)

            if text == "=":
                tk.Button(
                    root,
                    text=text,
                    font=("Arial", 20, "bold"),
                    bg=bg,
                    fg=fg,
                    activebackground=bg,
                    activeforeground="white",
                    relief="flat",
                    command=command
                ).grid(
                    row=row,
                    column=col,
                    columnspan=4,
                    sticky="nsew",
                    padx=5,
                    pady=5
                )
            else:
                tk.Button(
                    root,
                    text=text,
                    font=("Arial", 18, "bold"),
                    bg=bg,
                    fg=fg,
                    activebackground=bg,
                    activeforeground="white",
                    relief="flat",
                    command=command
                ).grid(
                    row=row,
                    column=col,
                    sticky="nsew",
                    padx=5,
                    pady=5
                )

        # ---------------- Keyboard ----------------

        root.bind("<Key>", self.key_press)

    # ---------------- Button Logic ----------------

    def click(self, value):

        if value == "C":
            self.expression = ""

        elif value == "⌫":
            self.expression = self.expression[:-1]

        elif value == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"

        else:
            self.expression += value

        self.display_var.set(self.expression)

    # ---------------- Keyboard ----------------

    def key_press(self, event):

        key = event.keysym

        if event.char in "0123456789+-*/().%":
            self.expression += event.char

        elif key == "Return":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"

        elif key == "BackSpace":
            self.expression = self.expression[:-1]

        elif key == "Escape":
            self.expression = ""

        self.display_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()