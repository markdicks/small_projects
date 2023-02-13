import tkinter as tk
from datetime import datetime

class FullScreenClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Full Screen Clock")
        self.geometry("400x400")
        self.bind("<Escape>", self.exit_fullscreen)
        self.bind("f", self.toggle_fullscreen)
        self.bind("t", self.toggle_mode)

        self.is_dark_mode = True
        self.toggle_button = tk.Button(self, text="Toggle Mode", command=self.toggle_mode)
        self.toggle_button.pack(side="top", pady=10)

        # Create a label to display the time
        self.time_label = tk.Label(self, font=("Helvetica", 72), bg="#000000", fg="#FFFFFF")
        self.time_label.pack(fill="both", expand=True)

        # Create a label to display the day, date, and month
        self.date_label = tk.Label(self, font=("Helvetica", 24), bg="#000000", fg="#FFFFFF")
        self.date_label.pack(pady=10)

        # Create an overlay to inform the user how to exit full screen
        self.overlay = tk.Label(self, text="Exit full screen: 'Escape'", font=("Helvetica", 24), bg="#000000", fg="#FFFFFF")

        # Call the update_time function every 1000 milliseconds (1 second)
        self.after(1000, self.update_time)

    def update_time(self):
        now = datetime.now()
        time_string = now.strftime("%H:%M:%S")
        day = now.strftime("%A")
        date = now.strftime("%d").lstrip("0") + now.strftime("%B")
        date_string = f"{day} - {date}"

        self.time_label.configure(text=time_string)
        self.date_label.configure(text=date_string)
        self.after(1000, self.update_time)

    def toggle_fullscreen(self, event=None):
        self.attributes("-fullscreen", not self.attributes("-fullscreen"))
        if self.attributes("-fullscreen"):
            self.toggle_button.pack_forget()
            self.overlay.pack(side="bottom")
            self.after(2000, self.fade_out_overlay)
        else:
            self.toggle_button.pack(side="top", pady=10)
            self.overlay.pack_forget()

    def fade_out_overlay(self):
        self.overlay.pack_forget()

    def exit_fullscreen(self, event=None):
        self.attributes("-fullscreen", False)
        self.toggle_button.pack(side="top", pady=10)

    def toggle_mode(self, event=None):
        if self.is_dark_mode:
            self.configure(bg="#FFFFFF")
            self.time_label.configure(bg="#FFFFFF", fg="#000000")
            self.date_label.configure(bg="#FFFFFF", fg="#000000")
            self.overlay.configure(bg="#FFFFFF", fg="#000000")
            self.is_dark_mode = False
        else:
            self.configure(bg="#000000")
            self.time_label.configure(bg="#000000", fg="#FFFFFF")
            self.date_label.configure(bg="#000000", fg="#FFFFFF")
            self.overlay.configure(bg="#000000", fg="#FFFFFF")
            self.is_dark_mode = True

if __name__ == "__main__":
    app = FullScreenClock()
    app.toggle_mode()
    app.mainloop()
