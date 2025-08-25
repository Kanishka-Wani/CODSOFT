import tkinter as tk
from tkinter import ttk, messagebox
import random

# Choices and rules
choices = ["Rock", "Paper", "Scissors"]

# Game logic: what beats what
def get_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Tie"
    if (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Scissors" and comp_choice == "Paper") or
        (user_choice == "Paper" and comp_choice == "Rock")
    ):
        return "User"
    else:
        return "Computer"

# Initialize scores
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)

    winner = get_winner(user_choice, comp_choice)

    if winner == "User":
        result = "You win!"
        user_score += 1
    elif winner == "Computer":
        result = "You lose!"
        comp_score += 1
    else:
        result = "It's a tie!"

    # Update GUI labels
    label_user_choice.config(text=f"Your Choice: {user_choice}")
    label_comp_choice.config(text=f"Computer Choice: {comp_choice}")
    label_result.config(text=result)
    label_score.config(text=f"Score - You: {user_score}  Computer: {comp_score}")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    label_user_choice.config(text="Your Choice: None")
    label_comp_choice.config(text="Computer Choice: None")
    label_result.config(text="Make your move!")
    label_score.config(text="Score - You: 0  Computer: 0")

# Set up the GUI window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.resizable(False, False)
root.config(bg="#f0f0f0")

header = ttk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
header.pack(pady=15)

frame_choices = ttk.Frame(root)
frame_choices.pack(pady=10)

btn_rock = ttk.Button(frame_choices, text="Rock", command=lambda: play("Rock"), width=10)
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = ttk.Button(frame_choices, text="Paper", command=lambda: play("Paper"), width=10)
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = ttk.Button(frame_choices, text="Scissors", command=lambda: play("Scissors"), width=10)
btn_scissors.grid(row=0, column=2, padx=5)

label_user_choice = ttk.Label(root, text="Your Choice: None", font=("Arial", 12))
label_user_choice.pack(pady=5)

label_comp_choice = ttk.Label(root, text="Computer Choice: None", font=("Arial", 12))
label_comp_choice.pack(pady=5)

label_result = ttk.Label(root, text="Make your move!", font=("Arial", 16, "bold"))
label_result.pack(pady=15)

label_score = ttk.Label(root, text="Score - You: 0  Computer: 0", font=("Arial", 12))
label_score.pack(pady=5)

btn_reset = ttk.Button(root, text="Reset Game", command=reset_game)
btn_reset.pack(pady=10)

root.mainloop()
