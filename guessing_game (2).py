import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game 🎮")
        self.root.geometry("420x320")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")  # Dark background

        self.number = random.randint(1, 100)
        self.attempts = 0

        # Title
        self.label_title = tk.Label(root, text="🎯 Guess the Number (1-100)", 
                                    font=("Arial", 16, "bold"), bg="#1e1e2e", fg="#f8f8f2")
        self.label_title.pack(pady=15)

        # Input
        self.entry = tk.Entry(root, font=("Arial", 14), justify="center", bg="#f8f8f2")
        self.entry.pack(pady=10)

        # Submit button
        self.button = tk.Button(root, text="Guess ✅", font=("Arial", 12, "bold"), 
                                bg="#50fa7b", fg="black", width=12, command=self.check_guess)
        self.button.pack(pady=10)

        # Result message
        self.label_result = tk.Label(root, text="", font=("Arial", 13, "bold"), 
                                     bg="#1e1e2e", fg="#8be9fd")
        self.label_result.pack(pady=15)

        # Restart button
        self.restart_button = tk.Button(root, text="🔄 Restart", font=("Arial", 12, "bold"), 
                                        bg="#ff5555", fg="white", width=12, command=self.restart_game)
        self.restart_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number:
                self.label_result.config(text="⬆️ Too low! Try again.", fg="#ffb86c")
            elif guess > self.number:
                self.label_result.config(text="⬇️ Too high! Try again.", fg="#ff79c6")
            else:
                self.label_result.config(
                    text=f"🏆 Correct! You guessed it in {self.attempts} tries 🎉",
                    fg="#50fa7b"
                )
        except ValueError:
            self.label_result.config(text="❌ Please enter a valid number.", fg="#ff5555")

    def restart_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.label_result.config(text="", fg="#8be9fd")
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
