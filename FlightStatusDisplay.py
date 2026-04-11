import tkinter as tk

# ---------------------------
# Flight Status Logic
# ---------------------------
def get_status_style(status):
    styles = {
        "On Time": {"bg": "#2ecc71", "fg": "white"},
        "Delayed": {"bg": "#f39c12", "fg": "white"},
        "Cancelled": {"bg": "#e74c3c", "fg": "white"},
    }
    return styles.get(status, {"bg": "gray", "fg": "white"})


# ---------------------------
# UI Function
# ---------------------------
def show_flight_status(status):
    root = tk.Tk()
    root.title("Flight Status Display")
    root.geometry("300x150")

    style = get_status_style(status)

    frame = tk.Frame(root, bg=style["bg"])
    frame.pack(expand=True, fill="both")

    label = tk.Label(
        frame,
        text=status,
        font=("Arial", 22, "bold"),
        bg=style["bg"],
        fg=style["fg"]
    )
    label.pack(expand=True)

    # Optional: status indicator dot
    dot = tk.Label(
        frame,
        text="●",
        font=("Arial", 30),
        bg=style["bg"],
        fg=style["fg"]
    )
    dot.place(x=20, y=40)

    root.mainloop()


# ---------------------------
# Run Example
# ---------------------------
if __name__ == "__main__":
    # Change this value to test:
    show_flight_status("On Time")
    # show_flight_status("Delayed")
    # show_flight_status("Cancelled")