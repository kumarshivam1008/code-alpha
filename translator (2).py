import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from googletrans import Translator, LANGUAGES
from tkinter import font
import random

# Initialize the Translator
translator = Translator()

# Function to translate the input text
def translate_text():
    source_lang = source_language_dropdown.get()
    target_lang = target_language_dropdown.get()
    text_to_translate = input_textbox.get(1.0, tk.END).strip()

    if not text_to_translate:
        messagebox.showerror("Input Error", "Please enter text to translate.")
        return

    progress_bar.start()

    try:
        translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        output_textbox.delete(1.0, tk.END)
        output_textbox.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")
    finally:
        progress_bar.stop()

# Function to clear both input and output textboxes
def clear_text():
    input_textbox.delete(1.0, tk.END)
    output_textbox.delete(1.0, tk.END)

# Crazy effect 1: Flashing text
def flash_title():
    current_color = title_label.cget("fg")
    next_color = "blue" if current_color == "white" else "white"
    title_label.config(fg=next_color)
    root.after(500, flash_title)  # Call this function again after 500ms

# Crazy effect 2: Changing background colors randomly
def change_bg_color():
    colors = ["#2E2E2E", "#1E1E1E", "#282828", "#3A3A3A", "#444444"]
    random_color = random.choice(colors)
    root.config(bg=random_color)
    language_frame.config(bg=random_color)
    input_text_label.config(bg=random_color)
    output_text_label.config(bg=random_color)
    title_label.config(bg=random_color)
    root.after(1000, change_bg_color)  # Change color every 1000ms

# Crazy effect 3: Hover effect on buttons
def on_hover_enter(event):
    event.widget.config(bg="#FF6347")  # Change to a "crazy" color on hover

def on_hover_leave(event):
    event.widget.config(bg="#4CAF50")  # Change back to the original color

# Initialize the main window with a theme
root = ThemedTk(theme="arc")
root.title("Crazy Language Translator")
root.geometry("800x800")
root.config(bg="#2E2E2E")

# Set custom fonts
heading_font = font.Font(family="canva sans", size=20, weight="bold")
text_font = font.Font(family="Arial", size=16)

# Adding a title label
title_label = tk.Label(root, text="Crazy Language Translator", font=heading_font, bg="#2E2E2E", fg="white")
title_label.pack(pady=10)

# Start the flashing text effect
flash_title()

# Dropdown options (languages)
languages_list = list(LANGUAGES.values())

# Create a frame for language selection
language_frame = tk.Frame(root, bg="#2E2E2E")
language_frame.pack(pady=10)

# Source language dropdown
source_language_label = tk.Label(language_frame, text="Source Language:", bg="#2E2E2E", fg="white", font=text_font)
source_language_label.grid(row=0, column=0, padx=10)

source_language_dropdown = ttk.Combobox(language_frame, values=languages_list, width=20)
source_language_dropdown.set("English")
source_language_dropdown.grid(row=0, column=1, padx=10)

# Target language dropdown
target_language_label = tk.Label(language_frame, text="Target Language:", bg="#2E2E2E", fg="white", font=text_font)
target_language_label.grid(row=0, column=2, padx=10)

target_language_dropdown = ttk.Combobox(language_frame, values=languages_list, width=20)
target_language_dropdown.set("Hindi")
target_language_dropdown.grid(row=0, column=3, padx=10)

# Textbox for input
input_text_label = tk.Label(root, text="Enter Text to Translate:", bg="#2E2E2E", fg="white", font=text_font)
input_text_label.pack(pady=5)

input_textbox = tk.Text(root, height=8, width=60, font=text_font, bg="#1E1E1E", fg="white", insertbackground="white")
input_textbox.pack(pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text, font=text_font, bg="#4CAF50", fg="white")
translate_button.pack(pady=10)

# Hover effect for translate button
translate_button.bind("<Enter>", on_hover_enter)
translate_button.bind("<Leave>", on_hover_leave)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
progress_bar.pack(pady=5)

# Textbox for output
output_text_label = tk.Label(root, text="Translated Text:", bg="#2E2E2E", fg="white", font=text_font)
output_text_label.pack(pady=5)

output_textbox = tk.Text(root, height=8, width=60, font=text_font, bg="#1E1E1E", fg="white", insertbackground="white")
output_textbox.pack(pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_text, font=text_font, bg="#f44336", fg="white")
clear_button.pack(pady=10)

# Hover effect for clear button
clear_button.bind("<Enter>", on_hover_enter)
clear_button.bind("<Leave>", on_hover_leave)

# Start the background color changing effect
change_bg_color()

# Start the application's GUI loop
root.mainloop()
