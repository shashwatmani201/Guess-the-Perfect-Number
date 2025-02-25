import random
import tkinter as tk
from tkinter import messagebox

# Generate a random number
random_no = random.randint(1, 100)
no_of_guesses = 0

# Function to check the guess
def check_guess():
    global no_of_guesses
    try:
        user_guess = int(entry.get())
        no_of_guesses += 1
        
        if user_guess > random_no:
            result_label.config(text="Try a LOWER number!", fg="red")
        elif user_guess < random_no:
            result_label.config(text="Try a HIGHER number!", fg="blue")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it right in {no_of_guesses} attempts!\nThe number was {random_no}.")
            reset_game()
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="black")

# Function to reset the game
def reset_game():
    global random_no, no_of_guesses
    random_no = random.randint(1, 100)
    no_of_guesses = 0
    entry.delete(0, tk.END)
    result_label.config(text="Guess a number between 1-100", fg="black")

# Function to toggle full screen
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

# Function to exit full screen
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

# GUI Setup
root = tk.Tk()
root.title("Number Guessing Game")

# Set full-screen mode
root.attributes("-fullscreen", True)

# Bind keys to toggle and exit full-screen mode
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)

# UI Layout
title_label = tk.Label(root, text="Guess the Number!", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Enter a number between 1 and 100:", font=("Arial", 18))
instruction_label.pack()

entry = tk.Entry(root, font=("Arial", 20), width=10, justify="center")
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit Guess", font=("Arial", 18), command=check_guess)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="Guess a number between 1-100", font=("Arial", 18))
result_label.pack(pady=20)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 18), command=reset_game)
reset_button.pack(pady=10)

exit_label = tk.Label(root, text="Press ESC to exit full screen", font=("Arial", 12), fg="gray")
exit_label.pack(side="bottom", pady=10)

# Run the GUI
root.mainloop()
