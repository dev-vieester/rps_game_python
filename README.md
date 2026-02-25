
---

✊ Rock Paper Scissors – Python CLI Game

A command-line implementation of the classic Rock Paper Scissors game built with Python.

This project demonstrates modular design, closures, state management, and CLI argument parsing for a personalized player experience.

---

🚀 Features

* 👤 Personalized player name via CLI argument
* 🎮 Interactive command-line gameplay
* 🔁 Replay functionality
* 📊 Game count tracking
* 🏆 Score tracking (Player vs Python)
* 🧠 Closure-based state management using `nonlocal`
* 🧩 Enum-based move handling
* 🚪 Graceful exit handling

---

🧠 How It Works

The main `rps()` function initializes game state:

* `game_count`
* `player_wins`
* `python_wins`

It returns an inner function `play_rps()`.

This structure creates a **closure**, allowing the inner function to retain access to outer variables using the `nonlocal` keyword.

Example execution pattern:

```python
rock_paper_scissors = rps(player_name)
rock_paper_scissors()
```

---

🛠 Installation & Usage

1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/rock-paper-scissors-cli.git
cd rock-paper-scissors-cli
```

2️⃣ Run the Game

```bash
python rps.py -n Victor
```

Or:

```bash
python rps.py --name Victor
```

---

🎮 Game Instructions

When prompted, enter:

```
1 for Rock
2 for Paper
3 for Scissors
```

After each round, you can choose:

```
Y to play again
Q to quit
```

---

🧩 Technical Concepts Demonstrated

* Python functions as first-class objects
* Closures
* `nonlocal` keyword
* Enum usage (`enum.Enum`)
* Random selection (`random.choice`)
* CLI argument parsing (`argparse`)
* Input validation
* Recursive replay logic
* State persistence inside nested functions

---

 🏗 Code Structure Overview

* `rps()` → Initializes state
* `play_rps()` → Handles user interaction and game flow
* `decide_winner()` → Determines round outcome
* `argparse` → Handles player name from CLI

---

🔮 Possible Improvements

* Refactor into class-based architecture
* Add score persistence to file
* Add difficulty levels
* Add colored terminal output
* Add unit tests
* Convert to a pip-installable CLI tool

---

👤 Author

Victor Adeniyi
Senior Flutter Developer | AI Engineer

---


