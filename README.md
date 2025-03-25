## 🕹️ **Number Guessing Game (Python)**

This repository contains a **Number Guessing Game** built with Python. The game challenges the player to guess a randomly generated number between **1 and 100**. Players can select between **easy** (10 attempts) and **hard** (5 attempts) difficulty levels. With each guess, the game provides hints if the guess is **too high** or **too low**. The game ends when the player correctly guesses the number or runs out of attempts. 

This project is a great way to understand Python basics like user input, condition handling, loops, and exception handling.

---

### 📌 **How the Game Works:**
1. The game starts by generating a random number between **1 and 100**.
2. Players choose the difficulty level:
   - **Easy:** 10 attempts
   - **Hard:** 5 attempts
3. Players guess the number, and the game provides feedback:
   - "Too high" if the guess is greater than the target number.
   - "Too low" if the guess is smaller.
4. The game continues until the player either guesses correctly or uses all their attempts.
5. If the player guesses the number, they win; otherwise, the correct number is revealed when attempts are exhausted.

---

### 📊 **Python Concepts Used:**

1. **Random Number Generation:**
   - `random.randint(1, 100)` generates a random integer between **1** and **100**.

2. **Input Handling and Case Conversion:**
   - `input()` is used to take input from the player.
   - `.lower()` ensures input is case-insensitive (e.g., accepting "Easy" and "easy").

3. **Conditional Statements (`if-elif-else`):**
   - Determines the number of attempts based on difficulty.
   - Compares the user’s guess with the random number and gives appropriate feedback.

4. **Loops:**
   - **`while True`**: Infinite loop to handle difficulty input until valid input is received.
   - **`while attempts_left > 0`**: Runs the main game logic and decreases the attempt count after each guess.

5. **Exception Handling (`try-except`):**
   - **`ValueError`** is handled if the user enters non-integer input. This prevents the program from crashing.

6. **String Formatting:**
   - `f-strings` are used for clean and efficient output (e.g., displaying remaining attempts and results).

---

### 🚀 **How to Run the Game:**
1. Ensure Python is installed on your system (version **3.x**).
2. Clone this repository:
   ```
   git clone https://github.com/juniorcoderr/number-guessing-game.git
   cd number-guessing-game
   ```
3. Run the game:
   ```
   python main.py
   ```
4. Follow the prompts to choose a difficulty level and start guessing!

---

Feel free to explore, play, and enhance the code! 🧑‍💻
