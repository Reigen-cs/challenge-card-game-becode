# Challenge Card Game - BeCode

This project implements a card game simulation for WeTakeYourMoney online casino as part of a developer interview challenge.

## Project Structure

```
challenge-card-game-becode/
│
├── README.md
├── main.py
└── utils/
    ├── card.py
    ├── player.py
    └── game.py
```

## Features

### Must-Have Features ✅
- **Complete Deck Generation**: Creates a standard 52-card deck with all combinations of symbols (♥, ♦, ♣, ♠) and values (A, 2-10, J, Q, K)
- **Card Distribution**: Evenly distributes all cards between players
- **Turn-Based Gameplay**: Each player plays one card per turn until all cards are exhausted
- **Game Loop**: Continues until all players have no cards remaining

### Project Components

#### 1. Card System (`utils/card.py`)
- **Symbol Class**: Manages card symbols with color and icon attributes
- **Card Class**: Inherits from Symbol, adds card value
- **Deck Class**: Manages the complete deck of 52 cards with methods to:
  - Fill deck with all card combinations
  - Shuffle cards randomly
  - Distribute cards amongs the player

#### 2. Player Management (`utils/player.py`)
- **Player Class**: Represents each game participant with:
  - Hand of cards
  - Turn counter
  - Card count tracking
  - Play history
  - `play()` method that randomly selects and plays a card

#### 3. Game Logic (`utils/game.py`)
- **Board Class**: Orchestrates the entire game with:
  - Player management
  - Turn counting
  - Active card tracking
  - Game history maintenance
  - Complete game flow from start to finish

#### 4. Game Entry Point (`main.py`)
- Initializes players
- Creates game board
- Starts the game simulation

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/Reigen-cs/challenge-card-game-becode.git
cd challenge-card-game-becode
```

2. Run the game:
```bash
python main.py
```

## Game Flow

1. **Initialization**: 
   - Creates 4 players (Alice, Bob, Charlie, Diana)
   - Generates and shuffles a complete 52-card deck
   - Distributes cards evenly among players (13 cards each)

2. **Gameplay**:
   - Each turn, every player with cards plays one random card
   - Game displays turn information and card counts
   - Continues until all players are out of cards

3. **Game Over**:
   - Displays final statistics
   - Shows total turns and cards played

## Sample Output

```
Welcome to Reigen Card Game!
========================================
Starting the card game!
Players: Player 1, Player 2, Player 3, Player 4

Cards distributed! Each player starts with cards.
Player 1: 13 cards
Player 2: 13 cards
Player 3: 13 cards
Diana: 13 cards

=== TURN 1 ===
Player 1 turn 1 played: K ♠ black
Player 2 turn 1 played: 7 ♥ red
Player 3 turn 1 played: A ♦ red
Player 4 turn 1 played: Q ♣ black
Turn 1 summary:
Active cards: ['K ♠', '7 ♥', 'A ♦', 'Q ♣']
Total cards in history: 0

...
```

## Code Standards

- All classes include `__str__()` methods
- Full type hints on all functions and classes
- Comprehensive docstrings in specified format
- Clean, commented code with no unused sections
- Object-oriented design principles


## Future Enhancements (Nice-to-Have)

The next version will include:
- Interactive player input for card selection
- Scoring system based on card strength
- Win conditions and game-over logic
- Winner determination

---

*This project was created as part of the BeCode developer challenge for WeTakeYourMoney online casino.*
