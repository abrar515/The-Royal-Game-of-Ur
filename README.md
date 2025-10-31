# The Royal Game of Ur
*A modern Python recreation of the world’s oldest known board game*

---

## Overview
**The Royal Game of Ur** is a two-player strategy race from ancient Mesopotamia, over 4,600 years old.
This project revives it in the terminal with ASCII art, Unicode graphics, rosette mechanics, and tetrahedral dice rolls.

---

## Features
- Two-player turn system (⬜️ vs ⚪️)
- Dynamic board rendering
- Four-die binary rolls (0 or 1 per die)
- Rosette safe cells grant extra rolls
- Capture mechanics send opponents’ pieces home


---

## Project Structure
```
The-Royal-Game-of-Ur/
│
├── Ur_Game.py              # main game file
├── test_Ur_Game.py         # Unit tests for game functions
├── requirements.txt        # Dependencies (tabulate, pytest)
└── README.md               # Project documentation
```

---




## How to Run the Game
```bash
# 1. Clone the repository
git clone https://github.com/abrar515/The-Royal-Game-of-Ur.git
cd The-Royal-Game-of-Ur

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the game
python Ur_Game.py

```

---

## Gameplay
Each player rolls **four binary dice**.
▲ counts as 1 and △ counts as 0
The number of “▲” equals how many spaces or cells a piece can move.

Example:
```
▲  △  ▲  △   → 2 steps
```

### Board Layout
- Top & bottom rows → private tracks
- Middle row → shared battle path
- Rosettes → safe zones with extra turns
- Finish all pieces to win
```
╔═══════╦═══════╦═══════╦═══════╗               ╔═══════╦═══════╗
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
║ │   │ ║       ║       ║       ║               ║ │   │ ║       ║
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
╠═══════╬═══════╬═══════╬═══════╬═══════╦═══════╬═══════╣═══════╣
║       ║       ║       ║ +---+ ║       ║       ║       ║       ║
║       ║       ║       ║ │   │ ║       ║       ║       ║       ║
║       ║       ║       ║ +---+ ║       ║       ║       ║       ║
╠═══════╬═══════╬═══════╬═══════╬═══════╩═══════╬═══════╣═══════╣
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
║ │   │ ║       ║       ║       ║               ║ │   │ ║       ║
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
╚═══════╩═══════╩═══════╩═══════╝               ╚═══════╩═══════╝
```
---

## Rules
1. Each player starts with 7 pieces.
2. Roll the dice → move any valid piece that many steps.
3. Landing on an opponent’s piece captures it.
4. Landing on a rosette grants another roll and safety.
5. You must roll the exact number to finish a piece.
6. The first to bring all pieces home wins.



---
## Path
```
╔═══════╦═══════╦═══════╦═══════╗               ╔═══════╦═══════╗
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
║ │   │ ║       ║       ║       ║               ║ │   │ ║       ║
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
╠═══════╬═══════╬═══════╬═══════╬═══════╦═══════╬═══════╣═══════╣
║       ║       ║       ║ +---+ ║       ║       ║       ║       ║
║   ┌───┼───────┼───────┼─┼───┼─┼───────┼───────┼───────┼────┐  ║
║   │   ║       ║       ║ +---+ ║       ║       ║       ║    │  ║
╠═══┼═══╬═══════╬═══════╬═══════╣═══════╩═══════╬═══════╬════┼══╣
║ +-│-+ ║       ║       ║       ║               ║ +---+ ║    │  ║
║ │ └─┼─┼───────┼───────┼───────┼◄─START   END ◄┼─┼───┼─┼────┘  ║
║ +---+ ║       ║       ║       ║               ║ +---+ ║       ║
╚═══════╩═══════╩═══════╩═══════╝               ╚═══════╩═══════╝
```

---

## Author
Created by **Abrar Ahmad** as the **Final Project for CS50’s Introduction to Programming with Python (CS50P)** — 2025.
> “The oldest game reborn in code.”

---
