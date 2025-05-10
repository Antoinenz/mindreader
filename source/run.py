import tkinter as tk
from tkinter import messagebox
import random
from tkinter import ttk
import os


class MindReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind Reader")
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        window_width = 200
        window_height = 150
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
        self.root.geometry("250x150")
        self.label = tk.Label(root, text="Please enter a number")
        self.label.pack(pady=10)

        self.number_input = tk.Entry(root)
        self.number_input.pack(pady=5)

        self.guess_button = tk.Button(root, text="Read Mind", command=self.check_guess)
        self.guess_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.number_input.get())
            
            # Create a new window for the loading screen
            loading_screen = tk.Toplevel(self.root)
            loading_screen.title("Reading Mind")
            loading_screen.geometry("300x100")
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
            if os.path.exists(icon_path):
                loading_screen.iconbitmap(icon_path)
            window_width = 300
            window_height = 100
            x_coordinate = int((screen_width / 2) - (window_width / 2))
            y_coordinate = int((screen_height / 2) - (window_height / 2))
            loading_screen.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
            
            messages = ["Reading your mind...", "Analyzing thoughts...", "Calculating brainwaves...", "Almost there..."]
            label = tk.Label(loading_screen, text=messages[0])
            label.pack(pady=10)

            def update_text(index=0):
                label.config(text=messages[index])
                next_index = (index + 1) % len(messages)
                loading_screen.after(1500, update_text, next_index)

            update_text()
            
            progress = tk.DoubleVar()
            progress_bar = ttk.Progressbar(loading_screen, mode='indeterminate')
            progress_bar.start(10)
            progress_bar.pack(pady=20, fill=tk.X, padx=20)
            def update_progress(value=0):
                if value <= 100:
                    progress.set(value)
                    loading_screen.update_idletasks()
                    loading_screen.after(50, update_progress, value + 1)
                else:
                    loading_screen.destroy()
                    messagebox.showinfo("Your Number", f"You are thinkig of the number {guess}")
            
            self.root.after(0, update_progress)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MindReaderApp(root)
    root.mainloop()