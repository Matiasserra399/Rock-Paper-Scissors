import tkinter as tk
import random

def computer_turn():
    rand_num = random.randint(1, 3)

    if rand_num == 1:
        return "ROCK"
    elif rand_num == 2:
        return "PAPER"
    elif rand_num == 3:
        return "SCISSORS"

def check_winner(player, computer):
    if player == computer:
        return "Draw!"
    elif computer == "ROCK":
        return "You Win!" if player == "PAPER" else "You Lose!"
    elif computer == "PAPER":
        return "You Win!" if player == "SCISSORS" else "You Lose!"
    elif computer == "SCISSORS":
        return "You Win!" if player == "ROCK" else "You Lose!"

def on_choice_button_click(choice):
    global player
    global computer
    global game_counter
    global win_counter
    global loss_counter

    player = choice
    computer = computer_turn()

    player_text.config(text=f"Player: {player}")
    computer_text.config(text=f"Computer: {computer}")
    result_text.config(text=check_winner(player, computer))

    game_counter += 1
    if check_winner(player, computer) == "You Win!":
        win_counter += 1
    elif check_winner(player, computer) == "You Lose!":
        loss_counter += 1

    update_counters()

def update_counters():
    counter_text.config(text=f"Games Played: {game_counter}\nWins: {win_counter}\nLosses: {loss_counter}")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

player_text = tk.Label(root, text="Player: ")
player_text.pack()

computer_text = tk.Label(root, text="Computer: ")
computer_text.pack()

result_text = tk.Label(root, text="")
result_text.pack()
choices = ["ROCK", "PAPER", "SCISSORS"]
for choice in choices:
    choice_button = tk.Button(root, text=choice, command=lambda c=choice: on_choice_button_click(c))
    choice_button.pack()

counter_text = tk.Label(root, text="")
counter_text.pack()


game_counter = 0
win_counter = 0
loss_counter = 0


root.mainloop()