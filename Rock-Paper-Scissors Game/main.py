import tkinter as tk
import random

player_score = 0
computer_score = 0
history = []

def determine_winner(player_choice):
    global player_score, computer_score
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = f"Both chose {player_choice}. It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        result = f"Computer chose {computer_choice}. You chose {player_choice}. You win!"
        player_score += 1
    else:
        result = f"Computer chose {computer_choice}. You chose {player_choice}. You lose!"
        computer_score += 1

    history.append(result)
    result_label.config(text=result)
    update_scoreboard()
    update_history()

def update_scoreboard():
    scoreboard.config(text=f"Player: {player_score}  Computer: {computer_score}")

def update_history():
    history_text = "\n".join(history[-3:])
    history_label.config(text=history_text)

def on_button_click(choice):
    determine_winner(choice)

def reset_game():
    global player_score, computer_score, history
    player_score = 0
    computer_score = 0
    history = []
    result_label.config(text="")
    update_scoreboard()
    update_history()

app = tk.Tk()
app.title("Rock Paper Scissors")

instructions = tk.Label(app, text="Choose Rock, Paper, or Scissors to play against the computer.",
                        font=("Helvetica", 14), fg="White")
instructions.pack(pady=10)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=15, command=lambda: on_button_click("rock"),
                        bg="lightgray", font=("Helvetica", 12))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=15, command=lambda: on_button_click("paper"),
                         bg="lightgray", font=("Helvetica", 12))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=15, command=lambda: on_button_click("scissors"),
                            bg="lightgray", font=("Helvetica", 12))
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(app, text="", font=("Helvetica", 12), fg="green")
result_label.pack(pady=10)

scoreboard = tk.Label(app, text="Player: 0  Computer: 0", font=("Helvetica", 12), fg="red")
scoreboard.pack(pady=10)

history_label = tk.Label(app, text="", font=("Helvetica", 10), fg="Yellow")
history_label.pack(pady=10)

play_again_button = tk.Button(app, text="Play Again", command=reset_game, bg="lightblue", font=("Helvetica", 12))
play_again_button.pack(pady=10)

exit_button = tk.Button(app, text="Exit", command=app.quit, bg="lightcoral", font=("Helvetica", 12))
exit_button.pack(pady=10)

app.mainloop()
