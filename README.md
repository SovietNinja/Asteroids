# Asteroids

A classic Asteroids clone built with Python and [pygame](https://www.pygame.org/). Pilot a ship around the screen, dodge and shoot asteroids as they split into smaller pieces, and try not to get hit.

## Requirements

- Python 3
- [pygame](https://www.pygame.org/) 2.6.1

## Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/SovietNinja/Asteroids.git
cd Asteroids

python3 -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Running the game

```bash
python3 main.py
```

## Controls

| Key | Action |
|---|---|
| `W` | Thrust forward |
| `S` | Thrust backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

Colliding with an asteroid ends the game.

## How it works

- The player ship is a rotating triangle drawn each frame based on its heading.
- Asteroids spawn periodically at the screen edges via an `AsteroidField` and drift across the screen.
- Shooting an asteroid splits it into smaller asteroids until it's small enough to be destroyed outright.
- Colliding with an asteroid prints `Game over!` and exits.

## Project structure

```
.
├── main.py             # Game loop: init, update, collision checks, draw
├── player.py           # Player ship: movement, rotation, shooting
├── asteroid.py         # Asteroid behavior and splitting logic
├── asteroidfield.py    # Spawns asteroids at screen edges over time
├── shot.py             # Projectile behavior
├── circleshape.py      # Shared base class for circular collidable objects
├── constants.py        # Screen size, speeds, cooldowns, and other tunables
└── requirements.txt    # Python dependencies (pygame)
```
