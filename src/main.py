import tkinter as tk
from tkinter import ttk
import json
import os
from PIL import Image, ImageTk, ImageSequence
from api import get_quote  # Importing get_quote from api.py

# Load themes
file_path = os.path.join(os.path.dirname(__file__), "themes.json")
gif_folder = os.path.join(os.path.dirname(__file__), "gifs")  # Path to GIFs

try:
    with open(file_path, "r") as file:
        themes = json.load(file)
except FileNotFoundError:
    print("Error: themes.json file not found!")
    themes = {}

# Main window setup
root = tk.Tk()
root.title("QuoteIt - Mood Quotes")
root.geometry("500x550")
root.config(bg="#2c3e50")  

# Title Label
label_title = tk.Label(root, text="🌟 QuoteIt 🌟", font=("Helvetica", 20, "bold"), bg="#2c3e50", fg="white")
label_title.pack(pady=10)

# Mood selection
label_mood = tk.Label(root, text="Select Your Mood:", font=("Arial", 14, "bold"), bg="#2c3e50", fg="white")
label_mood.pack()

mood_var = tk.StringVar()
mood_options = list(themes.keys())

style = ttk.Style()
style.configure("TCombobox", font=("Arial", 12), padding=5)

mood_dropdown = ttk.Combobox(root, textvariable=mood_var, values=mood_options, state="readonly", style="TCombobox")
mood_dropdown.pack(pady=5)
mood_dropdown.current(0)

# GIF Display Setup
gif_label = tk.Label(root, bg="#2c3e50")
gif_label.pack()

# Function to load and display GIFs
frames = []
def update_gif(mood):
    global frames
    gif_path = os.path.join(gif_folder, f"{mood}.gif")  

    if os.path.exists(gif_path):
        gif = Image.open(gif_path)
        frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]

        def animate(index=0):
            if frames:
                gif_label.config(image=frames[index])
                root.after(100, animate, (index + 1) % len(frames))  # Loop GIF

        animate()
    else:
        gif_label.config(image="")  # Remove GIF if not found

# Quote display
label_quote = tk.Label(root, text="Your quote will appear here!", font=("Helvetica", 14, "italic"), wraplength=400, 
                       bg="#34495e", fg="white", justify="center", padx=20, pady=20, relief="solid", borderwidth=2)
label_quote.pack(pady=10)

# Update UI function
def update_ui():
    mood = mood_var.get()
    theme = themes.get(mood, {"bg": "#FFFFFF", "fg": "#000000"})  
    root.configure(bg=theme["bg"])
    label_quote.config(text=get_quote(mood), fg=theme["fg"], bg=theme["bg"], font=("Georgia", 14, "italic"))
    update_gif(mood)  # Update GIF on mood change

# Button with Hover Effect
def on_enter(e):
    btn_get_quote.config(bg="#e67e22", fg="white")

def on_leave(e):
    btn_get_quote.config(bg="#d35400", fg="white")

btn_get_quote = tk.Button(root, text="Get Quote", font=("Arial", 12, "bold"), bg="#d35400", fg="white", relief="flat", 
                          command=update_ui, padx=20, pady=10, cursor="hand2")
btn_get_quote.pack(pady=10)
btn_get_quote.bind("<Enter>", on_enter)
btn_get_quote.bind("<Leave>", on_leave)

# Run the UI
root.mainloop()
