
import tkinter as tk

def launch_dashboard():
    root = tk.Tk()
    root.title("Game Statistics AI Dashboard")
    root.geometry("900x600")

    label = tk.Label(
        root,
        text="Game Statistics Extrapolation Platform",
        font=("Arial", 20)
    )

    label.pack(pady=20)

    root.mainloop()
